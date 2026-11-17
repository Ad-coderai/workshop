#to print list of keyword
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist))  
print() 

 #to show address
'''a=10
print(id(a))'''

'''#multi variable
a,b,c = 10,20,30
print()
print("address of a : "+str(id(a)))
print("address of b : "+str(id(b)))
print("address of c : "+str(id(c)))'''

'''#cheking id
a=60
b=40
a=10
print()
print(a)
print(b)
print("address of a : "+str(id(a)))
print("address of b : "+str(id(b)))'''

'''#indexing
a="happy father's day"
print(a[-6])'''

'''a=(10)
print(type(a))'''

'''print()
z="idnia is best"
print(z[7:1:-1])'''


'''print()
s="good morning good afternoon"
print(s[-14:-23:-2]) #index at a pattern'''

'''print()
print("checking whether thee input is a tuple or not")
print()
s=eval(input("enter the string"))
print(type(s))
if(type(s)==tuple):
    print("its a tuple")
else:
    print("its not")'''

'''print()
print("checking for a palindrome")
z=input("enter a string: ")
if(z[::1]==z[::-1]):
    print("palindrome")
else:
    print("not a palindrome")'''


'''print()
print("checking whether uppercase or lowercase")
p=input("enter a charecter")
if('A'<= p<'Z'):
    print("uppercase")
else:
    print("lowercase")'''

'''m=int(input("enter a digit"))
if(10<= m <=99):
    print("its a two digit number")
else:
    print("its not a two digit number")'''


'''print()
#checking whether its a uppercase lowercase a number or a special charecter
d=input("enter: ")
if('A'<= d<='Z'):
    print("uppercase")
elif('a'<=d<='z'):
    print("lowercase")
elif('0'<=d<='9'):
    print("its a number")
else:
    print("its a special charecter")'''

'''h=eval(input("enter a list : "))
if(type(h)==list):
    if(len(h)%2==0):
        print("length of the list is even")
    else:
        print("length of the list is odd")
else:
    print("enter a list")'''


'''i=1
while(i<=5):
    print(i)
    i=i+1'''


'''list=[23,43,76,99,11]
i=0
while(i<5):
    print(list[i])
    i=i+1'''


'''n=int(input('enter : '))
rev=0
while n>0:
    id=n%10
    n=n//10
    rev=rev*10+id
print(rev)'''


'''w=input("enter a charecter")
out=''
for ch in w:
    if('A'<=ch<='Z'):
        out=out+chr(ord(ch)+32)
    else:
        out=out+chr(ord(ch)-32)
print(out)'''

'''for i in range(1,6):
    for j in range(1,6):
        print('*',end='')
    print()'''


'''for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()'''


def convert(s):
    out=''
    for ch in s:
        if('A'<=ch<='Z'):
            out=out+chr(ord(ch)+32)
        else:
            out=out+chr(ord(ch)-32)
    return out

print(convert("Happy fathers day"))



