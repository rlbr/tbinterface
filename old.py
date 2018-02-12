import os
import sys
sys.path.insert(0,r'X:\Users\Raphael\Google Drive\Python\Scripts')
from find_file import find_file
from saveto import save
from datetime import datetime
backup_dir = r'D:\Android\TitaniumBackup'

def parse(prop_file):
    parsed = {}
    p = prop_file
    prop_file = open(prop_file,'r')
    raw = prop_file.read()
    prop_file.close()
    praw = list(filter(lambda x: x,raw.split('\n')))
    parsed['datetime'] = datetime.strptime(praw[1][1:],'%a %b %d %H:%M:%S CDT %Y')
    for row in praw[2:]:
        if row[0] != '#':
            row = row.split('=')
            if len(row) == 2:
                parsed[row[0]] = row[1]
            else:
                parsed[row[0]] = ''
    try:
        identity = parsed['app_label']
        del parsed['app_label']
    except KeyError:
        identity = parsed['app_gui_label']
        del parsed['app_gui_label']
    parsed['id'] = identity
    parsed['file_name'] = p
    return parsed

def get_files(prop):
    md5 = prop['app_apk_md5']
    apk = list(filter(lambda x: md5 in x,os.listdir(backup_dir)))[0]
    return [
        '{}{sep}{}'.format(backup_dir,apk,sep=os.sep),
        prop['file_name'],
        prop['file_name'].replace('.properties','.tar.gz')
        ]
properties = find_file(backup_dir,lambda x: '.properties' in x)
big_old_dict = {}

for entry in properties:
    entry = parse(entry)
    if not entry['id'] in big_old_dict.keys():
        big_old_dict[entry['id']] = {}
    big_old_dict[entry['id']][entry['datetime']] = entry
