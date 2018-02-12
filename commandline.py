import cmd
import os
import sys
from utils import *
##from multiprocessing import Pool
if __name__ == "__main__":
    apps = parse_dir()
    ui,applist = enum(apps)
    class tbinterface(cmd.Cmd):
        intro = 'Titanium Backup Shell'
        prompt = ':'
        file = None
            
        def do_list(self,arg):
            
            '''
    list default: lists all apps and ids
    list with string: searches for app
    list with number: lists backups
            '''
            if not arg:
                print('\n'.join(map(lambda app: '{1}. {0}'.format(*app),ui)))
            else:
                try:
                    arg = int(arg)
                    print(
                        '\n'.join(
                            map(
                                lambda trouble: '{}. {:<41} || ver={}'.format(
                                    trouble[1][1],
                                    trouble[1][0].strftime("%A, %B %e, %Y %H:%M:%S"),
                                    applist[arg][trouble[0]].version
                                    ),
                                enumerate(ui[arg][-1])
                                )
                            )
                        )
                except ValueError:
                    print(
                        '\n'.join(
                            map(
                                lambda result: '{1} {0}'.format(*result),search(arg,ui)
                                )
                            )
                        )
                


        def do_copy(self,args):
            '''
    copy app_id backup_id [dest]

    (default destination is the current working directory)
            '''
            args = args.split(' ')

            try:
                id1 = int(args[0])
                id2 = int(args[1])
                if len(args) > 2:
                    dest = os.path.expandvars(args[2])
                else:
                    dest = os.getcwd()
                copy(applist[id1][id2],dest)
            except ValueError:
                self.do_help('copy')
        def do_move(self,args):
            '''
    move app_id backup_id [serial]

    (moves to titanium backup folder on phone serial serial)
            '''
            args = args.split(' ')

            try:
                id1 = int(args[0])
                id2 = int(args[1])

                serial = None
                if len(args) == 3:
                    serial = args[2]

                move(applist[id1][id2],serial)
            except ValueError:
                self.do_help('move')
            
        def do_exit(self,arg):
            
            '''
    exit function
            '''
            return True
    def tbkp():
        tbinterface().cmdloop()
    tbkp()
