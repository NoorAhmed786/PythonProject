# a=10
# b=5
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(12//3) # 12/3=4 floor division
# print(10%3) # 10/3 = 3.3333... 3*3=9 10-9=1  modulus
# print(5**3) # 5*5*5=125 exponent

# # assignment operators  =, +=, -=, *=, /=, %=, //=, **= used to assign values to variables
# x=10
# x+=3
# print(x) # 13

# x=10
# x-=3
# print(x) # 7

# # comparison operators ==, !=, >, <, >=, x=3 <=    used to compare two values
# y=5
# print(x==y) # False
# print(x!=y) # True
# print(x>y) # False
# print(x<y) # True
# print(x>=y) # False
# print(x<=y) # True

# # logical operators and, or, not used to combine conditional statements

# x=3
# y=5

# print(x>2 and y>4) # True
# print(x>2 and y<4) # False
# print(x>2 or y<4) # True
# print(not x>y) # True  because x is not greater than y

# # membership operators  in, not in  its used to test if a sequence is presented in an object
# str1="Hello World"
# print("H" in str1) # True  it is case sensitive
# print("Hello" not in str1) # False

# l=[1,2,3,4,5]
# print(6 in l) # false
# print(6 not in l) # True  6 is not in list l



# # identity operators is, is not used to compare objects, not if they are equal, but if they are actually the same object, with the same memory location

# x=5
# y=5
# print(x is y) # True  because x and y are same object
# print(x is not y) # False  because x and y are same object

# # bitwise operators & , |, ^, ~, <<, >> used to compare binary numbers
# x=10
# y=4
# print(bin(x)) # 0b1010 # binary representation of 10
# print(bin(y)) # 0b0100 # binary representation of 4
# print(x&y) # 0  # 1010 & 0100 = 0000
# print(x|y) # 14 # 1010 | 0100 = 1110
# print(x^y) # 14 # 1010 ^ 0100 = 1110
# print(~x) # -11 # ~x = -x-1
# print(x<<2) # 40 # 1010 << 2 = 101000
# print(x>>2) # 2 # 1010 >> 2 = 109

# #====================== dAta types ======================
# # Text Type:	str
# a="Hello World"
# ab='''
# Hello
# World
# '''
# print(ab)
# print(type(a)) # <class 'str'>
# # Numeric Types:	int, float, complex
# a=5
# print(a,type(a)) # <class 'int'>
# b=5.5 
# print(b,type(b)) # <class 'float'>
# c=2+3j
# print(c,type(c)) # <class 'complex'>

# # Sequence Types:	list, tuple, range
# a=[10,"vs",23] # list is mutable
# a[1]=20 # list is mutable
# print(a,type(a)) # <class 'list'>

# b=(10,"vs",23) # tuple is immutable   fast as compared to list
# # b[1]=20 # tuple is immutable
# print(b,type(b)) # <class 'tuple'>


# c=range(10) # range is immutable
# print(c,type(c)) # <class 'range'>

# # Mapping Type:	dict
# a={"name":"vs","age":23} # key value pair
# print(a,type(a)) # <class 'dict'>
# print(a["name"]) # vs

# # Set Types:	set, frozenset
# a={10,20,30,10} # set is immutable
# print(a,type(a)) # <class 'set'>

# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview

#userinput input() function
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# print(a+b) # <class 'str'>
#=================== typecasting  ================== 
#   , converting one data type to another
#int
# a=int(input("Enter a number: "))
# b=int(input("Enter a number: "))
# print(a+b) # <class 'int'>
#float
# a=float(input("Enter a number: "))
# b=float(input("Enter a number: "))
# print(a+b) # <class 'float'>
#eval
# a=eval(input("Enter a number: "))
# b=eval(input("Enter a number: "))
# print(a+b) # <class 'int'> or <class 'float'>


#==================conditional statements==================
# a=int(input("Enter a number: "))
# if a%2==0:
#     print("Even")
# else:
#     print("Odd")

# a= int(input("Enter a number: "))
# if a>=70:
#     print("first division")
# elif a>=60:
#     print("second division")
# elif a>=45:
#     print("third division")
# else:
#     print("fail")

# ==================loops==================
# range
range(10) # 0 to 9 single parameter
range(1,10) # 1 to 9 double parameter
range(1,10,2) # 1,3,5,7,9 triple parameter
# 

# for loop
for i in range(10):
    print(i) # 0 to 9
for i in range(1,10):
    print(i) # 1 to 9
for i in range(1,10,2):
    print(i) # 1,3,5,7,9
    # table of 2
for n in range(1,11):
    print( "2" ,"X" ,n,"=", 2*n)

# reverse loop
# start, stop, step
for i in range(10,0,-1):
    print(i) # 10 to 1

# ==================while loop==================
i=1
while i<=10:
    print(i,"welcome")
    i+=1
    print(i)
a=10
while a>=1:
    print(a,"welcome reverse")
    a-=1
print(a)

# ==================string Indexing==================
# string indexing
w="welcome to noor"
print(w[0]) # w
print(w[0::1]) # welcome to noor
print(w[0::2]) # wloet or
print(w[0:7:1]) # wce n

# reverse string
print(w[-1::-1]) # roon ot emoclew
print(w[-1::-2]) # rntmcew

# ================== string iteration==================

for n in w:
    print(n)
l=len(w)
for n in range(l):
    print(w[n])

for m in range(l-1,-l-1,l-1):
    print(w[m])

# ==================string methods==================
# capitalize
cap="welcome to noor"
c=cap.capitalize() # Welcome to noor
print(c)

l=cap.lower() # welcome to noor
print(l)

u=cap.upper() # WELCOME TO NOOR
print(u)

t=cap.title() # Welcome To Noor
print(t)

num="123445"
print(num.isdigit())

num2="noor"
print(num2.isalpha())

num3="noor123"
print(num3.isalnum())
print(num3.find("o",2))
print(num3.index("r",2))
