logins_Users = input('введите логин')
fileconfig = open ('adler.py', 'a')
fileconfig.write(logins_Users)
fileconfig.close()
fileconf = open ('adler.py', 'r')
print(fileconf.read())
fileconf.close()
