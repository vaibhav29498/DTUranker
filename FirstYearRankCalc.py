import re
from prettytable import PrettyTable

marksf2 = open('marks2.txt')
marksf1 = open('marks1.txt')
newf = open('FirstYearRankList.html', 'w', encoding='utf-8')
x = PrettyTable(["Rank", "Name", "Roll No.", "Semester I", "Semester II", "Average", "Sem I rank", "Sem II rank", "Percentile(%)", "Change"],encoding='UTF-8')
f1 = open("sem1.txt", 'w')
f2 = open("sem2.txt", 'w')
f3 = open("avg.txt", 'w')
lst = []
for line in marksf2:
    name = re.findall('^[0-9]+ (.+)2016/[AB][0-9]+/[0-9]+', line)
    if len(name) == 1:
        cgpa2 = re.findall('[0-9]+\.[0-9][0-9]', line)
        rollno = re.findall('2016/[AB][0-9]+/[0-9]+', line)
        lst.append([name[0], rollno[0], float(cgpa2[0])])
lst.sort(reverse=True, key=lambda argm: argm[2])
j = 1
r = 0
c = lst[0][2]
for elem in lst:
    r += 1
    if elem[2] < c:
        c = elem[2]
        j = r
    elem.append(j)
for line in marksf1:
    rollno = re.findall('20[0-9][0-9]/[AB][0-9]+/[0-9]+', line)
    if len(rollno) == 1:
        found = 0
        for elem in lst:
            if elem[1] == rollno[0]:
                cgpa1 = re.findall('[0-9]+\.[0-9][0-9]', line)
                elem.insert(2, float(cgpa1[0]))
                break
for elem in lst:
    if len(elem) != 5:
        elem.insert(2, 0.00)
        spclCase = elem[1]
    elem.insert(5, (elem[2]+elem[3])/2)
lst.sort(reverse=True, key=lambda argm: argm[2])
j = 1
r = 0
c = lst[0][2]
for elem in lst:
    r += 1
    if elem[2] < c:
        c = elem[2]
        j = r
    elem.insert(4, j)
    elem[2], elem[3] = float(round(elem[2], 2)), float(round(elem[3], 2))
# for elem in lst:
#     if elem[1] == spclCase:
#         elem[2] = None
#         break
lst.sort(reverse=True, key=lambda argm: argm[6])
j = 1
r = 0
c = lst[0][6]
for elem in lst:
    r += 1
    if elem[6] != c:
        j = r
        c = elem[6]
    elem.append(j)
    elem[6] = round(elem[6], 2)
    diff = elem[4] - elem[5]
    if diff > 0:
        elem.append(u"\u25B2" + " " + str(diff))
    elif diff < 0:
        elem.append(u"\u25BC" + " " + str(-1 * diff)) #HTMLParser.HTMLParser().unescape('&#9660;')
    else:
        elem.append("-")
    elem.append(((1787 - elem[7]+1)/1787) * 100)
    x.add_row([elem[7], elem[0], elem[1], elem[2], elem[3], elem[6], elem[4], elem[5], round(elem[9], 2), elem[8]])
newf.write("<center><b>Developed By Vaibhav Jain<br>Suggestions by Sirjanpreet Singh Banga</b></center>")
newf.write(x.get_html_string())
newf.close()
marksf2.close()
marksf1.close()
