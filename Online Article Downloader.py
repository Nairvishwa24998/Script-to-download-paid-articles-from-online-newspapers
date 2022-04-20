# function to generate filename
def filenamegen(link):
     val = ""
     # the if and else commands are just a way to obtain the last characters upto slash which would be used as the filename
     if '.html' in link:
         s = link[::-1][5:][::-1]
         x = s[::-1].index('/')
         val = s[::-1][:x][::-1]
     else:
         s = link[::-1].index('/')
         val = link[::-1][:s][::-1]
     for item in val:
         if item == '?' or item == '=':
             val = val.replace(item, "")
     return val


# Relevant libraries
from urllib.request import Request, urlopen

# Obtain the link
link = input()

myrequest = Request(link, headers = {'User-Agent': 'Mozilla/5.0'})

# Needed to decode from byte format
my_HTML = urlopen(myrequest).read().decode('UTF-8')

# add html to the name to save it in html format
outputfilename = filenamegen(link) + '.html'

# Writing to that file
with open(outputfilename, 'w',encoding="utf-8") as file:
    for item in my_HTML:
        file.write(str(item))



