import csv
import pandas as pd

filename = "/Users/mac/Desktop/KriyaDocs/LearningExercises/CSV/annual-enterprise-survey-2021-financial-year-provisional-csv.csv"
 
# initializing the titles and rows list
fields = []
rows = []

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
 
    print("Total no. of rows: %d"%(csvreader.line_num))
 

print('Field names are:' + ', '.join(field for field in fields))
print('\nFirst 5 rows are:\n')
for row in rows[:5]:
    for col in row:
        print("%10s"%col,"")
    print('\n')

print('ROWS\n\n')
for i in rows:
    print(i)
# Writing to a CSV File
# field names
fields = ['Name', 'Branch', 'Year', 'CGPA']
 
# data rows of csv file
rows = [ ['LN', 'COE', '2', '9.0'],
        ['Sanchit', 'COE', '2', '9.1'],
        ['Aditya', 'IT', '2', '9.3'],
        ['Sagar', 'SE', '1', '9.5'],
        ['Prateek', 'MCE', '3', '7.8'],
        ['Sahil', 'EP', '2', '9.1']]
 
# name of csv file
filename = "/Users/mac/Desktop/KriyaDocs/LearningExercises/CSV/university_records.csv"
 
# writing to csv file
with open(filename, 'w') as csvfile:
    # creating a csv writer object
    csvwriter = csv.writer(csvfile)
     
    # writing the fields
    csvwriter.writerow(fields)
     
    # writing the data rows
    csvwriter.writerows(rows)



# Read a CSV file with name, number, street, city, state, pin and create a new file containing state, city,number of houses in the state/city into another CSV file

# Without Pandas
filename = "/Users/mac/Desktop/KriyaDocs/LearningExercises/CSV/example.csv"
fields = []
rows = []
 
with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    print("Total no. of rows: %d"%(csvreader.line_num))
    with open('createdAsPerRequest.csv', 'w') as new_file:
      field=['state','city','number']
      csvwriter = csv.writer(new_file)
      for row in csvreader:
        csvwriter.writerow((row[1],row[3],row[4]))

# Read a CSV file with name, number, street, city, state, pin and create a new file containing state, city,number of houses in the state/city into another CSV file



data = pd.read_csv('/Users/mac/Desktop/KriyaDocs/LearningExercises/CSV/example.csv')

# display
print("Original 'input.csv' CSV Data: \n")
print(data)

new_data=data
new_data.pop('name')
new_data.pop('street')
new_data.pop('pin')
# display
print("\nCSV Data after deleting the column 'year':\n")
print(new_data)
field=['state','city','number']
df = pd.DataFrame(new_data)
df.to_csv('pandasCreation.csv')

