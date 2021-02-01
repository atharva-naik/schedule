import os
import re
import sys
import tty
import curses
import random
import termios
from time import sleep
from colors import color
from reprint import output
from local_manager.manager import *
from local_manager.exceptions import InvalidCommand
# from local_manager.models import 

INSTALL_PATH = os.getcwd()

def terminal():
    while True:
        cwd = os.getcwd()
        cwd = cwd.replace(os.getenv("HOME"),"~")

        try: 
            cmd=input(color("schd-terminal-mode:", fg='green', style='bold')+color(cwd, fg='blue', style='bold')+"$ ")
            cmd = cmd.strip()
        except EOFError:
            print("\nPlease exit using \"schd\" next time, not Ctrl+D ( ͡° ͜ʖ ͡°)")
            return 
        except KeyboardInterrupt:
            print("\nPlease exit using \"schd\" next time, not Ctrl+C ( ͡° ͜ʖ ͡°)")
            return

        if cmd == "schd":
            print(color("Exiting terminal mode, schd is much better anyways ;)", fg='red', style='bold'))
            break
        elif cmd.split()[0] == "cd":
            next_dir=" ".join(cmd.split()[1:])
            if next_dir == "": 
                next_dir=os.getenv("HOME")
            try:
                os.chdir(next_dir)
            except FileNotFoundError:
                print(color(f"schd: terminal: cd: {next_dir}: No such file or directory", fg='red'))
            cwd = os.getcwd()
        else:
            err=os.system(cmd)
            if err!=0:
                print(color("↑ check the error above — schd", fg='red'))

def wave_pride_flag():
    frames=[]
    css = ["#242551", "#406244", "#dab71f", "#d8832b", "#c94d4d"]
    stripes=["▐░▒▓▓▓▓▓▓▓▓▓▓▓▓▒░", "▐░▒▒▒▒▒▓▓▓▓▓▓▓▓▒░", "▐░▒▓▓▒▒▒▒▓▓▓▓▓▓▒░", "▐░▒▓▓▓▓▒▒▒▒▓▓▓▓▒░", "▐░▒▓▓▓▓▓▓▒▒▒▒▓▓▒░", "▐░▒▓▓▓▓▓▓▓▓▒▒▒▒▒░"]
    
    for i,stripe in enumerate(stripes):
        rainbow=[]
        for j,c in enumerate(css):
            rainbow.append(color(stripes[len(stripes)-1-(i+j)%len(stripes)], fg=c))
        frames.append(rainbow)

    with output(output_type="list", initial_len=5) as ol:
        for i in range(random.randint(4,8)):
            for i,frame in enumerate(frames):
                for j,_ in enumerate(frame):
                    ol[j]=frame[j]
                sleep(random.randint(1,2)*0.1)

def parse(cmd):
    cmd=cmd.strip()
    typ=cmd.split()[0]
    pred=" ".join(cmd.split()[1:])

    if cmd == "clear":
        os.system("clear")
    elif cmd == "terminal" or cmd == "tm":
        terminal()
        os.chdir(INSTALL_PATH)
    elif cmd == "pride" or cmd == "flag":
        wave_pride_flag()
    elif cmd == "python" or cmd == "py":
        print(color("staring python shell :)", fg='green', style='bold'))
        os.system("python")
    elif cmd == "ipython" or cmd == "ipy":
        print(color("staring interactive python shell :)", fg='green', style='bold'))
        os.system("ipython")
    elif typ == "ls" or typ == "list":
        os.system("ls")
    elif typ == "rm" or typ == "remove":
        if input(color(f"Are you sure about deleting \"{pred}\" ? Press 'y' to continue\n", fg='red')).lower() == 'y':
            os.system("rm " + pred)
        else:
            print(color("Operation cancelled by user", fg='yellow'))
    elif typ == "touch":
        os.system("touch " + pred)
    elif typ == "alert":
        flags = re.sub("\"[^\"]*\"", "", pred).strip()
        # parse()
        for message in re.findall("\"[^\"]*\"", pred):
            alert(message.replace("\"",""))
            time.sleep(1)
            pred.split()
            # alert(message)
    elif typ == "now" or typ == "date" or typ == "time": 
        print(color("TODAY:", fg='#fcba03', style='italic'))
        os.system("date")
    else:
        raise(InvalidCommand)

if __name__ == '__main__':
    for i in range(4*random.randint(1,2)):
        ellipsis_str='.'.join(["" for j in range(i%4+1)])+' '.join(["" for j in range(3-i%4+1)])
        print(color(f"STARTING! {ellipsis_str}", fg='green', style='bold'), end='\r')
        sleep(0.1*random.randint(1,3))  
    print()
    cmds=[""]

    while True:
        try:
            print(color(f"schd>", fg='#ff8e4d', style='bold'), end=" ")
            cmd=input()  
        except EOFError: 
            if input(color("\nSure about exiting? Enter y to exit\n", fg='red', style='bold')).lower()=="y":
                print(color("QUICK EXIT!", fg="red"), end='\r')
                sleep(0.3)
                break
        except KeyboardInterrupt:
            print(color("\nYou exited through an interrupt! Did I annoy you ? :(", fg='yellow', bg='#000', style='bold'))
            break

        if cmd == "exit":
            for i in range(4*random.randint(1,2)):
                
                ellipsis_str='.'.join(["" for j in range(i%4+1)])+' '.join(["" for j in range(3-i%4+1)])
                print(color(f"EXITING! {ellipsis_str}", fg='red', style='bold'), end='\r')
                sleep(0.1*random.randint(1,3))

            print()
            print(color("exited successfully !", fg='yellow', style='bold'), end='\r')
            sleep(0.5)
            break

        parse(cmd)
        cmds.append(cmd)