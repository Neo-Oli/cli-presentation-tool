slides=[]
slides.append("Hello. Press Enter.")
slides.append("How are you?")
slides.append("This is slide number 3")
slides.append("Yes, this is indeed a cli slideshow presentation")
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
slides.append("All it needs is the slides and six lines of python")
slides.append("Infact, I believe it is better than powerpoint.")
slides.append("I hope you have configured your terminal correctly, or this last one will look weird. It's supposed to have colors.")
slides.append("Thank you for using KraftaNet.")

clear='\033[2J\033[1;1H'
print(clear)
for slide in slides:
    print(slide)
    input("")
    print(clear)

