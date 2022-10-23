# Given a list of numbers, find the sum of all the elements in the list.
a=[1,2,3,4,6,5]
b=0
for i in a:
  b+=i

print(b)

# Given a list of strings, find the longest string in the list.

a=['abc','adwe','dweweqw','abcdefghijklmnopqrstuvwxyz']
max_len=-1
for i in a:
  if len(i)>max_len:
    max_len=len(i)
    max=i

print(max)

# Given a list of numbers, create a new list that contains only the even numbers from the original list.
a=[1,2,3,4,5,6,7,8,9,10]
b=[]

for i in a:
  if i%2==0:
    b.append(i)

print(b)

# Given a list of strings, create a new list that contains only the strings that start with the letter 'a'.
a=['abc','apple','Arul','badwe','ceqw','dwdaw','AMG']
b=[]

for i in a:
  if i[0]=='a' or i[0]=='A':
    b.append(i)

print(b)

# Given a list of nested lists, create a new list that contains the sum of all the values in the nested lists.
#  (using recursion)
def sum_nestedlist(l):
    total = 0
    for j in range(len(l)):
        if type(l[j]) == list :
            total+= sum_nestedlist(l[j])
        else:
            total += l[j]  
             
    return total
             
print(sum_nestedlist([[1,2,3],[4,[5,6]],7]))

# Print a nested list

a=[[3.4,4],23,[3]]
print(a)

# Flatten a nested list
my_list = [[1], [2, 3], [4, 5, 6, 7]]

flat_list = []
for sublist in my_list:
    for num in sublist:
        flat_list.append(num)

print(flat_list)

# Convert a nested list to a string

my_list = [[1], [2, 3], [4, 5, 6, 7]]
flat_list = []
for sublist in my_list:
    for num in sublist:
        flat_list.append(num)

string=str(flat_list)

print(string)

