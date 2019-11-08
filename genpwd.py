import os
import sys
import itertools

if sys.platform == "linux" or sys.platform == "linux2":
    os.system("clear")

elif sys.platform == "win32":
    os.system("cls")

strings = []
user_repeats = ""
user_wdlist = "pwdwdlist.txt"

def strings_control():
    global strings
    
    strings = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'z', 'y',
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Z', 'Y', '*', '&', '.', ',', '/']

def user_custom():
    global user_repeats, user_wdlist

    user_repeats = int(input("\033[1;32m Enter Length: \033[1;m"))
    user_wdlist = input("\033[1;32m wordlist: \033[1;m")
    if  len(user_wdlist) < 1:
        print("\033[1;32m Error wordlist not Entered\033[1;m")
        sys.exit()
        
    while True:
        user_input = input("\033[1;32m Enter Words then enter --done when your finished: \033[1;m")
        
        if user_input == "--done":
            break
        
        strings.append(user_input)
        
        

def mainfunc(userrange, userrange1, userchoice=0):
    global user_wdlist, user_repeats

    for e in range(userrange, userrange1):
        opnr = open(user_wdlist, 'a+')
        if userchoice != 0:
            user_repeats += 1
        for combo in itertools.product(''.join(strings), repeat=user_repeats):
            chars = ''.join(combo)
            opnr.write(chars + "\n")
            sys.stdout.write("\r \033[1;32m [+}Writing %s: %s  Length: %s\033[1;m"%(user_wdlist, chars, user_repeats))
            sys.stdout.flush()
    
    opnr.close()



def user_select():
    global user_repeats

    user_input = input("\033[1;32m Do you want custom wordlist y/n \033[1;m")
    if user_input == "n":
        user_repeats = 2
        strings_control()
        mainfunc(2, 11, 1)

    elif user_input == "y":
        user_custom()
        mainfunc(0, 1)
    

if __name__ == "__main__":
    user_select()