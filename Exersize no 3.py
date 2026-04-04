Questions = [
    ["which language is used for creating youtube?","python","french","javascript","Php","None", 4],
    ["which language is used for creating instagram?","python","french","javascript","Php","None", 4],
    ["which language is used for creating facebook?","python","french","javascript","Php","None", 4],
    ["which language is used for creating twitter?","python","french","javascript","Php","None", 4],
    ["which language is used for creating linkedin?","python","french","javascript","Php","None", 4],
    ["which language is used for creating whatsapp?","python","french","javascript","Php","None", 4],
    ["which language is used for creating snapchat?","python","french","javascript","Php","None", 4],
]

Levels = [1000,2000,5000,6000,10000,100000,500000]

money = 0

for i in range(0,len(Questions)):
    question = Questions[i]
    
    print(f"\nQuestion for Rs.{Levels[i]}")
    print(question[0])
    print(f"1. {question[1]}   2. {question[2]}   3. {question[3]}   4. {question[4]}")
    
    reply = int(input("Enter your answer (1-4): "))
    
    if reply == question[-1]:
        print(f"Correct answer, you have won Rs.{Levels[i]}")
        
        if i == 2:
            money = 1000
        elif i == 3:
            money = 6000
        elif i == 4:
            money = 10000
    else:
        print("Wrong answer!")
        break

print(f"\nYou won Rs.{money}")