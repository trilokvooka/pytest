import csv
import matplotlib.pyplot as plt

filePath="C:\\Users\\trilok.vooka\\Downloads\\cap_rooms.csv"
ppn = []
beds = []
with open(filePath, 'r') as file:
    reader = csv.reader(file)
    next(reader)    
    for row in reader:    
      ppn.append(float(row[0]) if row[0] else 0)
      beds.append(int(row[1]) if row[1] else 0)
ppn = [str(item) for item in ppn]
number_of_bedrooms = [str(item) for item in beds]
plt.figure(figsize=(10, 5))
plt.plot(ppn, beds, marker='o')
plt.xlabel('PPN')
plt.ylabel('Number of Beds')
plt.title('Plot of PPN vs Number of Beds')
plt.grid(True)
plt.show()
