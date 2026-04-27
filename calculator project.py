def calculator():
 while True:
  a=float(input("enter first number:"))
  b=float(input("enter second number:"))
  print("----calculator opeartion----")
  print("1.addition")
  print("2.subtraction")
  print("3.multiplication")
  print("4.division")
  print("5.power")
  print("6.modulus")
  
  choice=int(input("enter choice between(1-4):"))
  if choice==1:
    print("result:",a+b)
  elif choice==2:
    print("result=",a-b) 
  elif choice==3:
    print("result=",a*b)
  elif choice==4:
    if b!=0:
     print("result=",a/b)
    else:
      print("division by zero is not possible")
  elif choice==5:
    print("result:",a**b)
  elif choice==6:
        print("result:", a%b) 
  
  else:
     print("invalid choice!!")  

  c=input("Do you want to continue(y/n):")  
  if c.lower()!="y":
    print("calculator stopped")
    break

     
calculator()

  
