import os

from dateutil import parser as date_parser
backupdir = r"X:\Users\Ralphie\Android\TitaniumBackup"

class parsed:
    def __init__(self,prop_file,backupdir = None):
        if "com.keramidas.virtual" in prop_file:
            raise TypeError(''''This file isn't for apps''')
        if backupdir:
            self.backupdir = backupdir
        else:
            self.backupdir = os.path.dirname(prop_file)
        self.name,self.time,self.filename,self.version,self.raw = parsed.__parse__(prop_file)
    def __parse__(prop):

        prop_file = open(prop)
        text = prop_file.read()
        prop_file.close()
        lines = list(filter(lambda line: line,text.split('\n')))
        time = date_parser.parse(lines[1][1:])
        raw = {}
        for line in lines[2:]:
            if line[0] != '#':
                line = line.split('=')
                if len(line) == 2:
                    raw[line[0]] = line[1]
                else:
                    raw[line[0]] = ''
        try:
            identity = raw['app_label'].lower()
        except KeyError:
            identity = raw['app_gui_label'].lower()
        version = raw['app_version_name']
        return (
            identity,
            time,
            prop,
            version,
            raw,
            )

    def get_files(self):
        md5 = self.raw['app_apk_md5']
        try:
            apk = next(filter(lambda file: md5 in file,os.listdir(self.backupdir)))
        except StopIteration:
            apk = None
        tar = os.path.split(self.filename.replace('.properties','.tar'))[-1]
        try:
            data = next(filter(lambda file: tar in file,os.listdir(self.backupdir)))
        except StopIteration:
            data = None
        return (
            os.path.join(self.backupdir,apk),
            self.filename,
            os.path.join(self.backupdir,data),
            )
            
