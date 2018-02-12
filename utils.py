import os
import prop_class
import shutil
from multiprocessing import Pool
from common import push,phone_dirs


def parse_dir(direct = prop_class.backupdir):
    listing = list(
        os.path.join(direct,file) for file in filter(
            lambda file: file.endswith('.properties') and not "com.keramidas.virtual" in file,os.listdir(direct)
            )
        )
    p = Pool(processes = 4)
    apps =p.map(prop_class.parsed,listing)
    p.close()
    p.join()
    return apps

def parse_dir2(direct = prop_class.backupdir):
    listing = list(
        os.path.join(direct,file) for file in filter(
            lambda file: file.endswith('.properties') and not "com.keramidas.virtual" in file,os.listdir(direct)
            )
        )
    apps =list(map(prop_class.parsed,listing))

    return apps

class app_backup:
    def __init__(self,name,applist):
        self.name = name
        self.backups,self.remaining = self.sift(applist)
    def sift(self,applist):
        name = self.name
        backups = []
        remaining = []
        for app in applist:
            if app.name == name:
                backups.append(app)
            else:
                remaining.append(app)
        return (sorted(backups,key = lambda app: app.time),remaining)
def enum(applist):
    names = sorted(set(map(lambda app: app.name,applist)))
    spl = []
    ui = []
    for id1,app in enumerate(names):
        backups = app_backup(app,applist)
        applist = backups.remaining
        backups = list(reversed(backups.backups))
        spl.append(backups)
        ui.append([app,id1,[]])
        for id2,backup in enumerate(backups):
            ui[-1][-1].append([backup.time,id2])
    return ui,spl
def search(query,ui):
    return filter(lambda app: query in app[0],ui)
def copy(prop,dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    for file in prop.get_files():
        shutil.copy(file,os.path.join(dest,os.path.split(file)[-1]))
    return
def move(prop,serial = None):
    for file in prop.get_files():
        filename = os.path.split(file)
        push(file,'/sdcard/{tb}/{filename}'.format(tb = phone_dirs['titanium_backup'],filename = filename),serial)
if __name__ == "__main__":
    import time
    t1 =  time.time()
    parse_dir2()
    print(time.time()-t1)
    t2 = time.time()
    parse_dir()
    print(time.time()-t2)
