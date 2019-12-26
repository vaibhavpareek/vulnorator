import terminal_banner,pyfiglet,webbrowser,time
from func_def import *
from os import system
from googlesearch import search
def sleep():
	time.sleep(5)
def clr():
	system("clear")
def cont():
	i = input("[+] Press Any Key to Continue ")
def metasploit():
	print("....Enter `quit` to exit the metasploit")
	print("[+]To Use Exploit         : use <exploit name>")
	print("[+]To See Requirements    : show options")
	print("[+]To Set the environment : set RHOSTS <target IP>")
	print("[+]To See Payload         : show payloads")
	print("[+]To Use the payload     : set PAYLOAD <payload name>")
	print("[+]To Exploit             : exploit or run")
					
def info_gather():
	ascii_banner = pyfiglet.figlet_format("!Information Gathering",font="slant")
	print(ascii_banner)
	print("\t\t\t\tLet's Recon !! \n");
	print("\t\t1.  Web Crawler\n")
	print("\t\t2.  Whois Information\n")	
	print("\t\t3.  Subdomains Analysis\n")
	print("\t\t4.  Instagram Crawler\n")
	print("\t\t5.  DNS Lookup \n")
	print("\t\t6.  Nmap Scan\n")
	print("\t\t7.  Traceroute Scan\n")
	print("\t\t8.  DNS STuff Analysis\n")	
	print("\t\t9.  Shodan Reconnasiance\n")
	print("\t\t10. Reconnasiance website View\n")	
	print("\t\t11. Download Guides for Reconnasiance\n")				
	print("\t\t12. Go Back\n")
	ch = int(input("\t\t\t>>HACKING : "))
	return ch	
def show():
	print("\t\t\t\tSharp your tools before hunting !! \n");
	print("\t\t1. Footprinting ----------- |\n")
	print("\t\t\t\t| ------------  2. Scanning\n")
	print("\t\t3. Enumeration ----------- |\n")
	print("\t\t\t\t| ------------  4. Threat Rator\n")
	print("\t\t5. Vulnerabilties ----------- |\n")
	print("\t\t\t\t| ------------  6. About Vulnorator \n")
	print("\t\t7. End Up Hacking----------- |\n")
def enumeration():
	ascii_banner = pyfiglet.figlet_format("!Enumeration",font="slant")
	print(ascii_banner)
	print("\t\t\t\tLet's Exploit !! \n");
	print("\t\t1. Search the exploit\n")
	print("\t\t2. Metasploit\n")
	print("\t\t3. SqlMap\n")
	print("\t\t4. How to Exploit\n")
	print("\t\t5. Go Back\n")
def sqlmap():
	print("\t\t\t\tSequence Should be followed to get fruitful results... !! \n");
	print("\t\t1. List Databases\n")
	print("\t\t2. List Tables of DB\n")
	print("\t\t3. List Columns of Table of particular DB\n")
	print("\t\t4. Dump the Database\n")
	print("\t\t5. Go Back\n")	
def menu():
	print("\033[1;34;48m* LINUX BASED TOOL V1.0 \033[1;32;48mDeveloped By @Vaibhav Pareek\033[1;31;48m")
	print("\033[1;34;48m* Website of Vulnorator :\033[1;32;48m http://vulnorator.ml/\033[1;31;48m")
	ascii_banner = pyfiglet.figlet_format("!Vulnorator!",font="slant")
	print(ascii_banner)
	print("\033[1;32;48m")
	banner_text = "\n\033[1;32;48m[+] It is a linux based tool,Specially designed for begineers to learn about various existing vulnerabilies.\n[+] It can be used to know the criticality of each vulnerability.\n[+] It also perform reconnasiance and scanning by itself for you.\n[+] Threat meter will show you the vulnerabilities that you should find in the domain as per their threat level.\n[+] Best Information is present to understand deeply about each vulnerability by availabe resources."
	my_banner = terminal_banner.Banner(banner_text)
	print(my_banner)
	print("\033[1;34;48m")
	show()
	