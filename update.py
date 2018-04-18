print("updating")
import urllib.request as url
def d(url,filename="cache.txt"):

    with open(filename,"wb") as f:
        
        vz=url.urlopen(url)

        #vz=vz.replace("\\n",'''\n''')
        print(vz)

        f.write(vz.read())



    return vz
try:
  d("https://raw.githubusercontent.com/AwesomeCatStudios/Escape-The-Building-Remix/master/Escape_The_Building_(Four_Rooms).py","Escape_The_Building_(Four_Rooms).py")
except:
    print("Get an internet connection dude!")
