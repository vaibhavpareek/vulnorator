from os import system
import pdfkit
link = input("enter : ")
system("nmap -v -p 1-1000 -sV -O -sS -T4 "+link+" -oX OUTPUT/Info_gathering/nmapreport"+ ".xml")
system("xsltproc "+link+" > nmap.html")
pdfkit.from_file('nmap.html','nmap.pdf')
print("[+ Saved] NMAP Scan RECORDS ARE SAVED  : OUTPUT/"+"/Info_gathering/nmap.pdf")
