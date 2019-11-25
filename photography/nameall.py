from os import listdir
from os.path import isfile, join
from mimetypes import guess_type
files = [f for f in listdir() if isfile(f) and guess_type(f)[0]!=None and guess_type(f)[0].find("image")!=-1]
f = open("imagelist.txt", "w")
f.write(";".join(files))
