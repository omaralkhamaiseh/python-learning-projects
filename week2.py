import random 
def gussing_game():
 secretNum=random.randint(1,100)
 attempts=0
 print("Welcome to guessing game!!")
 while True:
  try:
        guess=int(input("Enter the answer you think its correct?(1/100)"))
        attempts=attempts+1
        if guess>secretNum :
          print("Its lower than your answer!")
        elif guess<secretNum:
         print("Its higher than your answer!")
        else:
          print(f"Correct answer! You got the answer at attempt number {attempts}")
          break
  except ValueError:
    print("Invalid input! Please type a number using digits (e.g., 5, 22).") 
  
if __name__=="__main__":
  gussing_game()