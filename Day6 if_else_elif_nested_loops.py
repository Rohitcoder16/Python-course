#a= int(input("Enter your age:"))
#print("Your age is:",a)
#f a>=18:
 #   print("you can drive")
#else:
 #   print("you cannot drive")

#a = int(input("enter your age :"))
#print("your age is:",a)
#if a>18:
 #   print("you can drive")
#elif a==18:
 #   print("You are eligible to drive and apply to driving licence ")
#elif a<18 :
  #  print("you cannot drive ")
#else:
 #   print("invalid age enter correct age ")

num = int(input ("Enter a Number:"))
if (num<0):
    print("Negative number")
elif(num>0):
    if(num<=10):
        print("nuber is between 1 to 10")
    elif (num<=20):
        print ("number is between 11 to 20")
    else:
        print("number is graeter than 20")
else:
    print("Number is Zero")