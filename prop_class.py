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
        for item in parsed.__parse__(prop_file).items():
            setattr(self,item[0],item[1])
    def __parse__(prop):
        ret = {'prop':prop}
        prop_file = open(prop)
        text = prop_file.read()
        prop_file.close()
        lines = filter(lambda line: line,text.split('\n'))
        next(lines)
        time = next(lines)
        
        ret['time'] = date_parser.parse(time[1:])
        next(lines)
        split = lambda line: line.split('=')
        make_tuple = lambda line: line if len(line) == 2 else [line[0],None]
        startwith_hash = lambda line: line[0] != '#'
        ret['raw'] = dict(
            map(
                make_tuple,
                map(
                    split,
                    filter(startwith_hash,lines)
                    )
                )
            )
        
        try:
            ret['name'] = ret['raw']['app_label'].lower()
        except KeyError:
            ret['name'] = ret['raw']['app_gui_label'].lower()
        ret['version'] = ret['raw']['app_version_name']
        return ret
    def get_files(self):
        md5 = self.raw['app_apk_md5']
        try:
            apk = next(filter(lambda file: md5 in file,os.listdir(self.backupdir)))
        except StopIteration:
            apk = None
        tar = os.path.split(self.prop.replace('.properties','.tar'))[-1]
        try:
            data = next(filter(lambda file: tar in file,os.listdir(self.backupdir)))
        except StopIteration:
            data = None
        return [os.path.join(self.backupdir,apk),self.prop,os.path.join(self.backupdir,data)]
if __name__ == '__main__':
    test = parsed(r"X:\Users\Ralphie\Android\TitaniumBackup\org.qpython.qpy3-20180211-052129.properties")
