from os import listdir
from os.path import isfile, splitext
from mimetypes import guess_type
filetypes = [".JPG", ".PNG", ".GIF", ".WEBP", ".TIFF", ".PSD", ".RAW", ".BMP", ".HEIF", ".INDD", ".JPEG 2000", ".CR2", ".SVG", ".AI", ".PDF", ".JPEG"]
files = [f for f in listdir() if isfile(f) and splitext(f)[1].upper() in filetypes]
f = open("imagelist.txt", "w")
f.write(";".join(files))
print(len(files), " images found.")
