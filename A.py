# if statement : based on condition : 1 situation : selection statement 

# 1. Check if the number is positive 
x = 10
if x>0:
    print(x, "is positive")

# 2. Check is first level is qulified

score = int(input("Enter your score :"))
if score>100:
    print("Hurrey...qualified")

# if - else : 2 situations
# 3. Check whether qualified or disqualified 

score = int(input("Enter your score :"))
if score>100:
    print("Hurrey...qualified")
else:
    print("Oops...Disqualified")

# 4. Check whether the number is odd or even 
n = int(input("Enter a number :"))
if n%2 == 0:
    print(n, "is even")
else:
    print(n, "is odd")

# 5. Display grade according to percentage, <33 : 'F', <50 : 'C', <70 : 'B', <90 : 'A', > = 90 : 'O'

per = int(input("Enter your percentage :"))
if per<33 :
    grade = 'F'
elif per<50 :
    grade = 'C'
elif per<70 :
    grade = 'B'
elif per<90 :
    grade = 'A'
else:
    grade = 'O'
    print("Result : ", grade, 'grade')

# 6. Check wheather the number is positive odd, positive even, negative odd, negative even

#nested if : if inside another if : a case inside another case

n = int(input("Enter a number :"))
if n>0 :
    if n%2 == 0:
        print(n, "is positive and even")
    else:
        print(n, "is positive and odd")
elif n<0:
    if n%2 == 0:
        print(n, "is Negative and even")
    else:
        print(n, "is Negative and odd")
else:
    print(n, "is zero")

