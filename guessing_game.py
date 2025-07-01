import random
number=random.randint(1,10)
guess=0;
count=0
while(guess!=number):
  guess=int(input("Enter any number between 1 and 10: "))
  if(guess==number):
    count=count+1
    print("Correct Guess You Win!!" )
    break;
  elif(guess>number):
    print("Sorry, guess again.Too high ")
    count=count+1
  else:
    count=count+1
    print("Sorry, guess again. Too low ")
print("You took ",count,"chances to reach the correct no")
