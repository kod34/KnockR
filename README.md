
<h1 align="center">KnockR</h1>

<p align="center"> KnockR is a python program that uses web page css_selectors to carry out a dictionary attack against provided usernames.  
    <br> 
</p>

## 📝 Table of Contents

- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)

## 🏁 Getting Started <a name = "getting_started"></a>

### Prerequisites


```
Chrome
ChromeDriver
Python
Linux
```

### Installing

```
git clone https://github.com/kod34/KnockR
cd KnockR
chmod +x install.sh
./install.sh
```


## 🎈 Usage <a name="usage"></a>

```
knockr [-h] [-p PASSWORD_SELECTOR] [-l USERNAME_SELECTOR]
                 [-b LOGIN_BUTTON_SELECTOR] [-d DELAY] -s URL -u USERNAME -w
                 WORDLIST -c CHROMEDRIVER

optional arguments:
  -h, --help            show this help message and exit
  -p PASSWORD_SELECTOR, --pasel PASSWORD_SELECTOR
                        Specify the password selector
  -l USERNAME_SELECTOR, --usrsel USERNAME_SELECTOR
                        Specify the username selector
  -b LOGIN_BUTTON_SELECTOR, --buttonsel LOGIN_BUTTON_SELECTOR
                        Specify the login button selector
  -d DELAY, --delay DELAY
                        Specify a delay

required named arguments:
  -s URL, --url URL     Specify a url
  -u USERNAME, --username USERNAME
                        Specify the username
  -w WORDLIST, --wordlist WORDLIST
                        Specify the password list directory
  -c CHROMEDRIVER, --chromedriver CHROMEDRIVER
                        Specify the path to chrome driver

```

### Examples
```
knockr -s http://example.com -u admin -w wordlist_sample.txt -c ./chromedriver
```

## ⛏️ Built Using <a name = "built_using"></a>

- Python

## ✍️ Authors <a name = "authors"></a>

- [@kod34](https://github.com/kod34)

## ⚠️ Disclaimer
The sole purpose of writing this program was research, its misuse is the responsibility of the user only.