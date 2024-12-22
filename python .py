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
