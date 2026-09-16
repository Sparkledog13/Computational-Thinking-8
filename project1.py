print("Welcome to Trivia!!")
print("Where we ask the hottest questions!!")
input("")
name = input("What is the name you would like to go by?")
print(f"Alright {name} lets get started")
input("")
answer1 = input("Question one!What are two things you can never eat for breakfast")
if answer1 == "lunch and dinner":
    print("Correct +10 points")
else:
    print("Wrong that was a tough one!")  
input("")
print("Next question!!")
answer2 = input("Question two! What gets wetter the more it dries")
if answer2 == "a towel":
    print("Correct! +10 points")
else:
    print("Wrong you'll gt  it next time! -10 points!") 
input("")
print("Next question")
answer3 = input("What is something you can break but never hold")
if answer3 == "a promise":
    print("Correct +10 points")
else:
    print("Wrong! -10 points!") 
input("")
print("Next question!!")
answer = input("Question 4. What two keys cant open a door?")
if answer == "a monkey and a donkey":
    print("Correct +10 points")
else:
    print("Wrong that was a tough one -10 points!") 
    input("")
    print("Last question!!")
answer = input("What is the meaning of life?")
if answer == "nothing":
    print("Correct +10 points")
else:
    print("Wrong man how do you not know the meaning of life??")
input("")
print("AAAAAAnd thats all folk! Make sure to add up all your points at the end!")
