
# str =("This is a String.\nwe are creating it in python.")
# str1 =("This line used to learn tab.\tit's a tab func.")

# print(str)
# print(str1)


#CONCATE FUNCTION

#spaces and digits are also count in length
"""
str1 = "Shubhanshu"
str2 = "Patil"
#print(str1+str2)
print(len(str1))
print(len(str2))

"""

#INDEXING (starts with 0) with index we can access character but can not manipulate it

"""
str = "This tutorial is for indexing"
print(len(str))

print(str[28])
"""


#Slicing :- Accessing parts of a string
#ending index will not include

"""
str = "Apna college"
slice_part = str[1:4]
slice2 = str[5:len(str)]
slice3 =  str[5:]   #means index till length of str [5:len(str)]
slice4 = str[:4]    #means [0:4]
print(slice_part)
print(slice2)
print(slice3)
print(slice4)

"""


#Negative Index

"""
str = "Apple"
slc = str[-3:-1]
slc2 = str[-5:-1]
print(slc)
print(slc2)

"""

#str = " I am a Student"
#print(str.endswith("nt"))

# str = "i am shubhanshu"
# str = str.capitalize()
# print(str)


# str = " It's a winter season"
# print(str)
# str = str.replace("winter","Summer")
# print(str)

#str = "I am from studying python from ApnaCollege"
# print(str)
# print(str.find('o'))
# print(str.find('I'))
# print(str.count('a'))
# print(str.count("from"))


# str = str.replace('o','a')
# print(str)
# print(str.find("studying"))





#input users first name and print its length.
"""
name = input("Enter Your Name :")
print("Length of your name is :",len(name))
"""

#find the Occurence of $ in a string

"""
str = " This is a $ currency and $ is more superior the rupay"
print("Count of $ in a string is :" ,str.count('$'))
"""


#CONDITIONAL STATEMENTS

# light = "Look"

# if(light == 'red'):
#     print("Stop")
# elif(light=='green'):
#     print("Go")
# else:
#     print("Look")
#     print("End of code")
    


# marks = int(input("Enter the students marks: "))

# if(marks>=90):
#     grade = "A"
# elif(marks>=80 and marks<90 ):
#     grade = "B"
# elif(marks>=70 and marks<80):
#     grade = "C"
# else:
#    grade = "D"

# print("Grade of the Student: ",grade)   


#NESTING IN PYTHON

# age = int(input("Enter Your Age: "))

# if(age>=18):
#     if(age>=80):
#         print("cannot drive")
#     else:
#         print("can drive")
# else:
#     print("Cannot drive")


#Check if a number entered by user is odd or even

# num = int(input("Enter the number: "))

# rem = num%2

# if(rem==0):
#     print("Number is Even")
# else:
#     print("Number is Odd")



#Find the greatest of 3 numbers entered by users

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))

# if(a>=b and a>=c):
#     print("a is the greatest number")
# elif(b>=c):
#     print("b is the greatest number")
# else:
#     print("c is the greatest number")



#Find the greatest of 4 numbers entered by users

# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
# d = int(input("Enter the fourth number: "))

# if(a>=b and a>=c and a>=d):
#     print("a is the greatest number")
# elif(b>=c and b>=d):
#     print("b is the greatest number")
# elif(c>=d):
#     print("c is the greatest number")
# else:
#     print("d is the greatest number")




#Check if a number entered by users is multiply of 7

num = int(input("Enter the number: "))

mul = num%7==0

if(mul):
    print("its a multiple of 7")
else:
    print("Not a multiple of 7")