def clac():
 while True: 
     num1 = float(input("enter the first number\n"))
     symbol = input("enter what you want to do + ,-,*,/,%\n")
     num2 = float(input("enter the second number\n"))
   

     if symbol== "+":
      print(f"result {num1 + num2}")
     elif symbol == "-":
       print(f"result{num1-num2}")
     elif symbol == "*":
       print(f"result{num1*num2}")
     elif symbol == "/":
       print(f"result{num1/num2}")
     elif symbol == "%":
       print(f"result{num1%num2}")
     else:
       print("invalid operation")
     result = input("do you want to restart yes / no\n")
     if  result != "yes":
      print("thank you ")
   
    
