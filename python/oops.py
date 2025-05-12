# class student:
#     collegename="GLA University"
#     def __init__(self,name):
#         self.name=name
#         print("Adding new student in DataBase..")
    
#     def hello(self):
#         print("welcome",self.name)


# s1=student("karn")
# s1.hello()
# s2=student("arjun")
# s2.hello()


# class car:
#     color="blue"
#     model="qw1"
#     brand="Mercedes"


# class student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks

#     def average(self):
#         print(f"Hi! {self.name}, Your average of marks are {sum(self.marks)/3}")
    
#     @staticmethod #decorator
#     def hello():
#         print("hello")

# s1= student("Tony",[99, 86, 76])
# s1.average()

# s1.name="Mr.Stark"
# s1.average()
# s1.hello()

# abstraction== hiding the implementation details of a class and only showing the essential features to the user
# Encapsulation== Wrapping data and functions into single unit (object).

# class account:
#     def __init__(self,acc,bal):
#         self.balance=bal
#         self.accountno=acc

#     def debit(self,deb):
#         self.amount=deb
#         self.balance= self.balance - (self.amount) 
#         print(f"Rs. {self.amount} is debitted from your account {self.accountno}")
    
#     def credit(self,cred):
#         self.amount=cred
#         self.balance= self.balance + (self.amount) 
#         print(f"Rs. {self.amount} is creditted to your account {self.accountno}")
#     @staticmethod
#     def hello():
#         print('hello')

# acc1=account('cust1',12000)
# print(acc1.accountno)
# print(acc1.balance)
# acc1.debit(100)
# acc1.credit(200)
# acc1.credit(10000)
# acc1.debit(5000)
# acc1.balance





class student:
    def __init__(self,physics,chemistry,mathematics):
        self.phy=physics
        self.chem=chemistry
        self.math=mathematics
        self.percentage=str((self.chem +self.math +self.phy)/3)
    def get_percentage():
        pri


stu1=student(23,34,45)
print(stu1.percentage)










