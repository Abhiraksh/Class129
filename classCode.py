import csv

data = []

with open("archive_dataset.csv", "r") as f:
    csvReader = csv.reader(f)
    for row in csvReader:
        data.append(row)

headers = data[0]
planetData = data[1:]

# ascii values: A - 65, a - 97

for data1 in planetData:
    data1[2] = data1[2].lower()

planetData.sort(key = lambda planetData: planetData[2])

with open("archive_dataset1.csv", "a+") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planetData)


