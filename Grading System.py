score=float(input("Enter your score:"))

if (score>=0 and score<=100): 
    if score >= 90:
        print("Grade:A")
    elif score >= 80:
        print("Grade:B")
    elif score >= 70:
        print("Grade:C")
    elif score >= 35:
        print("Grade:D")    
    else:
        print("Grade:F")            
else:
    print("Score must be between 0 and 100.")


      #OUTPUT

    """Enter your score:67
       Grade:D"""

  

