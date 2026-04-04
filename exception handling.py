try:
    a = int(input("Enter a number : "))   
    print(f"multiplication table of {a} is:")
    for i in range(1, 11):
        print(f"{int(a)}x{i} = {int(a*i)}")

except ValueError:
    print("Please enter a valid integer number!")

except Exception as e:
    print("An error occurred:", e)

print("end")