sex = str(input("sir or ma'am? "))
website = str(input("website: "))
subtopic = str(input("subtopic: "))
message =f"""
​​Dear {sex},
I am Dhruva Sambrani, a Second Year Int. MS student at IISER Mohali, India. Quantum Computing and Information lies in the perfect intersection of the two of my favourite topics, Physics and Programming. As I did my First Year Summer Project with Dr Arvind on "Introduction to Quantum Computing" and realized that I could apply my love for algorithms to this field.

I was looking for a summer internship in the field of Quantum Computing when I chanced upon the {website} website, which led me to your team's page. As I was reading through your research, sub-topics within Quantum Computing such as {subtopic} which got me interested. Hence I am writing this email to request an undergraduate summer internship for the summer (May-August) of 2020 under your coveted guidance.

In the academic domain, I presently have a CPI of 9.5 on 10. My most recent research experience was a Summer project on the Introduction to QC under Prof. Arvind in which I wrote a Julia module which would simulate a Quantum Computer. My other research experiences include a short Winter project on the Black Body Radiation of a relativistically moving particle in Winter 2018 under Dr Jasjeet Bagla.

I am also an avid coder with multiple projects in Android, C++, Julia and Python. A recent project of mine has been a birding App called Minivet under BEL, IISER Mohali of Dr Manjari Jain and an IISER Mohali App for the students.

I hope that my past research and coding make me eligible for carrying out research work under you. As an enthusiastic student, I would like to know if there are any research opportunities available with you in any project as it will be a big step forward in my long term research perspective of specializing in this field.

You may visit my webpage https://dhruvasambrani.github.io to know more about me. I have also attached my CV for your convenience.

Hoping to hear a positive reply from your side and having an enriching experience with you this summer.

Thanks and Regards,
Dhruva Sambrani
"""
from tkinter import Tk
r = Tk()
r.withdraw()
r.clipboard_clear()
r.clipboard_append(message)
r.update() # now it stays on the clipboard after the window is closed
r.destroy()
print(message)
