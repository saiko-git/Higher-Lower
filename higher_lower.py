# -*- coding: utf-8 -*-
"""
Created on Sun Jul 20 13:25:09 2025

@author: ahmed amr ahmed khalil
"""
###higher lower
#you will need a dictionary (player,followers,brief desciption,his origin)
# randomly choose two people(keys) to compare between them according the no of followers
#continue until a certain limit or the player loses
import random
people = {
    "Albert Einstein": ["A German theoretical physicist known for the theory of relativity", 95],
    "Leonardo da Vinci": ["An Italian Renaissance artist, inventor, and polymath", 92],
    "Elon Musk": ["A South African entrepreneur and CEO of Tesla and SpaceX", 90],
    "Oprah Winfrey": ["An American television host and media executive", 88],
    "Cristiano Ronaldo": ["A Portuguese professional footballer with a global fanbase", 94],
    "Taylor Swift": ["An American Grammy-winning pop singer and songwriter", 93],
    "Malala Yousafzai": ["A Pakistani Nobel Peace Prize winner and education activist", 85],
    "Bill Gates": ["An American co-founder of Microsoft and philanthropist", 91],
    "Marie Curie": ["A Polish pioneer physicist and chemist in radioactivity research", 89],
    "Barack Obama": ["An American 44th President and influential global figure", 90],
}
print("Welcome to the higher lower game!")
print("The rules are simple.You need to simply guess which of these people is the most popular")

name1,name2 = random.sample(sorted(people), k=2)
score = 0
IsFinished = False
while(IsFinished == False and people != {}):
    if(name1 == name2):
        #print(people)
        if(len(people) == 1):
            print(f"your final score is: {score + 1}")
            break
        else:
            while(name1 == name2):
                name1 = random.sample(sorted(people), k =1)[0]          
            
    print("Which of these two is more popular(1 or 2):")
    print(name1,": ",people[name1][0],"(1)")
    print("or")
    print(name2,": ",people[name2][0],"(2)")
    print(people[name1][1])
    print(people[name2][1])
    choice = int(input("your choice: "))
   
    if(people[name1][1] >= people[name2][1]):
        if(choice == 1):
            score += 1
            people.pop(name2)
            name2 = random.sample(sorted(people), k=1)[0]
        else:
            IsFinished = True
            print(f"your final score is: {score}")
    elif(choice == 2):
        score += 1
        people.pop(name1)
        name1 = random.sample(sorted(people), k=1)[0]
    else:
        IsFinished = True
        print(f"your final score is: {score}")
    print("####################################################################")
