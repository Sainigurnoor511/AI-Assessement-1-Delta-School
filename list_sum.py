# Define a function that takes a list of
# numbers and returns the sum of these numbers
#
# Author: Gurnoor Singh Saini

list_of_num=[]

n = int(input("Enter number of elements :"))
print("Enter the elements :")

for i in range (n):
    x = int(input())
    list_num.append(x)

def sum_of_list(list_num):
    sum = 0
    for num in list_num:
        sum += num
    print("Sum :", sum)

sum_of_list(list_num)