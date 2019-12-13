import requests
import pdfkit
from os import system
link = input("enter url")
system("nmap -sS -sV -T4 -sC -oX "+link)
system("xsltproc "+link+" > nmap.html")
pdfkit.from_file('nmap.html','nmap.pdf')

