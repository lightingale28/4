"""A school has following rules for grading system: 
a. Below 25 - F 
b. 25 to 45 - E 
c. 45 to 50 - D 
d. 50 to 60 - C 
e. 60 to 80 - B 
f. Above 80 - A 
Ask user to enter marks and print the corresponding grade."""
x=int(input("Please enter your marks "))
if x<25:
    print("F")
elif 25<=x<45:
    print("E")
elif 45<=x<50:
    print("D")
elif 50<=x<60:
    print("C")
elif 60<=x<=80:
    print("B")
else:
    print("A")