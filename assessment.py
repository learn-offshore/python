# Conditional statements

# 1. Write a program that checks if a number is positive, negative, or zero.
# 2. Write a program that checks if a number is even or odd.

# 3. Write a program that checks if a number is prime or not.
# 4. Write a program that checks if a string is a palindrome or not.


barrel_of_water = int(input("Enter the amount of water in the barrel (in liters): ")) # 35
barrel_capacity = 50 # 50L

while(barrel_of_water != barrel_capacity): # 35 != 50
    
    # barrel_of_water = int(input("Enter the amount of water in the barrel (in liters): ")) # 35

    if (barrel_of_water < barrel_capacity): # 35 < 50
        print(f"Not enough to fill the barrel. Please add {barrel_capacity - barrel_of_water}L more to fill it.")
        # print("Please add", barrel_capacity - barrel_of_water, "more water to fill the barrel.")
    else: 
        print(f"Too much water! Please remove {barrel_of_water - barrel_capacity}L to fill the barrel.")

    barrel_of_water = int(input("Enter the amount of water in the barrel (in liters): ")) # 35
else:
    print("Perfect amount for filling the barrel.")
