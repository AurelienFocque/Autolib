import requests
import re
import os
import codecs
import sys
import hashlib
try:
  sys.argv[1]
  sys.argv[2]
except:
  print ("Usage : arg1=username, arg2=password")
  exit(0)
s=requests.Session()
url="https://moncompte.autolib.eu/account/login/"
r=s.get("https://moncompte.autolib.eu/account/login/")
csrfmiddlewaretoken=r.text.split("name='csrfmiddlewaretoken' value='")[1].split("' />")[0]
urlpost="https://moncompte.autolib.eu/account/login/"
print("csrfmiddlewaretoken : " +csrfmiddlewaretoken)
data={"csrfmiddlewaretoken":csrfmiddlewaretoken,"username":sys.argv[1],"password":sys.argv[2],"action":"Se connecter"}
headers={"Referer":"https://moncompte.autolib.eu/account/login/?","User-Agent":"Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0"}
r=s.post(urlpost,data=data,headers=headers)
if("Erreurs rencontr" in r.text):
  print("erreur d'authentification")
  exit(0)
r=s.get('https://moncompte.autolib.eu/account/bills/')
tmp=re.findall("/account/bill/[0-9]*/", r.text)
pdflisturl=["https://moncompte.autolib.eu"+x for x in tmp]
print("Nombre de facture : ")
print(len(pdflisturl))
directory=os.getcwd()+"/factures/"
print("ecriture dans : "+directory)
if not os.path.exists(directory):
    os.makedirs(directory)
for k,pdfurl in enumerate (pdflisturl,0):
  r=s.get(pdfurl)
  print(len(r.text))
  with codecs.open(directory+"facture"+str(k)+".pdf", "wb") as f:
    f.write(r.content)
    f.close()
