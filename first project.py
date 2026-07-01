num1=float( input( " write the first number"))
op = input("choose + , × , ÷ ,- , * ")
num2=float( input(" write the second number"))

if op == "+":
	print(num1+ num2)
elif op == "-":
	print(num1- num2)
elif op == "×" or op == "*":
	print(num1* num2)
elif op == "÷":
	if num2 == 0 :
		print("cannot divide on 0")
	else :
		print(num1/num2)
else:
    print("incorrect calculation")
