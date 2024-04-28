import os
import sys

red = "\033[1;31;40m"
clear = "\033[1;0;00m"

print("Network Penetration Testing Framework \n")
print("Dissertation - BITS, Pilani \n")
print("Prepared By :\n")
print("Uplabdhi Singh || 2022ht66111 || M.Tech - Computing Systems & Infrastructure \n")

command = 1

dir_exist = os.popen("ls | grep -c 'dir_results'").read()
R_DIR = int(dir_exist)

if R_DIR == 1:
	print("")

elif R_DIR == 0:
	os.system("mkdir dir_results")

else:
	print("Something went wrong")


dir_exist = os.popen("ls | grep -c headers").read()
R_DIR = int(dir_exist)

if R_DIR == 1:
	print("")

elif R_DIR == 0:
	os.system("mkdir headers")


dir_exist = os.popen("ls | grep -c port_scan").read()
R_DIR = int(dir_exist)

if R_DIR == 1:
	print("")

elif R_DIR == 0:
	os.system("mkdir port_scan")


while command != "exit":
	command = input("COMMAND"+red+"|>"+clear)

	if command == "":
		command = 1

	elif command == "hosts":
		print("\n")
		os.system('cat hosts.txt')
		print("\n")

	elif command == "alive":
		os.system('nmap -sn -iL hosts.txt')

	elif command == "clear":
		os.system('clear')

	elif command == "ports":
		os.system('python3 nmapScanner.py')

	elif command == "dir":
		os.system("cat hosts.txt | xargs -I{}  python3 dirsearch/dirsearch.py -u http://{} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt  -e php,jsp,rb,py,js,asp,aspx,zip,sql,tar,txt,key,doc,docx,html,jar,groovy,back,xml,ini,inc,config,json,yml,conf,cgi --format plain")

	elif command == "headers":
		os.system("cat hosts.txt | xargs -I{} sh -c 'curl -sI http://{} > headers/sample.txt'")
		os.system("cat headers/sample.txt")

	elif command == "scan":
		os.system("nmap -v -A -Pn -p- -T4 -iL hosts.txt")
		os.system("cat hosts.txt | xargs -I{}  python3 dirsearch/dirsearch.py -u http://{} -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -e php,jsp,rb,py,js,asp,aspx,zip,sql,tar,txt,key,doc,docx,html,jar,groovy,back,xml,ini,inc,config,json,yml,conf,cgi --format plain")
		os.system("cat hosts.txt | xargs -I{} sh -c 'curl -sI http://{} > headers/{}.txt'")
		
	elif command == "exploit":
		print('Type the exploit name or version number to search :\n')
		inputText=input("module name or version: ")
		os.system('searchsploit '+inputText)
		print('Starting metasploit to check available cve: \n')
		os.system('msfconsole')
	
	elif command == "report":
		print('Generating report...\n')
		os.system("nmap -A -Pn -T4 -oN reportOutput.txt -iL hosts.txt")
		os.system('python reportPDF.py')

	elif command == "help":
		print('''
		[exit]
		[clear]
		[hosts]	list all hosts
		[alive]	check if hosts are alive
		[ports]	port scan of all hosts
		[dir]	Directory Enumeration
	        [headers] Grab Web Headers
		[scan]	Grab Headers, Port Scan and Directory Enumeration for all hosts
		[exploit] Exploitation as per available CVE 
		[report] Generate a report
		''')

	else:
		print("[+] Unknown Command")
