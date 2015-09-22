#!/usr/bin/env python2.7
import socket
import subprocess
import sys
import os
from datetime import datetime

OKGREEN = '\033[92m'
FAIL = '\033[91m'
ENDC = '\033[0m'

def portScan(remoteServerIP, startPort, endPort):

    # Print a nice banner with information on which host we are about to scan
    print "-" * 60
    print "Please wait, scanning remote host", remoteServerIP
    print "-" * 60

    # Check what time the scan started
    t1 = datetime.now()

    try:
        for port in range(int(startPort),int(endPort)):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print "Port "+OKGREEN+"{}: \t Open".format(port) + ENDC
            # else:
            #     print "Port {}: \t Closed".format(port)
            sock.close()

    except KeyboardInterrupt:
        print "You pressed Ctrl+C"
        sys.exit()

    except socket.gaierror:
        print 'Hostname could not be resolved. Exiting'
        sys.exit()

    except socket.error:
        print "Couldn't connect to server"
        sys.exit()

    t2 = datetime.now()

    total =  t2 - t1

    print 'Scanning Completed in: ', total

# Takes in a start IP and an end IP and returns a list of all IP's in the range
def ipRange(start_ip, end_ip):
    # check that start_ip < end_ip
   if map(int, start_ip.split('.')) < map(int, end_ip.split('.')):
       start = list(map(int, start_ip.split(".")))
       end = list(map(int, end_ip.split(".")))
       temp = start
       ip_range = []

       ip_range.append(start_ip)
       while temp != end:
          start[3] += 1
          for i in (3, 2, 1):
             if temp[i] == 256:
                temp[i] = 0
                temp[i-1] += 1
          ip_range.append(".".join(map(str, temp)))
   else:
       print(FAIL+"ERROR: "+ENDC+"First IP must be smaller than last IP")
       print_menu()
       sys.exit()

   return ip_range

# Prints the menu
def print_menu():
    print("Usage: portscan -s [IP_address] [start_port] [end_port]")
    print("       portscan -m [start_IP_address] [end_IP_address] [start_port] [end_port]")
    print("Args:")
    print(" "*4+" -s: indicates single IP mode. ")
    print(" "*4+" -m: indicates multiple IP mode")

if __name__== "__main__":
    try:
        # receive argument that indicates single or multiple IP mode
        arg = sys.argv[1]

        firstIP = socket.gethostbyname(sys.argv[2])

        # single mode IP
        if arg == "-s":
            startPort = sys.argv[3]
            endPort = sys.argv[4]
            # Clear the screen
            subprocess.call('clear', shell=True)
            portScan(firstIP, startPort, endPort)

        # multiple mode IP
        elif arg == "-m":
            secondIP = socket.gethostbyname(sys.argv[3])
            startPort = sys.argv[4]
            endPort = sys.argv[5]
            all_ip = ipRange(firstIP,secondIP)

            # iterate through all IP's
            for single_ip in all_ip:
                portScan(single_ip, startPort, endPort)
        else:
            print(FAIL+"ERROR: "+ENDC+"Invalid argument!")
            print_menu();

    except (IndexError):
        print_menu();
