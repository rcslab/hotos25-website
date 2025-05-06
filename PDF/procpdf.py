#!/usr/bin/env python3

import csv
import pandas

papers = pandas.read_csv("accepted-papers-and-panels.csv", index_col="ID", quotechar = '"')

def StartDay(msg):
    print("{\\centering\\bf\\large " + msg + "}\\\\")
    print("\\vspace{0.1em}\n")

def StartSession(title, time, chair):
#    print("\\begin{centering}")
#    print("{\\bf\\large " + title + "}\\\\")
#    print("{\\it " + time + "}\\\\")
#    print("\\indent {\\bf Session Chair:} " + chair + "\\\\")
#    print("\\end{centering}")
#    print("\\setlength\\tabcolsep{1pt}")
#    print("\\begin{tabular}{p{2in}p{4.5in}}")
#    print("\\rowcolor{sessioncolor}")
#    print("{\\color{white}" + time + "}", "{\\color{white}" + title + "}\\\\")
#    print("\\rowcolor{sessioncolor}")
#    print("", "{\\color{white}Session Chair: " + chair + "}\\\\")
#    print("\\rowcolor{sessioncolor}", "\\\\")
#    print("\\end{tabular}")
#    print("\\vspace{1em}\n")
     #print("\\begin{table*}[h!]")
     print("\\begin{NiceTabular}{p[l]{1in}p[l]{5.5in}}")
     print("\\CodeBefore")
     print("\\rowcolor{sessioncolor}{1-3}")
     print("\\Body")
     #print("", "\\\\")
     print("{\\color{white}\\bf " + time + "} & {\\color{white}\\bf " + title + "}\\\\")
     print(" & {\\color{white}Session Chair: " + chair + "}\\\\")
     print(" & \\\\")
     print("\\end{NiceTabular}")
     print("\\vspace{0.1em}\n")
     #print("\\vspace{1em}\n")
     #print("\\end{table*}")

def PrintPapers(paperlist, pre = None):
    if (pre != None):
        print("\\begin{centering}")
        print("{\\bf " + pre + "}\\\\")
        print("\\end{centering}\\vspace{1em}")
    print("\\begin{enumerate}[resume]")
    for i in paperlist:
        #print("\\begin{centering}")
        print("\\item {\\bf " + papers.loc[i]["Title"].replace("_", "\\_") + "}\\\\")
        print("" + papers.loc[i]["Authors"].replace("&","\\&") + "\\\\")
        #print("\\end{centering}")
        #print("\\vspace{2em}\n")
    print("\\end{enumerate}")
    print("\\vspace{0.1em}\n")

def PrintBreak(time, msg):
     #print("\\begin{table*}[h!]")
     print("\\begin{NiceTabular}{p[l]{1in}p[l]{5.5in}}")
     print("\\CodeBefore")
     print("\\rowcolor{breakcolor}{1-2}")
     print("\\Body")
     #print("", "\\\\")
     #print("\\vspace{0.5em}")
     print("{\\bf " + time + " } & {\\bf " + msg + " }\\\\")
     #print("", "\\\\")
     print("\\end{NiceTabular}")
     print("\\vspace{0.1em}\n")
     #print("\\end{table*}")

def PrintPanel(time, panel):
    #print("\\begin{centering}")
    #print("{\\bf Panel: " + papers.loc[panel]["Title"] + "}\\\\")
    #print(papers.loc[panel]["Authors"] + "\\\\")
    #print(time + "\\\\")
    #print("\\end{centering}\n")
    print("\\begin{NiceTabular}{p[l]{1in}p[l]{5.5in}}")
    print("\\CodeBefore")
    print("\\rowcolor{panelcolor}{1-3}")
    print("\\Body")
    #print("", "\\\\")
    print(" & {\\color{black}\\bf Panel: " + papers.loc[panel]["Title"] + "}\\\\")
    print(" & \\color{black}" + papers.loc[panel]["Authors"] + "\\\\")
    print(" & \\\\")
    print("\\end{NiceTabular}")
    print("\\vspace{0.1em}\n")

#
# Wednesday
#

print("""\\documentclass[letter,10pt]{article}

\\usepackage{fontspec}
\\usepackage{fontenc}

\\usepackage{graphicx}
\\usepackage{microtype}
\\usepackage[table]{xcolor}
\\usepackage{nicematrix}
\\usepackage{enumitem}
      
\\definecolor{sessioncolor}{rgb}{0.27, 0.33, 0.42} 
\\definecolor{breakcolor}{rgb}{0.74, 0.95, 0.76} 
\\definecolor{panelcolor}{rgb}{0.75, 0.90, 0.92} 

\\usepackage[margin=1in]{geometry}

\\setmainfont{Myriad Pro}

\\begin{document}

\\pagestyle{empty}
\\title{HotOS 2025 Workshop Program}
\\date{}
\\maketitle
\\vspace{-1em}
""")

StartDay("Tuesday -- May 13, 2025")

PrintBreak("14:00--17:00", "Registration Desk in Mount Stephen Hall (Mezzanine 1)")
PrintBreak("18:00--20:00", "Welcome Reception in Mount Stephen Hall (Mezzanine 1)")

StartDay("Wednesday -- May 14, 2025")
PrintBreak("8:00--9:00", "Breakfast Buffet (Alhambra Room)")

StartSession("How to be in this world: Securing Adolescent AIs", "9:00--10:30", "Timothy Roscoe")
PrintPapers([156, 100, 290], "Introductory Remarks")

PrintBreak("10:30--10:45", "Coffee Break (Alhambra Foyer)")

StartSession("Breaking the Big Goal of Verification into Smaller Pieces", "10:45--12:00", "Alexandra (Sasha) Fedorova")
PrintPapers([67, 139, 206])

PrintBreak("12:00--13:15", "Lunch Buffet (Alhambra Room)")

StartSession("Tiered Storage: Yet More Systems Problems Solved with Another Layer of Indirection", "13:15--14:30", "Kim Keeton")
PrintPapers([72, 321, 144])

PrintBreak("14:30--15:00", "Coffee Break (Alhambra Foyer)")

StartSession("In Principle, Sure, but in Practice ...", "15:00--16:00", "James Mickens")
PrintPapers([56, 69])

PrintPanel("16:10--17:00", 399)

PrintBreak("", "Dinner on Your Own")

#
# Thursday
#

print("\\newpage")
StartDay("Thursday -- May 15, 2025")
PrintBreak("8:00--9:00", "Breakfast Buffet (Alhambra Room)")

StartSession("Throwback Thursday: Classic OS Design Issues, Remixed", "9:00--10:15", "Don Porter")
PrintPapers([364, 414, 178])

PrintBreak("10:15--10:45", "Coffee Break (Alhambra Foyer)")

StartSession("What Can we Learn from Learned Systems?", "10:45--12:00", "Aurojit Panda")
PrintPapers([113, 292, 251])

PrintBreak("12:00--13:15", "Lunch Buffet (Alhambra Room)")

StartSession("Faster Pipes", "13:15--14:30", "Ana Klimović")
PrintPapers([60, 240, 207])

PrintBreak("14:30--14:50", "Coffee Break (Alhambra Foyer)")

PrintPanel("14:50--15:50", 135)

StartSession("The Mind Fairly Boggles: Understanding Datacenter Application Behavior", "16:00--17:15", "Shivaram Venkataraman")
PrintPapers([71, 426, 106])

PrintBreak("18:00--19:00", "Cocktails (Alhambra Foyer)")
PrintBreak("19:00--21:00", "Banquet (Alhambra Room)")

#
# Friday
#

print("\\newpage")
StartDay("Friday -- May 16, 2025")
PrintBreak("8:00--9:00", "Breakfast Buffet (Alhambra Room)")

StartSession("Handling Malthusian Growth in Datacenter Infrastructure", "9:00--10:15", "Hugo Sadok")
PrintPapers([429, 102, 358])

PrintBreak("10:15--10:45", "Coffee Break (Alhambra Foyer)")

StartSession("Hot OSes without a Hot Planet", "10:45--12:00", "Natacha Crooks")
PrintPapers([17, 190, 92])

PrintBreak("", "Lunch on Your Own")

print("""\\end{document}""")
