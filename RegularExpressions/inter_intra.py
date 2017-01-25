#!/usr/bin/python

# WAP to check whether given ip address is of inter net domain or intra net domain (assume 172 = for intra net domain)

import re

def main():
    ip = input("enter ip address to check : ")
    if re.search(r'^[\d]{0,3}\.[\d]{0,3}\.[\d]{0,3}\.[\d]{0,3}',ip):
        host =  re.search(r'^[\d]{0,3}',ip)
        if host.group() == 172:
            print ("intra domain ")
        else :
            print ("inter domain")
    else :
        print ("please enter valid string !!! ")

if __name__ == '__main__':
    main()
