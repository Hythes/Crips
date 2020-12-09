#!/usr/bin/env python2.7
#
#
#

import os
import sys
d3 = os.system("curl http://ipinfo.io/ip")
os.system("clear && clear && clear")
logo = "Menu : "
menu = '''\033[0m
    {1}--Whois lookup
    {2}--Traceroute
    {3}--DNS Lookup
    {4}--Reverse DNS Lookup
    {5}--GeoIP Lookup
    {6}--Port Scan
    {7}--Reverse IP Lookup
    {99}-Exit
 '''
print logo
print menu


def quit():
    con = raw_input('Continue [Y/n] -> ')
    if con[0].upper() == 'N':
        exit()
    else:
        os.system("clear")
        print logo
        print menu
        select()


def select():
    try:
        choice = input("Crips~# ")
        if choice == 1:
            rot = raw_input('Use list.txt? (y/n) ')
            os.system("clear")
            print("""
 _       ____  ______  _________
| |     / / / / / __ \/  _/ ___/
| | /| / / /_/ / / / // / \__ \
| |/ |/ / __  / /_/ _/ / ___/ /
|__/|__/_/ /_/\____/___//____/
      """)
            if (rot == "y"):
                f = open("list.txt", "r")
                for d3 in f:
                    os.system("curl http://api.hackertarget.com/whois/?q=" + d3)
            else:
                d3 = raw_input('Enter IP Or Domain : ')
                os.system("curl http://api.hackertarget.com/whois/?q=" + d3)
            print("")
            quit()
        elif choice == 0:
            os.system("clear")
            print("This tool is only available for Linux and similar systems  ")
            os.system("git clone https://github.com/Manisso/Crips.git")
            os.system("cd Crips && sudo bash ./update.sh")
            os.system("crips")
        elif choice == 2:
            d3 = raw_input('Enter IP Or Domain : ')
            os.system("clear")
            print("""
 ____ ____   __   ___ ____ ____ _____ __  __ ____ ____
(_  _(  _ \ /__\ / __( ___(  _ (  _  (  )(  (_  _( ___)
  )(  )   //(__)( (__ )__) )   /)(_)( )(__)(  )(  )__)
 (__)(_)\_(__)(__\___(____(_)\_(_____(______)(__)(____)
""")
            os.system("curl https://api.hackertarget.com/mtr/?q=" + d3)
            print("")
            quit()
        elif choice == 3:
            os.system("clear")
            print("DNS Lookup")
            rot = raw_input('Use link.txt? (y/n) ')
            if (rot == "y"):
                f = open("list.txt", "r")
                for d3 in f:
                    os.system(
                        "curl http://api.hackertarget.com/dnslookup/?q=" + d3)
                    print("\n")
            else:
                d3 = raw_input('Enter IP Or Domain : ')
                os.system(
                    "curl http://api.hackertarget.com/dnslookup/?q=" + d3)
            print("")
            quit()
        elif choice == 0:
            print "Bye Bye"
            os.system("clear")
            exit()
        elif choice == 4:
            d3 = raw_input('Enter IP Address - IP Range Or Domain  : ')
            os.system("clear")
            print("""
 _____                            ____  _____ _____
| __  |___ _ _ ___ ___ ___ ___   |    \|   | |   __|
|    -| -_| | | -_|  _|_ -| -_|  |  |  | | | |__   |
|__|__|___|\_/|___|_| |___|___|  |____/|_|___|_____|

	  """)
            os.system("curl https://api.hackertarget.com/reversedns/?q=" + d3)
            print("")
            quit()
        elif choice == 5:
            d3 = raw_input('Enter IP Or Domain : ')
            os.system("clear")
            print("""
   _____           _____ _____
  / ____|         |_   _|  __ \
 | |  __  ___  ___  | | | |__) |
 | | |_ |/ _ \/ _ \ | | |  ___/
 | |__| |  __| (_) _| |_| |
  \_____|\___|\___|_____|_|

	""")
            os.system("curl http://api.hackertarget.com/geoip/?q=" + d3)
            print("")
            print("")
            quit()
        elif choice == 6:
            rot = raw_input('Use link.txt? (y/n) ')
            os.system("clear")
            print("""
     __                         __
  /\ \ \_ __ ___   __ _ _ __   / _\ ___ __ _ _ __
 /  \/ | '_ ` _ \ / _` | '_ \  \ \ / __/ _` | '_ \
/ /\  /| | | | | | (_| | |_) | _\ | (_| (_| | | | |
\_\ \/ |_| |_| |_|\__,_| .__/  \__/\___\__,_|_| |_|
                       |_|
      """)
            print("")
            quit()
        elif choice == 7:
            rot = raw_input('Use link.txt? (y/n) ')
            print "IP Lookup"
            if (rot == "y"):
                f = open("list.txt", "r")
                for d3 in f:
                  os.system("wget http://api.hackertarget.com/reverseiplookup/?q=" + d3)
                  os.system("curl http://api.hackertarget.com/reverseiplookup/?q=" + d3)
                  print("")
                  print("\033[91m\033[1mFile Saved On : ")
                  os.system("pwd")
                  print("File : index.html?q=" + d3)
                  print("\033[0m")
            else:
                d3 = raw_input('Enter IP Or Domain : ')
                print "IP lookup"
                os.system(
                    "wget http://api.hackertarget.com/reverseiplookup/?q=" + d3)
                os.system("clear")
                os.system(
                    "curl http://api.hackertarget.com/reverseiplookup/?q=" + d3)
                print("")
                print("\033[91m\033[1mFile Saved On : ")
                os.system("pwd")
                print("File : index.html?q=" + d3)
                print("\033[0m")

            quit()
    except(KeyboardInterrupt):
        print ""


select()
