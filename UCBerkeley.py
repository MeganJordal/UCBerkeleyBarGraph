import matplotlib.pyplot as plt
import numpy as np

count = 0
N = 0
malesAccepted = []
femalesAccepted = []
malesRejected = []
femalesRejected = []
freq = []

data = open("berkley.txt", "r")

#Break up the data into lists and make a list of frequencies
for line in data:
    words = line.split(',')
    print(words[0], words[1], words[2], words[3])
    freq.append(words[3])
    count = count+1

#print(freq)
#print(count)
N = int(count / 4)
#print(N)
#Make a list of males Accepted from all groups
for i in range(0, len(freq), 4):
    num = freq[i]
    num = num.rstrip("\n")
    num = float(num)
    malesAccepted.append(num)


#Make a list of males rejected
for i in range(1, len(freq), 4):
    num = freq[i]
    num = num.rstrip("\n")
    num = float(num)
    malesRejected.append(num)

#Make a list of females accepted
for i in range(2, len(freq), 4):
    num = freq[i]
    num = num.rstrip("\n")
    num = float(num)
    femalesAccepted.append(num)

#Make a list of females rejected
for i in range(3, len(freq), 4):
    num = freq[i]
    num = num.rstrip("\n")
    num = float(num)
    femalesRejected.append(num)


print(malesAccepted)
print("---------------")
print(malesRejected)
print("---------------")
print(femalesAccepted)
print("---------------")
print(femalesRejected)

width = 0.3                                 # the width of the bars: can also be len(x) sequence
#xlabel_offset = 0.17                       #width / 2.0 to center xlabels on the bar
ind = np.arange(N)                          # the x locations for the groups


p1 = plt.bar(ind, malesAccepted, width, color='#4922bf')
p2 = plt.bar(ind, femalesAccepted, width, color='#bcf442', bottom=malesAccepted)
p3 = plt.bar(ind+0.3, malesRejected, width, color='#a01414')
p4 = plt.bar(ind+0.3, femalesRejected, width, color='#42f4e8', bottom=malesRejected)

plt.ylabel('Frequency')
plt.xlabel('Groups')
plt.title('Acceptance Rate at UC Berkeley')
plt.xticks(ind, ('A', 'B', 'C', 'D', 'E', 'F'))
plt.yticks(np.arange(0,800, 50))
plt.legend((p1[0], p2[0], p3[0], p4[0]), ('Males Accepted', 'Females Accepted', 'Males Rejected', 'Females Rejected'))

plt.show()






















"""import matplotlib.pyplot as plt
import numpy as np
count = 0
N = 5
width = 0.3

deptA_male_admitted = 512
deptA_female_admitted = 89
deptA_male_rejected = 313
deptA_female_rejected = 19
deptB_male_admitted = 353
deptB_female_admitted = 17
deptB_male_rejected = 207
deptB_female_rejected = 8

xlabel_offset = 0.17
ind = np.arange(xlabel_offset, N, 1)

p1 = plt.bar(ind, deptA_male_admitted, width, color = '#d600ff')
p2 = plt.bar(ind, deptA_female_admitted, width, color = '#00ff00', bottom = deptA_male_admitted)

plt.ylabel('Frequency')
plt.title('Admission By Group and Gender')
plt.xticks(ind, ('A', 'B'))
plt.yticks(np.arange(0, 1000, 50))
plt.legend((p1, p2), ("Male", "Female"))




data = open("berkley.txt", "r")
admit = []
gender = []
dept = []
freq = []
for line in data:
        words = line.split(',')
        print(words[0], words[1], words[2], words[3])
        admit.append(words[0])
        gender.append(words[1])
        dept.append(words[2])
        freq.append(words[3])
print(admit)
print(gender)
print(dept)
print(freq)

plt.show()"""
