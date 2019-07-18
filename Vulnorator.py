import terminal_banner
import pyfiglet
from os import system
import webbrowser
from googlesearch import search
import time
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
while(True):
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
	ch = int(input("\t\t\t>>HACKING : "))
	if(ch==1):
		system("clear")
		print(ascii_banner)
		print("\033[1;35;48m\nIMPORTANT :: \n[+] Just Provide the URL or IP address of the target.it will open related tabs in your browser for information gathering.\n[+] Start reading content from websites opened in the browser to get best information regarding target.\n[+]It will store the whois and traceroute information in the files whois.txt and traceroute.txt respectively.\n[+] For backup all the important links are stored in a file which is saved in OUTPUT/[WEBSITE]/footprinting.txt.")
		que = input("\n\t\t\t\tURL or KEYWORD : ")
		query = "inurl:"+que
		system("mkdir OUTPUT/"+str(que))
		system("mkdir OUTPUT/"+str(que)+"/Info_gathering")
		file = open('OUTPUT/'+str(que)+'/Info_gathering/footprinting.txt','a')
		print("\033[1;35;48m\n[PASSIVE INFORMATION GATHERING]..........\n")
		for j in search(query, tld="co.in", num=10, stop=10, pause=2):
			print("[+ Opening]  "+str(j)+"\n")
			file.write(str(j))
			webbrowser.open(j)
		print("[ACTIVE INFORMATION GATHERING]..........\n")
		file.write("http://web.archive.org/")
		webbrowser.open("http://web.archive.org/")
		print("[+ Opening] Screenshots of websites : "+str("http://web.archive.org/")+"\n")
		file.write("https://www.shodan.io/search?query="+str(que))
		webbrowser.open("https://www.shodan.io/search?query="+str(que))
		print("[+ Opening] Shodan Information about the target : "+str("https://www.shodan.io/search?query="+str(que))+"\n")
		file.write("https://osintframework.com/")
		webbrowser.open("https://osintframework.com/")
		print("[+ Opening] OSINT Framework : "+str("https://osintframework.com/")+"\n")
		file.write("https://www.exploit-db.com/google-hacking-database")
		webbrowser.open("https://www.exploit-db.com/google-hacking-database")
		print("[+ Opening] ExploitDB(GHDB) : "+str("https://www.exploit-db.com/google-hacking-database")+"\n")
		file.write("https://tools.dnsstuff.com/#dnsReport|type=domain&&value="+str(que))
		webbrowser.open("https://tools.dnsstuff.com/#dnsReport|type=domain&&value="+str(que))
		print("[+ Opening] DNS QUERIES : "+str("https://tools.dnsstuff.com/#dnsReport|type=domain&&value="+str(que))+"\n")
		system("whois -v "+str(que)+" >OUTPUT/"+str(que)+'/Info_gathering/whois.txt')
		system("traceroute -v "+str(que)+" >OUTPUT/"+str(que)+'/Info_gathering/traceroute.txt')
		print("[+ Opening] WHOIS RECORDS ARE SAVED  : OUTPUT/"+str(que)+"/Info_gathering/whois.txt")
		print("[+ Opening] TRACEROUTE IS SAVED  : OUTPUT/"+str(que)+"/Info_gathering/traceroute.txt")
		file.close();
		down = input(">>Do you want the google search handbook for advance searches [y|n]?")
		if(down=='y' or down=='Y' or down=='yes' or down=='Yes' or down=='YES'):
			system("wget pdf.textfiles.com/security/googlehackers.pdf")
			system("mv googlehackers.pdf OUTPUT/"+str(que)+"/Info_gathering/")
		dow = input(">>Do you want the OWASP guide for penetration testing [y|n]?")
		if(dow=='y' or dow=='Y' or dow=='yes' or dow=='Yes' or dow=='YES'):
			system("wget https://www.owasp.org/images/1/19/OTGv4.pdf")
			system("mv OTGv4.pdf OUTPUT/"+str(que)+"/Info_gathering/")
		done = pyfiglet.figlet_format("Footprinting Done!")
		print(done)
		time.sleep(5)
		system('clear')
	elif(ch==2):
		system("clear")
		print(ascii_banner)
		print("\n\033[1;35;48mIMPORTANT :: \n[+] Just provide the URL or IP address of the target.\n[+] It will scan the domain thoroghly for open ports ,running services ,firewalls , outdated versions and much more.\n[+] After scanning is completed output will be saved in the DESKTOP/OUTPUT/[WEBSITE]/scan.txt")
		name = input("\n\n\t\t\tIP OR Name of the Target you want to scan : ")
		system("mkdir OUTPUT/"+str(name))
		system("mkdir OUTPUT/"+str(name)+"/Scanning")
		system("nmap -v -p 1-1000 -sV -O -sS -T4 -oN OUTPUT/"+str(name)+"/Scanning/scan.txt"+" "+str(name))
		down = input(">>Do you want to downnload Nmap Cheatsheet [y/n] ?")
		if(down=='y' or down=='Y' or down=='yes' or down=='Yes' or down=='YES'):
			system("wget https://blogs.sans.org/pen-testing/files/2013/10/NmapCheatSheetv1.1.pdf")
			system("mv NmapCheatSheetv1.1.pdf OUTPUT/"+str(name)+"/Scanning/")
		scan = pyfiglet.figlet_format("Scanning Done!")
		print(scan)
		time.sleep(5)
	elif(ch==3):
		print(ascii_banner)
		q = "q"
		print("\n\033[1;35;48mIMPORTANT :: \n[+] Search smartly for the exploit using OPTION 1.\n[+] Using OPTION 2 ,you could get familier with metasploit and can use it to load the found exploit.\n[+] Using OPTION 3 ,You could search for the sql injection in any web application.\n[+] Using OPTION 4 ,You could read about the methodologies of attacking a system or application.")
		while(q=="q" or q=="quit" or q=="Q"):
			system("clear")
			enumeration()
			name = input(">>[+ Target] : ")
			system("mkdir OUTPUT/"+str(name))
			system("mkdir OUTPUT/"+str(name)+"/Enumeration")
			inpp = int(input(">>Hacking : "))
			if(inpp==1):
				st = input(">>Enter the cve or service name to find exploit for that : ")
				s = input(">>Do you want the save results ?(y/n) : ")
				if(s=='y' or s=='YES' or s=='Yes' or s=='yes'):
					system("echo 'Search results for the "+str(st)+" ' > OUTPUT/"+str(name)+"/Enumeration/exploits.txt")
					system("searchsploit "+str(st) +" >> OUTPUT/"+str(name)+"/Enumeration/exploits.txt")
				system("searchsploit "+str(st))
				q = input(">>To Go Back Press q or Q ? : ")
			elif(inpp==2):
				system("clear")
				print("\033[1;33;48m")
				ascii = pyfiglet.figlet_format("!Vulnorator!  - Metasploit")
				print(ascii)
				system("service postgresql start")
				print("....Enter `quit` to exit the metasploit")
				print("[+]To Use Exploit         : use <exploit name>")
				print("[+]To See Requirements    : show options")
				print("[+]To Set the environment : set RHOSTS <target IP>")
				print("[+]To See Payload         : show payloads")
				print("[+]To Use the payload     : set PAYLOAD <payload name>")
				print("[+]To Exploit             : exploit or run")
				i = input(">>Do you want to record your further work with metasploit as POC ?[y/n] : ")
				if(i=='y' or i=='YES' or i=='Yes' or i=='yes'):
					print("......Enter `exit` to stop recording work")
					system("script --timing OUTPUT/"+str(name)+"/Enumeration/metasploit.log")					
				system("msfconsole -q")
				q = input(">>To Go Back Press q or Q ? : ")
			elif(inpp==3):
				system("clear")
				print(ascii_banner)
				st = input(">>Enter the target domain or link  where you want to launch sqlmap : ")
				sqlmap()
				c = input(">>Hacking : ")
				if(c==1):
					system("sqlmap -u "+str(st)+" --dbs")
				elif(c==2):
					db = input(">>[+] Database Name : ")
					system("sqlmap -u "+str(st)+" -D "+str(db)+" --tables")
				elif(c==3):
					db = input(">>[+] Database Name : ")
					tb = input(">>[+] Table Name : ")
					system("sqlmap -u "+str(st)+" -D "+str(db)+" -T "+str(tb)+" --columns")
				elif(c==4):
					db = input(">>[+] Database Name : ")
					tb = input(">>[+] Table Name : ")
					cn = input(">>[+] Column Name : ")
					system("sqlmap -u "+str(st)+" -D "+str(db)+" -T "+str(tb)+" -C " +str(cn) + " --dump")
				else:
					q='not'
			elif(inpp==4):
				system("clear")
				print(ascii_banner)
				print("How To Get Started in CyberSecurity? ")
				fo = open("learn_cyber.txt",'r')
				ar = fo.readlines()
				for i in ar:
					print(i)
				inu = input("Press any key to go back ........")
			else:
				system("clear")
				q='not'

	elif(ch==4):
		system("clear")
		fun = pyfiglet.figlet_format("THREAT METER",font="slant")
		print(fun)
		print("\n\033[1;32;48mIMPORTANT :: \n[+] There is a explanation of all vulnerabilities that can exist except for zero-days.\n[+] This is displaying the no of vulnerability with their threat level.\n[+] Each vulnerability is mentioned with its subparts threat level.\n")
		fil = open("meter.txt")
		ar = fil.readlines()
		for i in ar:
			print(i)
		fil.close()
		sc = input("\n[*]PRESS ANY KEY TO CONTINUE")		
	elif(ch==5):
		inp = 1
		while(inp == 1):
			system("clear")
			print(ascii_banner)
			print("\n\033[1;35;48mIMPORTANT :: \n[+] These are explanations for all vulnerabilities that can exist except for zero-days.\n[+] Choose any choice among this list to see details of that vulnerability.\n[+] Details consist of vulnerability subparts,its exposure,its exploitation,ways of discovering,blogs related to this vulnerability.")
			fil = open("vulnrator.txt")
			ar = fil.readlines()
			for i in ar:
				print(i)
			fil.close()
			switch = {1:"OUTPUT/vulnerability/servermis.txt",2:"OUTPUT/vulnerability/srvsideinj.txt",3:"OUTPUT/vulnerability/brokensession.txt",4:"OUTPUT/vulnerability/sensitivedataexp.txt",5:"OUTPUT/vulnerability/xss.txt",6:"OUTPUT/vulnerability/bac.txt",7:"OUTPUT/vulnerability/csrf.txt",8:"OUTPUT/vulnerability/ddos.txt",9:"OUTPUT/vulnerability/redirect.txt",10:"OUTPUT/vulnerability/extbehv.txt",11:"OUTPUT/vulnerability/insuff_conf_secr.txt",12:"OUTPUT/vulnerability/vulnerable_comp.txt",13:"OUTPUT/vulnerability/Insecure_DATA.txt",14:"OUTPUT/vulnerability/lackofbinary.txt",15:"OUTPUT/vulnerability/insdatatransport.txt",16:"OUTPUT/vulnerability/insecureos.txt",17:"OUTPUT/vulnerability/brokencrypto.txt",18:"OUTPUT/vulnerability/privacyconcern.txt",19:"OUTPUT/vulnerability/nwsec_conf.txt",20:"OUTPUT/vulnerability/mobile_sec.txt",21:"OUTPUT/vulnerability/client_inj.txt",22:"OUTPUT/vulnerability/auto_scu_conf.txt"}
			chg = int(input("\t\t\t>>HACKING : "))
			system("clear")
			print(ascii_banner)
			fi = open(str(switch[chg]),'r')
			a = fi.readlines()
			for j in a:
				print(j)
			fi.close()
			inp = int(input("\n\nTo Go Back Press 0 or To see other Vulnerabilty details Press 1 : "))
			system("clear")
	elif(ch==6):
		system("clear")
		print("\033[1;31;48m")
		print(ascii_banner)
		print("\033[1;36;48m")
		fir = open("about.txt" )
		ar = fir.readlines()
		for i in ar:
			print(i)
		fir.close()
		iny = input("Press any key to move ahead............")
	elif(ch==7):
		fun = pyfiglet.figlet_format("Thanks for using Vulnorator !")
		print(fun)
		exit()
