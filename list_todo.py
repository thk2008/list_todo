
import csv

list=[]
todo=input("enter todo, or 'q' to stop: ")
while (todo != 'q'):
    list.append(todo)
    todo=input("enter todo, or 'q' to stop: ")
print(list)

with open("todo.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(list)  # writes each word to a cell
    writer.writerows(list) # writes each letter to a cell

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(list)

# if you change the delimiter to a newline
# this appears to work
with open("out2.csv", "w") as f:
  writer = csv.writer(f, delimiter='\n')
  writer.writerow(list)

# why not just write the file as one item per line
with open("out3.csv", "w") as f:
  for item in list:
    print(item, file=f)

# Open File
filename = input("Enter the name of the data file: ")
infile = open(filename, 'r')
print(infile.read())
#Read lines from File
#Close File  
    
