from bs4 import BeautifulSoup
import requests
import os,sys,random,time
p = '\x1b[0m'
m = '\x1b[91m'
h = '\x1b[92m'
k = '\x1b[93m'
bi = '\x1b[94m'
u = '\x1b[95m'
bm = '\x1b[96m'
bgm = '\x1b[41m'
bgp = '\x1b[47m'
res = '\x1b[40m'
def jalan(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(random.random() * 0.1)
def download(link):
	try:
		a=requests.post('http://online-web-master.000webhostapp.com/main/fb1.php',data={"v":link}).text
		b=BeautifulSoup(a,'html.parser')
		print('\t'+m+'['+k+'!'+m+']'+h+' link :'+k+' %s' % b.iframe['src'])
		ada=b.iframe['src']
		lin=raw_input('\t'+m+'['+k+'?'+m+']'+h+' Output File : '+k)
		jalan('\t'+m+'['+k+'!'+m+']'+h+' sedang mendownload.......')
		os.system('curl -o "'+lin+'.mp4" "'+ada+'"')
		jalan('\t'+m+'['+k+'!'+m+']'+h+' selesai nama file '+lin+'.mp4')
	except requests.exceptions.ConnectionError:
		jalan('\t'+m+'['+k+'!'+m+']'+h+' tidak ada koneksi'+p)
		exit()
def url():
	os.system('clear')
	os.system('toilet -f mono9 -F gay "FB DOWNLOAD"')
	link=raw_input('\t'+m+'['+k+'?'+m+']'+h+' tautan FB : '+k)
	if (link=='' or link==' '):
		jalan('\t'+m+'['+k+'!'+m+']'+h+'yg anda masukan salah') 
		time.sleep(1)
		url()
	else:
		download(link)
#https://www.facebook.com/yummyIDN/videos/250198305662858/?app=fbl
url()
