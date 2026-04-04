a=int(input("Enter a value between 5 or 9"))
if (a<5 or a>9):
    raise ValueError("value shoul have to be between 5 or 9")
else:
    print("you entered right value")


