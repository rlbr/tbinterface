import subprocess
import datetime
import shutil
import os
import re
import time

date_format = "%Y-%m-%d_%H.%M.%S"
_adb = r"c:\Program Files (x86)\ADB\adb.exe"
screenshots = r"X:\Users\Ralphie\Pictures\Screenshots"
nandroids = r"X:\Users\Ralphie\Android\TWRP"
titanium = r"X:\Users\Ralphie\Android\TitaniumBackup"
harbor = r"X:\Users\Ralphie\Android\harbor"
updates = r"X:\Users\Ralphie\Downloads\sort\phone_updates"

dirs = (
    screenshots,
    titanium,
    nandroids,
    )

phone_dirs = {
    "screenshots":"/sdcard/Pictures/Screenshots",
    "titanium_backup":"/sdcard/TitaniumBackup",
    "updates":"/data/lineageos_updates",
    }

def adb(*args,out= False):
    """wrapper for calling adb commands using the subprocess module"""
    args = list((_adb,)+args)
    if out:
        return subprocess.check_output(args,shell = False).decode()
    else:
        subprocess.call(args,shell = False)

def get_info():
    thing = adb("devices","-l",out = True)
    formed = list(filter(bool,thing.split("\r\n")))
    main = []
    for device in formed[1:]:
        categories = re.split(" +",device)
        device_dict = {
            "serial":categories[0],
            "mode":categories[1]
            }
        
        device_dict.update(dict(category.split(":") for category in categories[2:]))
        main.append(device_dict)
    return main


def prim_device():
    prim_device_serial = []
    while len(prim_device_serial) == 0:
        prim_device_serial = get_info()
    return prim_device_serial[0]["serial"]

def reboot(mode = None,serial = None):
    if not serial:
        serial = prim_device()
    if mode:
        adb("-s",serial,"reboot",mode)
    else:
        adb("-s",serial,"reboot")
    
def delete_on_phone(path,serial = None):
    if not serial:
        serial = prim_device()
    adb("-s",serial,"shell","rm","-rf",path)

def wipe(partition,serial = None):
    if not serial:
        serial = prim_device()
    adb("-s",serial,"shell","twrp","wipe",partition)
def move_to_dir(phone,computer,delete_dups = True,serial = None):
    if not serial:
        serial = prim_device()
    flag = False
    if os.path.exists(computer):
        last = os.path.split(computer)[-1]
        real_dir = computer
        computer = os.path.join(harbor,last)
        flag = True
    adb("-s",serial,"pull","-a",phone,computer)
    delete_on_phone(phone,serial = serial)
    if flag:
        shutil.merge(computer,real_dir)
        if os.path.exists(computer) and delete_dups:
            shutil.rmtree(computer)
def push(fullpath,phone,serial = None):
    if not serial:
        serial = prim_device()
    adb('-s',serial,'push',fullpath,phone)
def backup(*partitions,name = None,backupdir = nandroids,serial = None):
    if not serial:
        serial = prim_device()
    options_dict = {
        "system": "S",
        "data": "D",
        "cache": "C",
        "recovery": "R",
        "spec_part_1": "1",
        "spec_part_2": "2",
        "spec_part_3": "3",
        "boot": "B",
        "as": "A"
    }
    options = "".join(options_dict[option] for option in partitions)

    if not name:
        name = "backup_"+datetime.datetime.today().strftime(date_format)
        
    filename = os.path.join(backupdir,name)
    adb("-s",serial,"shell","twrp","backup",options,name)
    phone_dir = "/data/media/0/TWRP/BACKUPS/{serial}/{name}".format(serial = serial,name = name)
    move_to_dir(phone_dir,filename)
