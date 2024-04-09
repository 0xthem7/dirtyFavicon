import mmh3
import requests
import codecs
import sys
import os
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

banner = '''
              \||/
                |  @___oo
      /\  /\   / (__,,,,|
     ) /^\) ^\/ _)
     )   /^\/   _)        dirtyFavicon       
     )   _ /  / _)        author : 0xtheM7
 /\  )/\/ ||  | )_)       version : 0.1
 <  >      |(,,) )__)  
 ||      /    \)___)\ 
 | \____(      )___) )___  
  \______(_______;;; __;;; 
    '''


print(banner)
URL = sys.argv[1]
HOST = URL.split('/')[2]
response = requests.get(f'{URL}')
favicon = codecs.encode(response.content,"base64")
hash = str(mmh3.hash(favicon))
faviconHash = hash.split('-')[1]
print(f'{Fore.GREEN}[{Fore.YELLOW}+{Fore.GREEN}] Host Name : {Fore.YELLOW}{HOST}{Style.RESET_ALL}')
print(f'{Fore.GREEN}[{Fore.YELLOW}+{Fore.GREEN}] Favicon Hash : {Fore.YELLOW}{faviconHash}{Style.RESET_ALL}')
print(f'{Fore.GREEN}[{Fore.YELLOW}-{Fore.GREEN}] Shodan Dork: {Fore.YELLOW}http.favicon.hash:{faviconHash}{Style.RESET_ALL}')
### WORK IN PROGRESS 
#os.system(f'shodan search org:"REDACTED" http.favicon.hash:{faviconHash} --fields ip_str,port --separator " " | awk \'{{print $1":"$2}}\'')
