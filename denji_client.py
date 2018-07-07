#!/usr/bin/env python3

import os
import time
import serial
import requests
from network import scan

denji_ip = scan('backpack_pi') # scan network for denji IP
print('denji found on:', denji_ip)

def empty(denji_ip):
  pass


def denji(denji_ip):
    # url = "http://%s:5000/step" % denji_ip
    # headers = {
    #     'cache-control': "no-cache",
    #     'postman-token': "0c6e31b9-4742-bce4-6c15-726f72554ca5"
    # }
    # response = requests.request("GET", url, headers=headers)
    #print(response.text)
    print('denji')
    os.system('aplay default.wav')
    time.sleep(0.25)


def step(denji_ip):
    url = "http://%s:5000/step" % denji_ip
    headers = {
        'cache-control': "no-cache",
        'postman-token': "0c6e31b9-4742-bce4-6c15-726f72554ca5"
    }
    response = requests.request("GET", url, headers=headers)
    #print(response.text)
    print('step')
    os.system('aplay moving.wav')
    time.sleep(0.25)


def neutral(denji_ip):
    url = "http://%s:5000/neutral" % denji_ip
    headers = {
        'cache-control': "no-cache",
        'postman-token': "0c6e31b9-4742-bce4-6c15-726f72554ca5"
    }
    response = requests.request("GET", url, headers=headers)
    #print(response.text)
    print('neutral')
    os.system('aplay posture.wav')
    time.sleep(0.25)


def crouch(denji_ip):
    url = "http://%s:5000/crouch" % denji_ip
    headers = {
        'cache-control': "no-cache",
        'postman-token': "0c6e31b9-4742-bce4-6c15-726f72554ca5"
    }
    response = requests.request("GET", url, headers=headers)
    #print(response.text)
    print('crouch')
    os.system('aplay stabilizing.wav')
    time.sleep(0.25)


def taunt(denji_ip):
    url = "http://%s:5000/taunt" % denji_ip
    headers = {
        'cache-control': "no-cache",
        'postman-token': "0c6e31b9-4742-bce4-6c15-726f72554ca5"
    }
    response = requests.request("GET", url, headers=headers)
    #print(response.text)
    print('taunt')
    os.system('aplay kill.wav')
    time.sleep(0.25)


commands = {0:empty, 17:denji, 18:step, 19:neutral, 20:crouch, 21:taunt}

# serial settings
ser = serial.Serial(

    port='/dev/ttyUSB0',
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)
ser.flushInput()

# set speech module to waiting state then import group 1 and await voice input
# run twice to make sure it's in the correct mode
for i in range(2):
  ser.write(serial.to_bytes([0xAA]))
  time.sleep(0.5)
  ser.write(serial.to_bytes([0x21]))
  time.sleep(0.5)
print('init complete')

# read serial data and convert to integer
try:
  while True:
    line = ser.read()
    int_val = int.from_bytes(line, byteorder='big') # convert to integer
    print(int_val)
    commands[int_val](denji_ip)
except KeyboardInterrupt:
  print('Exiting Script')


