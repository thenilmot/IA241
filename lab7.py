'''
lab 7
'''

#3.1
i=0
while i <= 5:
    if i !=3:
        print(i)
    i = i+1
    
#3.2
i= 1
x = 1

while i <=5:
    x= x * i
    i= i+1
print(x)    

#3.3
i= 1
x = 0

while i <=5:
    x= x + i
    i= i+1
print(x)    

#3.4
i= 3
x=1

while i <=8:
    x= x*i
    i= i +1
print(x)    

#3.5
i= 4
x=1

while i <=8:
    x= x*i
    i= i +1
print(x)    

#3.6
num_list = [12,32,43,35]
while num_list:
    num_list.remove(num_list[0])
print(num_list)