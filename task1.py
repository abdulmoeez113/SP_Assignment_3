import requests
from PIL import Image
from bs4 import BeautifulSoup
from StringIO import StringIO
import os
import sys
import time

def Qari_Shbs_Names(URL):
	r = requests.get(URL)
	name = []
	
	if r.status_code == 200:
		parser_obj = BeautifulSoup(r.content, "html.parser")
		anchor_tags = parser_obj.find_all("a")
		
		for n in anchor_tags:
			name.append(n.text)
	return name

def makeDir(dirr):
    try:
        if not os.path.exists(dirr):
            os.makedirs(dirr)
    except OSError:
        print ('Error in Creating this ' +  dirr)


count=1
proCount=0
url1='https://download.quranicaudio.com/quran/'
Qari_Names = Qari_Shbs_Names(url1)

total=len(Qari_Names)
file = open("file","w+")

st = str(time.strftime("%c"))+" "+"Total number of Qari's : "+str(total)
file.write(st)
file.write("\n")

for Qari in Qari_Names:
	if count==1:
		count=count+1
		continue

	makeDir(Qari)
	os.chdir(Qari)
	url2=url1+Qari
	print(url2)
	file_list = Qari_Shbs_Names(url2)
	proCount=proCount+1

	st=str(time.strftime("%c"))+" "+"PROCESSING : "+str(proCount)+"out of "+str(total)
	file.write(st)
	file.write("\n")

	st=str(time.strftime("%c"))+" "+"QARI NAME : "+str(Qari)
	file.write(st)
	file.write("\n")	

	for filee in file_list[-26:]:

		url3=url2+filee
		print(url3)

		st=str(time.strftime("%c"))+" "+"QARI NAME : "+str(Qari)+" "+"FILENAME : "+str(filee)+"START"
		file.write(st)
		file.write("\n")

		r=requests.get(url3)
		with open(filee,"web") as code:
			code.write(r.content)
	
		st=str(time.strftime("%c"))+" "+"QARI NAME : "+str(Qari)+" "+"FILENAME : "+str(filee)+"END"
		file.write(st)
		file.write("\n")

	st=str(time.strftime("%c"))+" "+"Merge FILE of qaris names : "+str(Qari)+" "+"START"
	file.write(st)
	file.write("\n")
			
	os.system("mp3wrap MERGED.mp3 *.mp3")
			
	st=str(time.strftime("%c"))+" "+"Merge FILE of qaris names : "+str(Qari)+" "+"END"
	file.write(st)
	file.write("\n")

	os.chdir("../")