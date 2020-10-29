import json
import sys
import pypandoc

section_template = "# {title}\n\n{subsections}"
subsection_template = "### {title}\n\n{content}"


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
    title = " | ".join([data["title"]] + [i for i in data["subtitle"] if i])
    content = mdfy(data["content"])
    return subsection_template.format(title=title, content=content)


def makeSection(data):
    subsections = "\n".join([makeSubsection(i)
                             for i in data["col1"]+data["col2"]])
    sectiontext = section_template.format(
        title=singleline(data["pagename"]), subsections=subsections)
    return sectiontext


def makeCV(data):
    title = """---
title: Dhruva Sambrani
colorlinks: true
block-headings: true
---
"""
    sections = "\n".join([makeSection(i) for i in data["pages"]])
    return title + absolutify(sections, data["baseurl"])


try:
    pypandoc.get_pandoc_version()
except OSError as e:
    pypandoc.pandoc_download.download_pandoc()

with open("data.json", "r", encoding="utf8") as f:
    data = json.loads(f.read())
    with open("cv.md", "w", encoding="utf8") as cv:
        cv.write(makeCV(data))

pypandoc.convert_file("cv.md", "pdf", outputfile="cv.pdf")
