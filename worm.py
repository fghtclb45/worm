import os
import git
os.system("pip install GitPython")
a = "\033[1m" #Koyu yazı
b = "\033[30m" # siyah
c = "\033[31m" #kırmızı
d = "\033[33m" #sarı
e = "\033[34m" #mavi
f = "\033[47" #background beyaz
q = "\033[0m" #no effect
j = "\033[35m" #mor
z = "\033[36m" #cyan
wh = "\033[37m" #beyaz
po = "\033[32m"
print(a+d+"""__      _____  _ __ _ __ ___  / _ \ / _ \ _ __  _   _ 
\ \ /\ / / _ \| '__| '_ ` _ \| | | | | | | '_ \| | | |
 \ V  V / (_) | |  | | | | | | |_| | |_| | |_) | |_| |
  \_/\_/ \___/|_|  |_| |_| |_|\___/ \___/| .__/ \__, |
                                         |_|    |___/""")
print(c+"""			 |--------|
			 |1 tool  |
    			 |4 choice|
			 |--------|
""")

print(a+z+"[1-]",a+po+"Zenmap")
print(a+z+"[2-]",a+po+"Build-Malware")
sec = input("[set>] \n")
if sec == "1":
	os.system("sudo apt-get install nmap")
	print(a+z+"""		#       #  #   	#   ######  ######
		     # #     #  # #   # #   #    #  #    #
		     #  #    #  #  # #  #   #    #  #    #
		     #   #   #  #   ##  #   ######  #####    
		     #    #  #  #       #   #    #  #
		     #     # #  #       #   #    #  #
		     #      #   #       #   #    #  #
       		""")
	print(a+c+"""
		[1 tool 10 choice]\n""")
	while True:
		set = input(a+e+"[Target İp >] ")
		print(a+z+"[1-]",a+po+"Intense scan")
		print(a+z+"[2-]",a+po+"Intense scan plus UDP")
		print(a+z+"[3-]",a+po+"Intense scan,all TCP ports ")
		print(a+z+"[4-]",a+po+"Intense scan,no ping")
		print(a+z+"[5-]",a+po+"Ping scan")
		print(a+z+"[6-]",a+po+"Quick scan")
		print(a+z+"[7-]",a+po+"Quick scan plus")
		print(a+z+"[8-]",a+po+"Quick scan traceroute")
		print(a+z+"[9-]",a+po+"Regularscan")
		print(a+z+"[10-]",a+po+"SLow comprenhensive scan")
		sec = input(z+a+"[set> ]")
		def set1():
			os.system("nmap -T4 -A -v "+set)
		def set2():
			os.system("nmap -sS -sU -T4 -A -v "+set)
		def set3():
			os.system("nmap -p 1-65535 -T4 -A -v "+set)
		def set4():
			os.system("nmap -T4 -A -v -Pn "+set)
		def set5():
			os.system("nmap -sn "+set)
		def set6():
			os.system("nmap -T4 -F "+set)
		def set7():
			os.system("nmap -sV -T4 -O -F --version-light "+set)
		def set8():
			os.system("nmap -sn --traceroute "+set)
		def set9():
			os.system("nmap "+set)
		def set10():
			print("--NOT FOUND--")
					
		if sec == "1":
			set1()
		elif sec == "2":
			set2()
		elif sec == "3":
			set3()
		elif sec == "4":
			set4()
		elif sec == "5":
			set5()
		elif sec == "6":
			set6()
		elif sec == "7":
			set7()

		elif sec == "8":
			set8()
		elif sec == "9":
			set9()
		elif sec == "10":
			set10()
		elif sec == "exit":
			break
		else:
			print("Yanlış veya hatalı giriş!")
if sec == "2":
	txt = "closed"
	jpg = "closed"
	
	def options():
                print(c+" -"*20)
		print(po+'txt	',txt)
		print(po+"jpg	",jpg)
                print(c+" -"*20)
	while True:
		birb = input("w0rm >")
		if birb == "show options":
			options()
		elif birb == "set jpg open":
			print("jpg => open")
			jpg = "open"
		elif birb == "set txt open":
			print("txt => open")
			txt = "open"

		elif birb == "run":
			if txt == "open":
				dizin = os.getcwd()
				git.Git(dizin).clone("https://github.com/fghtclb45/txt")
			elif jpg == "open":
				dizin = os.getcwd()
				git.Git(dizin).clone("https://github.com/fghtclb45/jpg")
                        elif jpg and txt == "open":
                                dizin = os.getcwd()
                                git.Git(dizin).clone(url)
                        
			else:
				print("OK...")			
