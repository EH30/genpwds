import os
import sys
import itertools

if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")

elif sys.platform == "win32":
    os.system("cls")

strings = []
user_repeats = int(input("\033[1;32m Enter Length: \033[1;m"))

user_wdlist = input("\033[1;32m wordlist: \033[1;m")

if  len(user_wdlist) < 1:
    print("\033[1;32m Error wordlist not Entered\033[1;m")
    sys.exit()

while True:
    user_input = input("\033[1;32m Enter Words enter --done when your finished: \033[1;m")
    
    if user_input == "--done":
        break

    strings.append(user_input)

opnr = open(user_wdlist, 'a+')


for combo in itertools.product(''.join(strings), repeat=user_repeats):
    chars = ''.join(combo)
    
    opnr.write(chars + "\n")
    sys.stdout.write("\r \033[1;32m [+}Writing Wordlist: %s\033[1;m"%(chars))
    sys.stdout.flush()


opnr.close()
