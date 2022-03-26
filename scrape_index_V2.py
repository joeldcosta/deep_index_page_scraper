import requests
import re
import os
import time
from time import strftime
import urllib.parse



d = time.strftime("%d") # 06
m = time.strftime("%m") # 01
H = time.strftime("%H") # 10
M = time.strftime("%M") # 33
S = time.strftime("%S") # 06
Y = time.strftime("%Y") # 2020

try:
   file = open("path.txt",'r')
   data = file.readlines()
   print("SCRAPING...")
   for i in data:
      m_url = str(i.replace('\n',''))
      ###############################################     
      website = requests.get(m_url)
      html = website.text

      #url = "http://"+str(m_url.split('/')[2])
      #url = str(website.url)
      #url = str(website.url)[:-1]

      host0 = str(m_url.split('/')[:3][0])
      host2 = str(m_url.split('/')[:3][2])
      host = host0+"//"+host2
      path = m_url.replace(host,'')

      #url = host+path[:-1]
      url = host+path
      
      f = open(H+M+S+d+m+Y+"_scrapped_data.csv", "a+")
      #mp4
      mp4 = re.findall('href="(.*mp4)"', html)
      #avi
      avi = re.findall('href="(.*avi)"', html)
      #mkv
      mkv = re.findall('href="(.*mkv)"', html)
      #flv
      flv = re.findall('href="(.*flv)"', html)
      #pdf
      pdf = re.findall('href="(.*pdf)"', html)

      for infile in sorted(x for x in (mp4)):
         f.write(url + urllib.parse.quote_plus(infile)+'\n')
         f.flush()
      for infile in sorted(x for x in (avi)):
         f.write(url + urllib.parse.quote_plus(infile)+'\n')
         f.flush()
      for infile in sorted(x for x in (mkv)):
         f.write(url + urllib.parse.quote_plus(infile)+'\n')
         f.flush()
      for infile in sorted(x for x in (flv)):
         f.write(url + urllib.parse.quote_plus(infile)+'\n')
         f.flush()
      for infile in sorted(x for x in (pdf)):
         f.write(url + urllib.parse.quote_plus(infile)+'\n')
         f.flush()
      f.close()
      ###############################################

      p = open("path_.txt", "a+")
      #path
      folder = re.findall('href="(.*/)"', html)
      for infile in sorted(x for x in (folder)):
         if "/" != infile[0]:
            if "../" not in infile:
               p.write(url + infile+'\n')
               p.flush()
	
         #print(url+infile)
         #if "../" not in infile:
         #   p.write(url + infile+'\n')
         #   p.flush()
            
         #if "/" != infile[0]:
         #   if "../" not in infile:
         #      p.write(url + infile+'\n')
         #      p.flush()
         
               
      p.close()
      ###############################################
   file.close()

   # REMOVE DUPLICATES #############################################################
   import fileinput
   seen = set() # set for fast O(1) amortized lookup
   for line in fileinput.FileInput("path_.txt", inplace=1):
        if line in seen: continue # skip duplicate
        seen.add(line)
        print (line.replace('\n','')) # standard output is now redirected to the file
   #################################################################################
        

   #Remove previous link###############################################
   infile = "path.txt" # GIVE ME BOUNCE
   with open(infile,'r') as b:
      bounce = b.readlines()
        
   with open("path_.txt",'r') as e: # GIVE ME STUFF TO CLEAN
      emails = e.readlines()

   list_ = [x for x in emails if x not in bounce]
   for i in list_:
      #print(i.strip())
      with open("_path_.txt",'+a') as clean: # CLEAN FILE
         clean.writelines(i.strip()+'\n')
   ######################################################################



   # REMOVE DUPLICATES #############################################################
   import fileinput
   seen = set() # set for fast O(1) amortized lookup
   for line in fileinput.FileInput("_path_.txt", inplace=1):
        if line in seen: continue # skip duplicate
        seen.add(line)
        print (line.replace('\n','')) # standard output is now redirected to the file
   #################################################################################


             
   #delete file
   if os.path.exists("path.txt"):
      os.remove("path.txt")
   if os.path.exists("path_.txt"):
      os.remove("path_.txt")
      #rename file  
      os.rename('_path_.txt','path.txt')
 
#except:
#   file = open("NOTE.txt",'w')
#   file.write('################################\nCOPY PASTE YOUR INDEX URL IN PATH FILE\n################################\nNo path file.\nCreating path file.\nKindly Enter index URL\ne.g.\n\nintext:sex ext:jpg | mp4 -rape intitle:"index of"\nintext:JAV ext:jpg | mp4 -rape intitle:"index of"\n:::Search in Google:::')
#   print('No path file.\nCreating path file.\nKindly Enter index URL\ne.g.\n\nintext:sex ext:jpg | mp4 -rape intitle:"index of"\nintext:JAV ext:jpg | mp4 -rape intitle:"index of"\n:::Search in Google:::')

except Exception as e:
   print(e)
