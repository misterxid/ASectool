import os, sys

print ("\033[00m > Masukan Username & Password")
print ("\033[00m > Jika tidak tahu, harap chat admin")
print ("\033[00m > Ini nomor WhatsApp nya:" "\033[91m +6285733428090")
username = 'ALIF'      
password = 'SECURITY'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input(" > username : ")
	if uname == username:
		pwd = raw_input(" > password : ")

		if pwd == password:
			print "\n\033[00m >>>> SELAMAT DATANG DI TOOL ASectool <<<< ", 
			sys.exit()

		else:
			print "\n\033[91mMaaf, Password salah !!!\033[91m"
			print "Login ulang\n"
			restart()

	else:
		print "\n\033[91mMaaf, Username salah !!!\033[91m"
		print "Login Ulang\n"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
