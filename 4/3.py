"""Write a multiplication game program for kids. The program should give the player ten randomly generated multiplication questions to do.
After each, the program should tell them whether they got it right or wrong and what the correct answer is.
Question 1: 3 x 4 = 12
Right!
Question 2: 8 x 6 = 44
Wrong. The answer is 48.
...
...
Question 10: 7 x 7 = 49
Right."""
import random
for x in range(10):
    a1=[1,2,3,4,5,6,7,8,9,10]
    y1=random.choice(a1)
    y2=random.choice(a1)
    print (y1,"X",y2,"=")
    X1=int(input())
    if X1==y1*y2:
        print("Right!")
    else:
        print("Wrong. The answer is",y1*y2,".")