import json
import pypandoc

section_template = "# {title}\n\n{subsections}"
subsection_template = "### {title}\n\n{content}"

def alternateMerge(arr1, arr2) :
    i = 0; j = 0;
    arr3 = []
    # Traverse both array
    while (i < len(arr1) and j < len(arr2)) :
        arr3.append(arr1[i])
        i += 1         
        arr3.append(arr2[j])
        j += 1
    return arr3 + arr1[i:] + arr2[j:]


def absolutify(mdtext, baseurl):
    return mdtext.replace("](/", "]("+baseurl+"/")


def mdfy(text):
    return pypandoc.convert_text(
        (text).encode('ascii', 'ignore').decode(),
        "md",
        format="html",
        extra_args=['--wrap=preserve']
    )


def singleline(text):
    return mdfy(text).replace("\\\n", " - ")


def makeSubsection(data):
    if data.get("ignorecv", False):
        return ""
    title = " | ".join([data["title"]] + [i for i in data["subtitle"] if i])
    content = mdfy(data["content"])
    return subsection_template.format(title=title, content=content)


def makeSection(data):
    if data.get("ignorecv", False):
        return ""
    merged = alternateMerge(data["col1"], data["col2"])
    if data.get("reversecv", True):
        merged = reversed(merged)
    subsections = "\n".join([makeSubsection(i)
                             for i in merged])
    sectiontext = section_template.format(
        title=singleline(data["pagename"]), subsections=subsections)
    return sectiontext


def makeCV(data):
    title = open("templates/header.yml").read()
    sections = "\n".join([makeSection(i) for i in data["pages"]])
    return "---\n" + title + "---\n\n" + absolutify(sections, data["baseurl"])


try:
    print(pypandoc.get_pandoc_version())
except OSError as e:
    pypandoc.pandoc_download.download_pandoc()

with open("data.json", "r", encoding="utf8") as f:
    data = json.loads(f.read())
    with open("cv.md", "w", encoding="utf8") as cv:
        cv.write(makeCV(data))

pypandoc.convert_file("cv.md", "pdf", outputfile="cv.pdf", extra_args=["--template=./templates/latex.tex"])
#pypandoc.convert_file("cv.md", "html", outputfile="cv.html", extra_args=["-s", "--toc"])
