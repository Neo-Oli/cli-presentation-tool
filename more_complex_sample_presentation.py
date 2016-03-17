slides=[]
slides.append(r"""
Hello. Press Enter.
""")
slides.append(r"""
How are you?
""")
slides.append(r"""
This is slide number 3
""")
slides.append(r"""
Yes, this is indeed a cli slideshow presentation.
""")
slides.append(r"""

 ______________________________________
< This is how you do multi-line slides >
 --------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
""")
slides.append(r"""
 _____ _     _       _               _   _ _   _      
|_   _| |__ (_)___  (_)___    __ _  | |_(_) |_| | ___ 
  | | | '_ \| / __| | / __|  / _` | | __| | __| |/ _ \
  | | | | | | \__ \ | \__ \ | (_| | | |_| | |_| |  __/
  |_| |_| |_|_|___/ |_|___/  \__,_|  \__|_|\__|_|\___|



Stuff like this can be easily added in vim if you call external programs. `:read ! figlet "This is a title"`

        """)


def printline(line,width):
    print('      \033[0;30m\033[47m   ', end="")
    print(line.ljust(width),end="")
    print('   \033[0m     ')
import os
rows, columns = os.popen('stty size', 'r').read().split()
linewidth=int(columns)-18
clear='\033[2J\033[3;1H'
print(clear)
for slide in slides:
    lines=slide.split('\n')
    for line in lines:
        words=line.split(" ")
        shortline=""
        for word in words:
            testline=shortline + " " +word
            if len(testline) < linewidth:
                shortline=testline
            else: 
                printline(shortline,linewidth)
                shortline=word
        printline(shortline,linewidth)
    i=len(lines)
    while i < int(rows)-7:
        printline("",linewidth)
        i+=1
    input("")
    print(clear)

