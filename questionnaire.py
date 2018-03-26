print ("Hello! Welcome to my Questionnaire")
begin = input("Would you like to answer  ")
if begin =="yes":
     print("A) YES!")
     print("B) NO")
     question1 = input("Do you like Python? ")
     if question1 == "A":
         print("Well done , You have good taste")
         print("  ")
         
         print("A) Excellent!")
         print("B) Good")
         print("C) NO i don't")
         question2 = input("How is Python so far?  ")
         if question2 == ("A"):
             print("Stay Motivated!")
         elif question2 == ("B"):
             print("Good Job!")
         else:
                     question2 == ("C")
                     print("Motivate yourself! , Beacuse you are missing out")
     else:
         print("Oh sorry! You are missing out")
         print("  ")
         
         print("A) Excellent!")
         print("B) Good")
         print("C) NO i don't")
         question2 = input("How is Python so far?  ")
         if question2 == ("A"):
             print("Stay Motivated!")
         elif question2 == ("B"):
             print("Good Job!")
         else:
                     question2 == ("C")
                     print("Motivate yourself! , Beacuse you are missing out")

else:
    print("Thank you for your honesty , Goodbye:")
