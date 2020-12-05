import urllib.request
import huepy
import sys,time
import os
banner="""


                                   ____ ____ ____ ____
    )                             |   /|   /|   /|   /
 ( /( (    (    (          (  (   |  / |  / |  / |  / 
 )\()))(   )\ ) )\   (     )\))(  | /  | /  | /  | /  
(_))/(()\ (()/(((_)  )\ ) ((_))\  |/   |/   |/   |/   
| |_  ((_) )(_))(_) _(_/(  (()(_)(    (    (    (     
|  _|| '_|| || || || ' \))/ _` | )\   )\   )\   )\    
 \__||_|   \_, ||_||_||_| \__, |((_) ((_) ((_) ((_)   
           |__/           |___/                       


"""
def finder(banner):
    os.system('clear')
    print(banner)
    found=[]
    url=input('url>')
    if not url.endswith('/') :
        url=url+'/'
    #if not url.startswith('https://'):
     #  add_to_url='https://'+url#here i added https if the user forget to use it
      # print(add_to_url)
   # elif url.startswith('https://'):
    #    add_to_url=url#here if  the url start with https:// i del or removed added_to_url variable to keep it as the user entered
    try:
        curl=urllib.request.urlopen(url)
    except:

        sys.exit(huepy.bad('url not correct !'))
    wlist = input(huepy.info('wordlist>'))
    try:
        op=open(wlist,'r')
    except:
        print(huepy.bad('file not found !'))
        sys.exit()
    for i in op.readlines():
        i=i.rstrip()
       # print(huepy.run(' trying ... :{}'.format(url+i)))
        try:
            url2=urllib.request.urlopen(url+i)
            
            if url2:
                print(huepy.good(time.ctime().split(' ')[3]+'   : '+'{} '.format(url+i)))
                found.append(i)
        except:
            print(huepy.bad(time.ctime().split(' ')[3]+'   : '+'{}'.format(url+i)))
    if len(found)>0:
       print('#'*60+'this pages found =>>>>',found,'#'*60)
finder(banner)
