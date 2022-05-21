import csv

dataset1 = []
dataset2 = []

with open("final.csv", "r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dataset1.append(row)

with open("archive_dataset1.csv", "r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        dataset2.append(row)

header1 = dataset1[0]
header2 = dataset2[0]

planetData1 = dataset1[1:]
planetData2 = dataset2[1:]

headers = header1 + header2

planetData = []

for index,dataRow in enumerate(planetData1):
    planetData.append(planetData1[index]+planetData2[index])

with open("finalResult.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planetData)