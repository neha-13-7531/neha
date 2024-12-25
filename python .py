#program for number which are divisible by 7 but not multiple  of 5
x=int(input("Enter the first value:"))
y=int(input("Enter second value:"))
for i in range(x,y+1):   #range function is used to find number in range
    if i % 7 ==0 and i % 5 !=0:
        print(i)
output:Enter the first value: 1
Enter second value: 200
7
14
21
28
42
49
56
63
77
84
91
98
112
119
126
133
147
154
161
168
182
189
196

# program forrotate element of a list (e.g[1,2,3,4] become a [4,1,2,3]
def rotate_list(x):
    if x:
        x.insert(0,x.pop()) #pop is used to remove last element in list
        return x
list=[1,2,3,4]
rotated_list=rotate_list(list)
print("rotated list is",rotated_list)
out put: rotated list is [4, 1, 2, 3]

#program for to merge two dictionaries summing the values of common keys
n={'maths':78,'sci':45,'geo':50}
m={'elex':88,'comp':90,'stat':70}
for key in m:
    if key in n:
        m[key]=m[key]+n[key]
    else:
        pass
print(m)
out put: {'elex': 88, 'comp': 90, 'stat': 70}
#fibonacci series upto n term
def fibo_seq(n):
    if n<0:
        print("enter number")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibo_seq(n-1)+fibo_seq(n-2)
print(fibo_seq(9))
output:34
#pyramid pattern using nested loop
x=int(input("Enter the number of rows"))
for i in range(1,x+1):  #i for rows
    for j in range(x - i): #j for column
        print(" ",end="")
    for k in range(2 * i - 1):   # for star print
        print("*",end="")
    print()
output:Enter the number of rows 5
    *
   ***
  *****
 *******
*********
#to count number of tralings zeros in the factorial of number
def zeros(n):
    count=0
    while n>=5:
        n//=5
        count += n
    return count

x=int(input("enter number"))
trailing_zeros=zeros(x)
print( f" the number of trailing zeros in {x}! is {trailing_zeros}")
output:enter number 5
 the number of trailing zeros in 5! is 1
#reverse the string without using built in function
my_string=("Good morning")
str=""
for i in my_string:
    str=i+str
    
print("Reversed string:",str)
output:
Reversed string: gninrom dooG
#Accept white space
def process_words():
    words=input("enter a sequence of whitespace separated word:") # accept input from user
    unique_sorted_words=sorted(set(words.split()))  # split the word and removing duplicate and sorting them
    print("         ".join(unique_sorted_words))
process_words()
output:enter a sequence of whitespace separated word: Neha Khushi Mohini
Khushi         Mohini         Neha
#find the 3 most common element in a list using a dictionary
def find_top_3_element(x):
    element_counts={}
    for elem in x:
        if elem in element_counts:
            element_counts[elem] += 1
        else:
            element_counts[elem] = 1

    sorted_elements=sorted(element_counts.items(),key=lambda y: y[1],reverse=True) # sort the element by count in descending order
    top_3_elements=sorted_elements[:3]  #get top 3 element
    return top_3_elements
sample_list=[6,3,8,5,9,5,5,2,3,3,3]
result=find_top_3_element(sample_list)
print(result)
output:
[(3, 4), (5, 3), (6, 1)]
#calculate the greatest common divisor(GCD) of two number using recursion
def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x%y)   #call the function
num1=50
num2=20
result=gcd(num1,num2)
print(f"The GCD of {num1} and {num2} is {result}.") 
output:
The GCD of 50 and 20 is 10.
#write a function to count the frequency of each character in a given string
def count_frequency(string):
    frequency = {}   #create empty dictionary to store charecter frequency
    for char in string:
        if char in frequency:
            frequency[char] += 1  # charecter is exits in the dictionary 
        else:
            frequency[char] = 1    # if not exits 
    return frequency
input_string="Good Morning"
result = count_frequency(input_string)
print(result)
output:
{'G': 1, 'o': 3, 'd': 1, ' ': 1, 'M': 1, 'r': 1, 'n': 2, 'i': 1, 'g': 1}
#write a prgram to read a csv file and print contents line by line
import csv
def read_csv_file(file_path):
    with open(file_path,mode='r') as file: # use open to open file and r mode for read file
         csv_reader=csv.reader(file)   #csv_reader to read the file content
         for line in csv_reader:
            print(line)
file_path='neha.csv'
read_csv_file("C:\\Users\\hp\\Downloads\\neha.csv")
output:
['name', 'marks']
['Anu', '90']
['neha', '88']
['moni', '75']
['khushi', '80']
#implement  a function to generate all permutation of a list
def generate_permutation(x):
    if len(x) <= 1:
        return [x]
    permutations = []
    for i in range(len(x)):
        current = x[i]
        remaning=x[:i] + x[i+1:]  # remaning list without the current element
        for permu in generate_permutation(remaning):# generate  permutation for reamning list
            permutations.append([current] + permu)  # append for add all permutation
    return permutations
input_list=[10,11,12,13]
result=generate_permutation(input_list)
print(result)
output:
[[10, 11, 12, 13], [10, 11, 13, 12], [10, 12, 11, 13], [10, 12, 13, 11], [10, 13, 11, 12], [10, 13, 12, 11], [11, 10, 12, 13], [11, 10, 13, 12], [11, 12, 10, 13], [11, 12, 13, 10], [11, 13, 10, 12], [11, 13, 12, 10], [12, 10, 11, 13], [12, 10, 13, 11], [12, 11, 10, 13], [12, 11, 13, 10], [12, 13, 10, 11], [12, 13, 11, 10], [13, 10, 11, 12], [13, 10, 12, 11], [13, 11, 10, 12], [13, 11, 12, 10], [13, 12, 10, 11], [13, 12, 11, 10]]
#generate a random dataset of integer and calculate the mean median and mode
import random 
from statistics import mean,median,mode  # import mean median and mode from statistics library
def generate_dataset(size,min_val,max_val): # generate random dataset
    return [random.randint(min_val,max_val) # use in a list comprehension to create a list of random integer
for _ in range(size)]
def calculate_statistics(data):
    try:
        mode_val=mode(data) # calculate mean,median,mode
    except:
        mode_value="No unique mode"
    return {
        'mean':mean(data),
        'median':median(data),
        'mode':mode_val
    }
dataset=generate_dataset(size=15,min_val=2,max_val=10)
print(f"Dataset:{dataset}")
stats=calculate_statistics(dataset)
print(f"Mean:{stats['mean']}")
print(f"Median:{stats['median']}")
print(f"Mode:{stats['mode']}")   
output:
Dataset:[2, 9, 7, 10, 5, 9, 8, 4, 6, 7, 8, 6, 2, 5, 2]
Mean:6
Median:6
Mode:2
