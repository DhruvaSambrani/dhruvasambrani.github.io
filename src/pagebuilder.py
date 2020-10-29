import json
from random import randint

pagehtml = open("./templates/page.html", "r", encoding="utf8").read()
cardhtml = open("./templates/card.html", "r", encoding="utf8").read()
mainhtml = open("./templates/index_template.html", "r", encoding="utf8").read()
conthtml = open("./templates/contact.html", "r", encoding="utf8").read()
colors = {"light": ("black", ""), "dark": ("near-white", "home-invert")}

def maketolength(text, length):
    padd = length-len(text)
    l1 = (padd) // 2
    return (" " * l1) + text + (" " * (padd - l1))


def makesubtitle(subtitle):
    maxlength = max(map(lambda l: len(l), subtitle))
    return " | ".join(map(lambda l: maketolength(l, maxlength), subtitle))


def makeCard(colelement):
    tid, title, subtitle, content = colelement["id"],  colelement[
        "title"], colelement['subtitle'], colelement["content"]
    return cardhtml.format(id=tid, title=title, subtitle=makesubtitle(subtitle), content=content)


def makepage(pageid, pagename, colorscheme, col1, col2):
    try:
        fg, invert = colors[colorscheme[0]]
    except KeyError:
        fg, invert = "", ""
    cs = fg + " " + " ".join(colorscheme[1:])
    return pagehtml.format(
        pageid=pageid,
        pagename=pagename,
        colorscheme=cs,
        invert=invert,
        col1="\n".join(col1),
        col2="\n".join(col2))


def makecontent(pagedata):
    pages = []
    for page in pagedata:
        col1, col2 = [], []
        for colelement in page["col1"]:
            col1.append(makeCard(colelement))
        for colelement in page["col2"]:
            col2.append(makeCard(colelement))
        pages.append(
            makepage(page["pageid"], page["pagename"], page["colorscheme"], col1, col2))
    return "\n".join(pages)


def makecontact(name, url, icon):
    shift = randint(2, 9)
    enc = []
    for i in url:
        enc.append(chr(ord(i) + shift))
    encurl = "".join(enc)
    encurl = encurl.replace("\\", "\\\\")
    return conthtml.format(name=name, url=encurl, shift=shift, icon=icon)


def makefooter(footerdata):
    foots = []
    for footele in footerdata:
        foots.append(makecontact(
            footele["name"], footele["url"], footele["icon"]))
    return "\n".join(foots)


with open("data.json", "r", encoding="utf8") as f:
    data = json.loads(f.read())
    with open("index.htm", "w", encoding="utf8") as index:
        index.write(mainhtml.format(
            title=data["title"],
            maincontent=makecontent(data["pages"]),
            footerdata=makefooter(data["contact"])))
