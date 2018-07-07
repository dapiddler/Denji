#!/usr/bin/env python

import time
import requests
import curses
import curses.textpad
from network import scan

denji_ip = scan('backpack_pi') #scan network for denji IP
print('denji found on:', denji_ip)


def step_forward(denji_ip):
    url = "http://%s:5000/step" % denji_ip
    headers = {
        'cache-control': "no-cache",
        'postman-token': "0c6e31b9-4742-bce4-6c15-726f72554ca5"
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)


def crouch(denji_ip):
    url = "http://%s:5000/crouch" % denji_ip
    headers = {
        'cache-control': "no-cache",
        'postman-token': "0c6e31b9-4742-bce4-6c15-726f72554ca5"
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)



def neutral(denji_ip):
    url = "http://%s:5000/neutral" % denji_ip
    headers = {
        'cache-control': "no-cache",
        'postman-token': "0c6e31b9-4742-bce4-6c15-726f72554ca5"
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)


def taunt(denji_ip):
    url = "http://%s:5000/taunt" % denji_ip
    headers = {
        'cache-control': "no-cache",
        'postman-token': "0c6e31b9-4742-bce4-6c15-726f72554ca5"
    }
    response = requests.request("GET", url, headers=headers)
    print(response.text)


if __name__ == "__main__":
    stdscr = curses.initscr()

    curses.noecho()
    try:
        while 1:
            c = stdscr.getch()
            if c == ord('w'):
                step_forward(denji_ip)
                time.sleep(5)
            elif c == ord('s'):
                neutral(denji_ip)
                time.sleep(1)
            elif c == ord('c'):
                crouch(denji_ip)
                time.sleep(1)
            elif c == ord('t'):
                taunt(denji_ip)
                time.sleep(1)
            elif c == ord('q'):
                curses.endwin()
                break
    except KeyboardInterrupt:
        curses.endwin()
