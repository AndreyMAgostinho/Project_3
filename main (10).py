import csv
import matplotlib.pyplot as plt
import pandas
import numpy as np

file = open('data.csv')
csvreader = csv.reader(file)

header = []
header = next(csvreader)
print(header)
print(header[0])

rows = []
for row in csvreader:
  rows.append(row)

print(rows)
file.close()

print(rows[0])
print(rows[1])



for i in range(len(rows[0])):
  rows[0][i] = int(rows[0][i])
print()
print(rows[0])



plt.yticks(np.arange(0,65,5))
plt.title("Students with Covid")
plt.xlabel("Days")
plt.ylabel('Students')
plt.plot(header, rows[0], '-o', label="High School")
plt.plot(header, rows[1], '-o', label="Parlin School")
plt.legend()
plt.show()
