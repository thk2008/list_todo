
list=[]
todo=input("enter todo, or 'q' to stop: ")
while (todo != 'q'):
    list.append(todo)
    todo=input("enter todo, or 'q' to stop:")
print(list)

import csv
with open("todo.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(list)  # writes each word to a cell
    writer.writerows(list) # writes each letter to a cell

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(list)


   #Open File
filename = input("Enter the name of the data file: ")
infile = open(filename, 'r')
print(infile.read())
#Read lines from File
#Close File  
    
