from collections import Counter
import csv

with open("pro104\SOCR-HeightWeight.csv", newline = '') as f:
    reader = csv.reader(f)
    filedata = list(reader)

filedata.pop(0)
newdata = []
for i in range(len(filedata)):
    num = filedata[i][2]
    newdata.append(float(num))

m = len(newdata)
total = 0

for i in newdata:
    total = total + i

mean = total/m

print(mean)

newdata.sort()

if m%2 == 0:
    median1 = float(newdata[m//2])
    median2 = float(newdata[m//2-1])
    median = (median1 + median2)/2

else:
    median = float(newdata[m//2])

print(median)

data = Counter(newdata)

modeClassIntervals = {
    "100-110": 0,
    "110-120": 0,
    "120-130": 0,
    "130-140": 0,
    "140-150": 0,
    "150-160": 0
}

for weight, occurance in data.items():
    if 100< float(weight) < 110:
        modeClassIntervals["100-110"] += occurance
    if 110< float(weight) < 120:
        modeClassIntervals["110-120"] += occurance
    if 120< float(weight) <130:
        modeClassIntervals["120-130"] += occurance
    if 130< float(weight) <140:
        modeClassIntervals["130-140"] += occurance
    if 140< float(weight) <150:
        modeClassIntervals["140-150"] += occurance
    if 150< float(weight) <160:
        modeClassIntervals["150-160"] += occurance

modeRange, modeoccurance = 0, 0

for range, occurance in modeClassIntervals.items():
    if occurance>modeoccurance:
        modeRange , modeoccurance = [int(range.split("-")[0]), int(range.split("-")[1])], occurance


mode = float((modeRange[0] + modeRange[1]) / 2)
print(f"{mode:2f}")
