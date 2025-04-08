#!/usr/bin/env python3

import csv
import pandas

papers = pandas.read_csv("accepted-papers-and-panels.csv", index_col="ID", quotechar = '"')

def StartDay(msg):
    print("<h3>" + msg + "</h3>")

def StartSession(title, time, chair):
    print("<h4 class=\"sch\">")
    print(title)
    print("<span class=\"sch-time\">" + time + "</span>")
    print("<span class=\"sch-sessionchair\">Session Chair: " + chair + "</span>")
    print("</h4>")

def PrintPapers(paperlist, pre = None):
    print("<table class=\"table\">")
    print("  <tbody>")
    print("    <tr></tr>")
    if (pre != None):
        print("    <tr>")
        print("      <td>" + pre + "</td>")
        print("    </tr>")
    print("    <tr>")
    print("      <td>")
    print("        <ul>")
    for i in paperlist:
        print("          <li>")
        print("          <span class=\"sch-title\">" + papers.loc[i]["Title"] + "</span>")
        print("          <br>")
        print("          <em>" + papers.loc[i]["Authors"] + "</em>")
        print("          </li>")
    print("        </ul>")
    print("      </td>")
    print("    </tr>")
    print("  </tbody>")
    print("</table>")

def PrintBreak(msg):
    print("<table class=\"table\">")
    print("  <tbody>")
    print("    <tr class=\"table-success\">")
    print("      <th>" + msg + "</th>")
    print("    </tr>")
    print("  </tbody>")
    print("</table>")

def PrintPanel(time, panel):
    print("<table class=\"table\">")
    print("  <tbody>")
    print("    <tr class=\"table-info\">")
    print("      <th>" + time + " &mdash; " + papers.loc[panel]["Title"] + "</th>")
    print("    </tr>")
    print("    <tr>")
    print("      <td>")
    print("        <b>Panelists:</b>")
    print("        " + papers.loc[panel]["Authors"])
    print("      </td>")
    print("    </tr>")
    print("  </tbody>")
    print("</table>")

#
# Wednesday
#

print("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>HotOS XX: The 20th Workshop on Hot Topics in Operating Systems</title>
  <meta content="width=device-width, initial-scale=1.0" name="viewport">
  <meta content="" name="keywords">
  <meta content="" name="description">

  <!-- Favicons -->
  <link href="img/favicon.jpg" rel="icon">
  <link href="img/apple-touch-icon.jpg" rel="apple-touch-icon">

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.gstatic.com">
  <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,700,700i|Raleway:300,400,500,700,800" rel="stylesheet">

  <!-- Libraries CSS Files -->
  <link href="lib/font-awesome/css/font-awesome.min.css" rel="stylesheet">
  <link href="lib/bootstrap/css/bootstrap.min.css" rel="stylesheet">

  <!-- Main Stylesheet File -->
  <link href="css/style.css" rel="stylesheet">

  <!-- =======================================================
    Theme Name: TheEvent
    Theme URL: https://bootstrapmade.com/theevent-conference-event-bootstrap-template/
    Author: BootstrapMade.com
    License: https://bootstrapmade.com/license/
  ======================================================= -->
</head>

<body>

  <!--==========================
    Header
  ============================-->
  <header id="header" class="header-fixed">
    <div class="container">
        <div id="logo" class="pull-left">
                <h1><a href="./index.html"><span class="logo-a">HotOS</span> 
                        <span class="logo-b">XX</span></a></h1>
              </div>
      <nav id="nav-menu-container">
        <ul class="nav-menu">
          <li class="menu"><a href="index.html">Home</a></li>
	  <li class="menu"><a href="attend.html">Attend</a></li>
	  <li class="menu"><a href="venue.html">Venue</a></li>
	  <li class="menu"><a href="travel.html">Travel</a></li>
	  <li class="menu"><a href="register.html">Register</a></li>
	  <li class="menu-active"><a href="program.html">Program</a></li>
          <li class="menu"><a href="cfp.html">CFP</a></li>
          <li class="menu"><a href="organizers.html">Organizers</a></li>
        </ul>
      </nav>
    </div>
  </header>

<section id="venue" class="wow fadeInUp"><div class="container">
  <div class="section-header"><h2>Workshop Program</h2></div>""")

PrintBreak("Notice: Please do not email us changes to your paper title and affiliation.  Please update them in HotCRP and they will be updated shortly.")

StartDay("Tuesday &ndash; May 13, 2025")

PrintBreak("14:00&ndash;17:00 &mdash; Registration Desk in Mount Stephen Hall (Mezzanine 1)")
PrintBreak("18:00&ndash;20:00 &mdash; Welcome Reception in Mount Stephen Hall (Mezzanine 1)")

StartDay("Wednesday &ndash; May 14, 2025")
PrintBreak("8:00&ndash;9:00 &mdash; Breakfast Buffet (Alhambra Room)")

StartSession("How to be in this world: Securing Adolescent AIs", "9:00&ndash;10:30", "TBA")
PrintPapers([156, 100, 290], "Introductory Remarks")

PrintBreak("10:30&ndash;10:45 &mdash; Coffee Break (Alhambra Foyer)")

StartSession("Breaking the Big Goal of Verification into Smaller Pieces", "10:45&ndash;12:00", "TBA")
PrintPapers([67, 139, 206])

PrintBreak("12:00&ndash;13:15 &mdash; Lunch Buffet (Alhambra Room)")

StartSession("Tiered Storage: Yet More Systems Problems Solved with Another Layer of Indirection", "13:15&ndash;14:30", "TBA")
PrintPapers([72, 321, 144, 321])

PrintBreak("14:30&ndash;15:00 &mdash; Coffee Break (Alhambra Foyer)")

StartSession("In Principle, Sure, but in Practice ...", "15:00&ndash;16:00", "TBA")
PrintPapers([56, 69])

PrintPanel("16:10&ndash;17:00", 399)

PrintBreak("Dinner on Your Own")

#
# Thursday
#

StartDay("Thursday &ndash; May 15, 2025")
PrintBreak("8:00&ndash;9:00 &mdash; Breakfast Buffet (Alhambra Room)")

StartSession("Throwback Thursday: Classic OS Design Issues, Remixed", "9:00&ndash;10:15", "TBA")
PrintPapers([364, 414, 429])

PrintBreak("10:15&ndash;10:45 &mdash; Coffee Break (Alhambra Foyer)")

StartSession("What Can we Learn from Learned Systems?", "10:45&ndash;12:00", "TBA")
PrintPapers([113, 292, 251])

PrintBreak("12:00&ndash;13:15 &mdash; Lunch Buffet (Alhambra Room)")

StartSession("Faster Pipes", "13:15&ndash;14:30", "TBA")
PrintPapers([60, 240, 207])

PrintBreak("14:30&ndash;15:00 &mdash; Coffee Break (Alhambra Foyer)")

PrintPanel("14:50&ndash;15:50", 135)

StartSession("The Mind Fairly Boggles: Understanding Datacenter Application Behavior", "16:00&ndash;17:15", "TBA")
PrintPapers([71, 426, 106])

PrintBreak("18:00&ndash;19:00 &mdash; Cocktails in Alhambra Foyer")
PrintBreak("19:00&ndash;21:00 &mdash; Banquet (Alhambra Room)")

#
# Friday
#

StartDay("Friday &ndash; May 16, 2025")
PrintBreak("8:00&ndash;9:00 &mdash; Breakfast Buffet (Alhambra Room)")

StartSession("Handling Malthusian Growth in Datacenter Infrastructure", "9:00&ndash;10:15", "TBA")
PrintPapers([178, 102, 358])

PrintBreak("10:15&ndash;10:45 &mdash; Coffee Break (Alhambra Foyer)")

StartSession("Hot OSes without a Hot Planet", "10:45&ndash;12:00", "TBA")
PrintPapers([17, 190, 92])

PrintBreak("Lunch on Your Own")

print("""</section>

  <!--==========================
    Footer
  ============================-->
  <footer id="footer"><div class="container">
    <div class="copyright">
      &copy; SIGOPS, 2024.
    </div>
  </div></footer>

  <a href="#" class="back-to-top"><i class="fa fa-angle-up"></i></a>

  <!-- JavaScript Libraries -->
  <script src="lib/jquery/jquery.min.js"></script>
  <script src="js/venobox.min.js"></script>
  <script src="lib/superfish/hoverIntent.js"></script>
  <script src="lib/superfish/superfish.min.js"></script>
  <script src="js/main.js"></script>
</body>

</html>""")
