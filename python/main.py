# shortcutkeys @vs code
# ctrl + / == mass commentout
# alt + up-down keys == shifting the line 
# alt + shift + up-down keys == copying that line in yplane
# F5 == debug and Run
# alt + click == selecting words and editing them at once

# easter egg of python(ZEN of Python)

# import this #run it
# Types of programming:
# Blockcoding
# Procedural Programming
# Functional Programming
# Object Oriented Programming

# imp. topics array
# difference transformation use of tuple,dictionary,list,string,array
# ennnumerate learn
# virtual environment


# python is interactive,interpreted,object oriented programming language,highly readable.
# oops(technique of programming that incapsulates code within objects)
# python was developed by guido van rossum in late 80s or early 90s at the national reserch institute for mathematics and computer science, netherlands
# features of python: easy to(learn-read-maintain),gui programming scalable, standard broad library,interactive mode.

# there are certain predefined keywords in python
# import keyword
# print(keyword.kwlist)


# first python program
# print("Hello, Python!")

# identifiers
# they are made up of alphabets(uppercase and lowercase), numbers(0-9) and a underscore.
# starting an identidier with a leading single underscore indicates that the identifier is private 
# starting an identidier with a leading single underscore indicates a strongly private identifier.
# if it also ends with with two trailing underscores, this identifier is a language defined special name


# multi line statements(/)
# denotes that line should continue. for eg:
# tom= tom1+\
#     tom2+\
#         tom3+\
 
 
# lines and indentation
# python uses no type of braces to indicate blocks of code, class or function intead they are seperted by the use of indentation.
# the no. of space in indentation is variable, but all statements within the block must be indented the same amount.


# Data Types(number[int,float,lon,complex],string,list,tuple,dictionary)
# a=1 #variable
# b="harry" #string 
# c= True #boolean
# d=None 
# print(a, b, c, d)
# print(type(a))



#  comment out ing we can write the working of the code here
# print("Hello\n World")
# print("hey",6,7,sep="~",end="009\n")



# typecasting
# a="4"
# a="2"
# b="4"
# print(a+b)
# to# error while
#  solve it we use ttype cast
# print(int(b) + int(a))



# userinput
# input function
# a= input()
# print("My name is ", a)
# input() it stores input in a string. use typeast to store specific datatype

# types of operators:
# 1. arithmetic operators +,-,*,/,//,**,%
# 2. comparision operators  <>, >, <, >=, <=, ==, !=
# 3. assignment operators  =,+=,-=,*=,/=,%=,**=,//=,
# 4. logical operators and, or, not
# 5. bitwise operators &,|,^(XOR),~(ones complement),<<,>>
# 6. membership operators in, not in{{let x be a list of n variables, if x has element a it will give ouput one is [if(a in x): print("1")]}}
# 7. identity operators is, is not (can be used to compare as either the two variables are equal or not)

# Exercise-1 (calculator-performing of different mathmatical operations)
# a= input()
# b= input()
# print(a+b)
# print(a-b)
# print(a*b)
# print(a**b)
# print(a/b)
# print(a//b)
# print(a%b)
# x= int(a)
# y= int(b)
# print(x+y)
# print(x-y)
# print(x*y)
# print(x**y) #power of function
# print(x/y) #provied ans in float
# print(x//y) #provide ans in int form floor division
# print(x%y) #provides remainder
# print("the value of", a, "+", b, "is:", a+b )


# import sys
# print( 'number of arguments:',len(sys.argv), 'arguments.')
# print('argument list:', str(sys.argv))




#more about strings from basics
# ('single quoted string')("double quoted string for writing string in a line")('''triple quoted string for writing string in paragraph format''')


# apple='''he said, "hiharrry!
# tum kaise ho i gusee sb thik hoge'''
# print(apple)
# nm="he!!Man!!go!!"
# print(type(apple))

# #slicing in string
# #strings are immutable 
# print(apple[0:12])
# print(len(apple))
# print(nm[:-4]) # 0: len(apple)-4
# print(nm[-4:-2])
# print(apple[0])
# print(apple+'test')
# print(apple*2)

# #how to play with case
# #capitalize changes all to lower and the first letter in string to uppercase
# print(nm.upper(),"\n", nm.lower(),"\n",nm.capitalize())

# # use of rstrip is to remove the letter. .replace can be ctrl+r, 
# # and split function can divide the string from the letter or word mentioned and print the splitted output
# print(nm.rstrip("!"))
# print(nm.replace("Man","Woman"))
# print(nm.split("!!"))

# print(nm.count("!"))
# print(nm.endswith("!!")) #output in boolean datatype
# print(nm.endswith("go",4,11))
# print(nm.startswith("!!")) #output in boolean datatype
# print(nm.startswith("go",4,11))
# find only gives first output
# print(nm.find("go"))
#print(nm.index("ish"))
#nm.index("ish") # iff sure of occurance 

#conditions checkers and answeres in boolean [true,false]
# n="cm.;'; o3ev\n"
# an= "rajurastogi123"
# a= "RajuRastogi"
# q="     "
# s= "Gantavya Bansal Is Not A Good Bboy"
#isalnum()= if the given string is alpha numeric then print it..condition A-Z;a-z;0-9}
#islapha()= same as above ... conditions A-Z;a-z}
# print(n.isalnum(),an.isalnum())
# print(an.isalpha(),a.isalpha())
# print(a.islower(),a.isupper())# true if all letters are between a-z; true if all letters are between A-Z;

# only prints if everthing is printable
# print(n.isprintable(),a.isprintable())
#prints true only if there are white spaces in dtring
# print(n.isspace(),q.isspace()) 
# istitle prints true if only first letter of word is capitalised
# print(n.istitle(), s.istitle())
# print(a.swapcase()) #changes upper to lower and vice versa (+-)32 gamefunction
# print(an.title()) #converts string to title i.e capitalizing first etter of a word


# Python- Decision m=Making
#if-else statements
#conditional operators >, <, >=, <=, ==, !=
# a= int(input("Enter your age:"))
# print(a==18)
# print(a!=18)
# print(a>=18)
# print(a<=18)
# print(a>18)
# print(a<18)
# print("your age is:", a)
# # NOTE **if condition is matched it will not move further
# if(a<18): 
#     print("underage")#this space is caled indentation
# elif(a==18): #else if hi hai
#     print("dekh kr chlaiyo beti")
# else: 
#     print("enjoy")



#nested if-else statements
# a= int(input("Enter your Marks:"))
# if(a==33):
#     print("just pass")
# if(a<33):
#     if(a>30):
#         print("can be promoted")
#     elif(a>20):
#         print("fill compartment")
#     else:
#         print("year back")
# if(a>33):
#     if(a<40):
#         print("need to work hard")
#     if(a<50):
#         print("can do better")
#     elif(a<60):
#         print("some more effort")
#     elif(a<70):
#         print("B")
#     elif(a<80):
#         print("+B")
#     elif(a<90):
#         print("A")
#     elif(a<100):
#         print("+A")
#     else:
#         print("O=Outstanding")



# Exercise-2 (greet according to time)
# import time
# print("Real Time is:")
# #to print real time
# timestamp = time.strftime('%H:%M:%S')
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
 
# a = int(time.strftime('%H'))
# if(a<12):  print("Good Morning!")
# elif(a<16):print("Good Afternoon!")
# elif(a<20):print("Good Evening!")
# elif(a<24):print("Good Night!")



#match case statements
# x= int(input("Enter the value of'x':"))
# match x:
#     case 0:
#         print("x is 0")
#     case 1:
#         print("x is 2")
#     case _ if x!=80:
#         print("not 80") #default case ony gets matched only if none of above case is matched
#     case _ :
#    
# 
# 
# print(x)





# message= 45
# print(message)
# print("message")

#loops statement
# for loops
# colors= ["Red","Green","Yellow","blue"]
# for color in colors:
#     print(color)
#     for i in color:
#         print(i)
        
# for k in range(10):
#     print(k)# always takes n-1 for eg; if k = 10 ans is 0,1,2,3,4,5,6,7,8,9
# for k in range(100):
#     print(k+1)
# for k in range(10,20):
#     print(k)
# for k in range(1,20,3):# k+=3 
#     print(k)

# #while loop
# count=0
# while count<9:
#     print(count)
#     count+=1
# for i in range(3):
#     print(i)
    
# i=0
# j=-9
# while(j<0):
#     print(i)
#     i=i+1
    
#break and continue statements
# for i in range(12):
#     print(5*i)
#     if(i==10):
#         break
   
# for i in range(12):
#     if(i==10):
#         print("iteration skipped for:",i,)
#         continue
#     print(5*i)

# break, continue, pass statements

# var=10
# while var>0:
#     if var==5:
#         break
#     print(var)
#     var-=1
# while var>0:
#     if var==5:
#         continue
#     var-=1
#     print(var)
    
    
#functions use 
# def calculategmean(x,y):
#     mean = (a*b)/(a+b)
#     print(mean)
    
# def isgreater(a,b):
#     if(a>b): print(a," is greater than ",b)
#     elif(a<b): print(a," is lesser than ",b)
#     else: print("both are equal")

# a=9
# b=8
# calculategmean(a,b)
# isgreater(a,b)
# c=7
# d=12
# calculategmean(c,d)
# isgreater(c,d)
# e=9
# f=9
# calculategmean(e,f)
# isgreater(e,f)

#function arguements
#dictionary and tupple, requirwd argument(return)


#Lists {represented as lists=[a,b,c,d]}
# + sign concatenate two list
# * sign repetition operator

# moj=[1,2,3,4,5,6,7,8,9]
# print(moj)
# print(moj[0])
# print(moj[3])
# print(type(moj))
# print(moj[:])
# print(moj[1:-1])
# print(moj[1:7:2])

#methods to manipulate lists
# list = [11,3,47,8,2,68,46,257,1436,1257]
# print(list)
# list.append(34) #used to add variables
# print(list)

# list.sort() #ascending order sorting
# print(list)
# list.sort(reverse = True) #descending order sorting
# print(list)
# list.reverse() #reverse the order of list
# print(list)

# print(list.count(34)) #no. of times 34 is repeated
# mist =list.copy() #copies the list
# print(mist)
# print(list.index(3))
# print(list)
# list.insert(1,56) #add element 56 on the index 1 provided
# print(list)

#ways to concatinate
# kist= list+ mist
# print(kist)
# list.extend(mist) #extend just merges two list and stores the values in the one same cas concanating
# print(list)



#tuple datatype unmutable(representation)
# slicing is possible 
# concatination is possible
# tup = (1,2,34,36,690,7,)
# print(type(tup),tup)
# if 34 in tup:
#     print("Yes")
#     tup2 = tup[1:5]
# print(len(tup2),tup2)

# operations in tuple or manipulation(THESEARE immutable)
#usual way to count and indexing
# res = tup.index(36,2,5) #2,5 is the range to search in between
# print(res)
# print(len(tup))



#Exercise-3 (Kaun Banega crorepati) (Pending Project)

# def form():
#     name = input("Enter your name:")
#     age = input("Enter your age:")
#     gender = input("Choose your gender M/F/?:")
#     locationa = input("Enter your country:")
#     locationb = input("Enter your state:")
#     locationc = input("Enter your City:")
#     print("Kindly confirm your details\n",name,age,gender,locationa,locationb,locationc)
#     confirm= input("Y/N")
#     if(confirm!="Y"):
#         form()
   
# def kbc_lifelines():
#     l= int(input("choose lifeline from below:\n\n",dic.items()))
#     match l:
#         case 1: 5050()
#         case 2: phone_a_friend()
#         case 3: Audience_Poll()
#         case 4: Switch_the_Question()
#         case 5: Ask_the_Expert()
#     dic.pop(l)

# def call_lifelines():
# def question1():
#     print
    
# def call_question():
    # ans=int(input((queslib[i],)))
    # if(ans=0):
    #     kbc_lifelines()

    
# def winamount():
#     if(levels[i+1]<5000):return 0
#     if(levels[i+1]<10000):return 5000
#     if(levels[i+1]<25000):return 10000
#     if(levels[i+1]<100000):return 25000

# #main code
# # l=0
# # i=0
# print("Welcome to Gantavya's KBC\n\n input your basic details")
# form()

# print(" 1: 50_50\n 2: Phone_a_Friend\n 3: Audience_Poll\n 4: Switch_the_Question\n 5: Ask_the_Expertpress\n\n\t press(1)(2)(3)(4) to choose answer\n\t (0) for lifelines\n\t (9) to exit the game")
# input("press enter to start the quiz")
# print("\n\n")
# dic={
#          1:"50_50" ,
#          2:"Phone_a_Friend",
#          3:"Audience_Poll",
#          4:"Switch_the_Question",
#          5:"Ask_the_Expert" 
        
#          }
# questionbank=[["who is king","(1) wazir","(2) raja","(3) rani","(4) salim"],
#               ["who is king","(1) wazir","(2) raja","(3) rani","(4) salim"],
#               ["who is king","(1) wazir","(2) raja","(3) rani","(4) salim"],
#               ["who is king","(1) wazir","(2) raja","(3) rani","(4) salim"],
#               ["who is king","(1) wazir","(2) raja","(3) rani","(4) salim"],
#               ["who is king","(1) wazir","(2) raja","(3) rani","(4) salim"]]
# correctanswers=["raja","raja","raja","raja","raja","raja"]
# levels=[0,1000,2000,3000,5000,10000,15000,20000,25000,50000,100000]

# for i in range (0,len(questionbank)):
#     print("question for rs.",levels[i+1],"\n\n\n",questionbank[i])
#     ans= int(input())
#     if(ans==0):
#         print("lifeline called")
#         print("")
#     elif(ans==1):
#         print("you won rs.",levels[i+1])
#     elif(ans==9):
#         print("you took an exit from game with a rize money of",levels[i])
#         break
#     else:
#         print("thank you for playing")
#         winamount()
#         break





# #fstrings
# name= "Gantavya"
# lname="Bansal"
# college="glau"
# fname= f"My name is {name}{lname} from {college}"
# print(fname)



#Docstrings_  inshort a printable comment used to define a function
# def square(n):
#     '''takes a n and return square of n'''
#     print(n**2)
# square(5)
# print(square.__doc__)



#Recursion(function calling a function)
# def factorial(n):
#     if(n==0 or n==1): return 1
#     else: return n *   factorial(n-1)
    
# print(factorial(5))

# #fibonacci series
# def fibonacci(n):
#     return fibonacci(n-1)+ fibonacci(n-2)

# print(fibonacci(2))



#sets
# ex= {22,5,46,7,4,2,667,1,43,13,5,2,34,46}
# fex= {46,367,47,4,33,65,8,4,2,4635,7,5,3,25,7,6,6444446,53,7,14,5568,5}
# print(ex)
# print(type(ex),len(ex))

# print(ex.union(fex))
# ex.update(fex) #update = save + union
# print(ex)
# print(ex.intersection(fex))
# ex.intersection_update(fex) #update = save + intersection
# print(ex)

# print(ex.symmetric_difference(fex))#symmetric difference{(ex U fex)-(ex A fex)}
# ex.symmetric_difference_update(fex) #symmetric difference{(ex U fex)-(ex A fex)}
# print(ex.isdisjoint(fex)) #no common vaalues non intersecting
# print(ex.issuperset(fex))
# print(ex.issubset(fex))

# ex.add("hello")
# print(ex)
# ex.update(fex)
# print(ex)x
# ex.remove("hello") #raises error if false
# print(ex)
# ex.discard(fex)
# print(ex)
# print(ex.pop()) #ops a random value from set
# del ex #deletes a set
# print(e)



#dictionary{hash table type}
# dic={
#     "run": "activity",
#     "gantavya": "coder",
#     "dhruv": "man",
#     #Employee ids
#     112:"harry"
# }
# print(dic["dhruv"])
# print(dic.get("dhruva"))#does not give error
# print(dic.keys())
# print(dic.items()) 

# ep1={122:34, 344:23,345:67,325:56}
# ep2={345:56,675:56}

# ep1.update(ep2)
# print(ep1)
# ep1.clear()
# print(ep1)
# ep1.popitem()
# print(ep1) #removes the last dic item
# print(ep1.popitem()) #prints the last dic item





# ERROR Handling/ Exception Management
# try: 
#     a= int(input("Enter the value:"))
#     for i in range (10):
#         print((i+1)*a)
#     else: print("hogya bas")
# except ValueError:
#     print("value is incorrect")
# finally: #this will get always executed doesnt get affected by break statements or return in functions
#     print("by dhruv")



# Raising custom errors
# a= int(input("Enter the value between 5 to 9:"))
# if(a<5 or a>9):
#     raise ValueError(" value is not between 5 to 9")
# print(a)



#Exercise-4 (secret code language)
# input("code or decode")
# sen=input("enter the response")
# sen="harry is good"
# words= sen.split(" ")
# nwords=[]
# for word in words:
#     if(len(word)>2):
#         r1="rjs"
#         r2="fhr"
#         nword= r1+ word[1:] + word[0] +r2
#         nwords.append(nword)
#     else: nwords.append(word)
# print(" ".join(nwords))




# sen=input("Enter the response:  ")
# words= sen.split(" ")
# coding=int(input("1 or 0 "))
# nwords=[]
# if(coding==1):
#     for word in words:
#         if(len(word)>2):
#             r1= "asd"
#             r2= "fgh"
#             nword= r1+ word[1:]+word[0]+r2
#             nwords.append(nword)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))


# elif(coding==0):
#     word=sen.split(" ")
#     nwords=[]
#     for word in words:
#         if(len(word)>2):
#             r1= "asd"
#             r2= "fgh"
#             nword= word[3:-3]
#             nword= word[-1]+ word[:-1]
#             nwords.append(nword)
#         else:
#             nwords.append(word[::-1])
#     print(" ".join(nwords))
        
# else: print("calculation error")






















# print(sen)
# print("hello")
# #short hand if else
# a=1342
# b=0
# print("A") if a>b else print("B") if b>a else print("=")
# importing
# import pandas
# pandas.read_csv()
# import math
# print(dir(math),math.nan)
# math.floor(4.23)
# from math import sqrt,pi
# # print(sqrt(9)*pi)

# def welcome():
#     print("goood morning mf")

# print("hello")
# welcome()
# if __name__=="__main__":
#     welcome()



# # OS Module
# import os
# os.mkdir("data0")
# # power to create 100 folders in a sec.
# for i in range(0,100):
#     os.mkdir(f"data0/test{i+1}")
# for j in range(0,100):
#     os.rename(f"data0/test{j+1}",f"data0/sample {j+1}")
    
# for k in range(0,100):
#     for l in range(0,100):
        # os.mkdir(f"data0/sample {k+1}/code {l+1}")

# folders= os.listdir("data0")
# print(folders)



# local vs global variable



#file i/o handling
# f= open('myfile.txt','a')
# print(f)
# print(f.read())# reading a file
# f.write("hello ")#clears all previous and then writes
# f.write("hello ")#append writes after previous
# f.close()

# other way
# with open('myfile.txt','a') as f:
#     f.write(" Hey! I am your Master")

#use of readline
# i=0
# f= open('myfile.txt','r')
# while True:
#     i+=1
#     line=f.readline()
#     if not line:
#         break
#     m1=line.split(",")[0]
#     m2=line.split(",")[1]
#     m3=line.split(",")[2]
#     print(f"mark of student {i} is {m1} in maths, {m2} in english and {m3} in hindi")
#     m=(int(m1)+int(m2)+int(m3))/3
#     print(m)
#     print(line)
    
#use of writelines()
# f= open('myfile.txt','w')
# lines=["line3\n","line2\n"]
# f.writelines(lines)
# f.close()

# #use of seek()
# f= open("myfile.txt","r")
# print(type(f))
# f.seek(10) # move the current position to 10th character
# print(f.read(5))#then it will read 5 characters

# use of tell()
# tells till what seek is used
# print(f.tell())

# use of truncate()
# only takes the n bytes from eritten characters
# with open('myfile.txt','w') as f:
#     f.write("hello world")
#     f.truncate(7)
# with open('myfile.txt','r') as f:
#     print(f.read())



# lambda functions
# def double(x):
#     return x*2

# cube = lambda x: x**3# by lambda
# print(cube(5))
# avg= lambda x,y,z: (x+y+z)/3
# print(avg(2,1,3))



#map filter reduce in python

# def cube(x):
#     return x**3
# l= [1,2,3,4,5,6,7,8,9]
# newl=[]
# without map function
# for item in l:
#     newl.append(cube(item))

# newl= list(map(cube,l)) #use of map
# print(newl)

# use of filter
# def filter_function(a):
#     return a>4
# newnewl=list(filter(filter_function,l))
# print(newnewl)

# use of reduce
# from functools import reduce
# num=[1,2,3,4,9,5,6,7,8]
# sum= reduce(lambda x,y:x+y, num)
# print(sum)



# is vs == keyword( both are comparision operators)
# Ewxercise-5 (snake water gun)
# print("rock paper scissor")
# p1=0
# p2=0 
# p3=1
# for i in range(100):
#     if(p1==5 or p2==5):
#         break
#     else:
#         print(f"points of player 1 is {p1} and player 2 is {p2}")
#         a= input("input for player A")
#         b= input("input for player B")
#         if(a=='r'):
#             if(b=='p'):
#                 p2+=1 
#             if(b=='s'): 
#                 p1+=1 
#         if(a=='p'):
#             if(b=='r'): 
#                 p1+=1 
#             if(b=='s'): 
#                 p2+=1 
#         if(a=='s'):
#             if(b=='r'): 
#                 p2+=1 
#             if(b=='p'):
#                 p1+=1  
    
# if(p1>p2): print(f"player 1 is winner \np1: {p1} and p2: {p2}")
# elif(p1<p2): print(f"player 2 is winner \np1: {p1} and p2: {p2}")
# else: print("ek match aur khelte hai")




# 
# 
# END of Procedural(Functional) Programming
# START of Object Oriented Prgramming
# 
# 
# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
        
#     def avg(self):
#         print(sum((self.marks))/3)




# a=student('karan',[98,99,97])
# a.avg()

# OOPS(features:- encapsulation,inheritance)


# class and objects
# class person():
#     name= 'Harry'
#     occupation= 'accountant'
#     networth= '10M'
#     def info(self):
#         print(f"{self.name} is a {self.occupation} with a networth of {self.networth} US dollars")
# a=person()
# b=person()
# a.name='Dhruv'
# a.occupation='hacker'
# print(f"{a.name} is a {a.occupation}")
# print(f"{b.name} is a {b.occupation}")
# a.info()
# b.info()



# constructors
# class person():
#     def __init__(self,n,o):
#         print("Hey I am an OP hacker")
#         self.name=n
#         self.occupation=o
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")
        
# a=person("harry","developer")
# b=person("divya","hr")
# a.info()
# b.info()



# Decorators
    
# def greet(fx):
#     def mfx(*args,**kwargs):
#         print("Good Morning")
#         fx(*args,**kwargs)
#         print("Thanks for using this functions")
#     return mfx
    
# @greet
# def hello():
#     print("Hello World")
    
# def add(a,b):
#     print(a+b)        
        
        
# hello()
# greet(add)(1,2)



# Getters and setters

 





# OOPs
# def scope_test():
#     def do_local():
#         spam = "local spam"

#     def do_nonlocal():
#         nonlocal spam
#         spam = "nonlocal spam"

#     def do_global():
#         global spam
#         spam = "global spam"

#     spam = "test spam"
#     do_local()
#     print("After local assignment:", spam)
#     do_nonlocal()
#     print("After nonlocal assignment:", spam)
#     do_global()
#     print("After global assignment:", spam)

# scope_test()
# print("In global scope:", spam)







# constructor
# class person:
#     def __init__(self,n,o):
#        print("Hey")
#        self.name=n
#        self.occ=o
    
# a=person("Harry","dev.")
# print(a.name)

# Decorators
# def greet(fx):
#     def mfx(*args,**kwargs):
#         print("Welcome in the interface")
#         fx(*args,**kwargs)
#         print("thanks for using the function")
#     return mfx

# @greet
# def hello():
#     print("Hello")

    
# @greet
# def add(a,b):
#     print(a+b)
    
# hello()
# add(2,4)





# getters setters


# class myclass:
#     def __init__(self,value):
#         self._value=value
#     def show(self):
#         print('value is', self._value)
#     @property
#     def tenvalue(self):
#         return 10*self._value
    
# obj = myclass(10)

# obj.show()
# print(obj.tenvalue)
# print(obj._value)
# print(obj.value)
  
# print(obj.__dir__()) 
# print(obj.__init__())

# class User:
#     def __init__(self,name,company):
#         self.name = name
#         self.company = company
#     def changename(cls,newc):
#         cls.newc = newc

# x = (1,2,3,4)

# print(dir(x))
# print(x.__add__)



# from typing import Any


# class employee:
#     def __init__(self,name):
#         self.name=name

#     def __len__(self):
#         i = 0
#         for a in self.name:
#             i= i + 1
#         return i
    
#     def __str__(self):
#         return f"the method str is verified successfully. {self.name}"
#     def __repr__(self):
#         return f"the method repr is verified successfully. {self.name}"
#     def __call__(self):
#         print("hello called")


# hello = employee("dhruvler")
# print(len(hello))
# print(hello)
# hello()
# print("hello")
# class animal:
#     def __init__(self,name,color,legs,type):
#         self.name = name
#         self.legs = legs
#         self.color =color
#         self.type = type

#     def show(self):
#         print(f"""
#         {self.name}
#         {self.legs}
#         {self.color}
#         {self.type}

# """)
        
# class dog(animal):
#     def __init__(self):



# a = True
# print(a:=False)

# a=[1,2,3,4,5]
# while(n:=len(a))>0:
#     a.pop()
#     print(a)
# print('done')


# import shutil

# shutil.copy("python\main.py","main2.py")
# shutil.copytree("project")

# print(shutil.__all__)

import selenium









































































# Inheritence

# class employee:
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
        
#     def showdetails(self):
#         print(f"{self.name}'s id is:{self.id}")
        
# e= employee("DHruv",4203)
# f= employee("euv",4203)
# e.showdetails()
# f.showdetails()

# city=input()
# if city.isalnum():
#     print('yes')
# else:
#     print('no')

# class player:
#     def __init__(self,health,power,wealth):
#         self.health=health
#         self.power=power
#         self.wealth=wealth

# class railwayform:
#     def __init__(self,name,age,gender,train):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         self.train=train
    
#     def status(self):
#         print(f"form filled sucessfully for {self.name}")
    
#     def show_passenger_details(self):
#         print(f'''Name: {self.name}\nAge: {self.age}\nGender: {self.gender}\nTrain no.: {self.train} ''')

# name=input("Enter your fullname here:")        
# age=int(input("Enter your Age"))        
# gender=input("Gender {M/F}:")        
# train=input("Enter your train number:")        
# p1=railwayform(name,age,gender,train)
# p1.status()
# p1.show_passenger_details()

# Constructors

    
    
    
    
    
    










    
    
    
    
    
    
    
    
    