#%% Create a dictionary for your fruits and price

fruits_dict = { 
    "apple": 0.5, 
    "orange": 0.3, 
    "pineapple": 1.2
}

# Dictionary in Python:
# dictionary_name = { 
#     "key 1": value 1, 
#     "key 2": value 2,  
#     "key 3": value 3, 
#       ...
# }
# 
# For example, in fruits_dict, the key "apple" has value of 0.5.

#%% Main Menu

# The program runs forever, unless the user pics Option 4: Quit
while True:

# The contents of a block string are all literal. 
# Therefore, if there is indentation, it will be printed as well.
# So, that's why the contents are not indented in this case.
# Only the print() method needs to be indented, as it belongs to a parent while-loop.

    print("""
Fruit Ordering System
----------------------
1. Order Fruit
2. List Fruit Price
3. Update Fruit Price
4. Quit""")


    #  A list to record the quantity of each fruit
    orders = [0, 0, 0]

    # List in Python
    # 
    # list_name = [index 0, index 1, index 2, ... ]
    # 
    # For example, 
    # 
    # students = ['Carole', 'Jamie', 'Raphael', 'Hubert']
    # 
    # Carole's index is 0, Jamie's is 1, Raphael's is 2, and Hubert's is 3. 
    # So if we want to call Jamie, then we can refer to her like this:
    # 
    # jamie = students[1]
    # 
    # Fun fact: You can even start counting from the right.
    # From the right, Hubert's index is -1, Raphael's is -2, Jamie's is -3, and Carole's is -4.
    # Therefore, Jamie can also be called by:
    # 
    # jamie = students[-3]
    # 
    # lists, a.k.a. arrays, are extremely widely used in all programming languages. 
    # We are currently only using 1D arrays.
    # Arrays can even come in higher dimensions, like 2D, 3D, even 4D, 5D and beyond, arrays. (Especially in the field of AI)


    # Choose one of the four options. Ask again if invalid.
    while True:
        chosen_option = int(input("Please Enter Your Option: "))
        if chosen_option in [1,2,3,4]: break

    # match-case, only available for Python 3.10 and above. (Similar to switch-case in C/C++)
    # If using older versions of Python, please resort to using if-elif-else.

    match chosen_option:

        #  Option 1: Order fruit
        case 1:

            while True:

                # Pick a fruit. Ask again if invalid. Non case sensitive.
                while True:
                    fruit_to_order = input("Fruit to order: ").lower()
                    if fruit_to_order in ['apple', 'orange', 'pineapple']: break
                
                # Set how many of that fruit to buy. Ask again if input given is not a number.
                while True:
                    quantity = input("Quantity: ")
                    if quantity.isdigit(): break
                
                # Convert the keys of fruits_dict into a list ["apple", "orange", "pineapple"]
                fruits = list(fruits_dict.keys())

                # Get the index of the chosen fruit
                # e.g. "orange" has the index 1.
                index = fruits.index(fruit_to_order)

                # Increase the member of 'orders' list by the quantity given
                # e.g. If quantity given is 2, and "orange" is chosen, we get index = 1
                # Then orders[1] is added by 2.
                orders[index] += int(quantity)

                # A compressed way to write them, on a single line of code:
                # orders[list(fruits_dict.keys()).index(fruit_to_order)] += int(quantity)
                # Benefit: less variables needed

                # Shall we check out? Ask again if user input is invalid. Non case sensitive.
                while True:
                    check_out = input("\nDo you want to check out? (Y/N) ").lower()
                    print("")
                    if check_out in ['y', 'n']: break
                
                # If check_out is a Yes, then exit the loop to stop ordering fruits, proceed to calculations and check out.
                if check_out == 'y': break
            
            # Calculations and check out
            count = 1
            total = 0
            print("Your Order")
            for index, fruit in enumerate(fruits_dict):
                result = fruits_dict[fruit] * orders[index]
                # total = total + result
                total += result
                if result != 0:
                    print(f"{count}. {fruit} - ${result}")
                    # count = count + 1
                    count += 1
            print(f"Total price: ${total}")

            # To enumerate fruits_dict is to assign index/numbers to each of its keys.
            # So, for the case of fruits_dict, after enumeration, it will become like:
            # 0     apple       0.5
            # 1     orange      0.3
            # 2     pineapple   1.2
            # 
            # *** 
            # Do note that the enumerate(fruits_dict) was NOT stored into any variable at all. 
            # So, fruits_dict remains unchanged. The enumerate() function is like a mask used on fruits_dict
            # to make it look different for the moment. In other words, no equal sign used means nobody is changed. 
            # ***
            # 
            # However, we cannot directly print() it. Instead, we can use a for-loop, as shown above,
            # to iterate/scan through them one by one (row by row).
            # In the use case above, we use: index, fruit to store columns 1 and 2 of the enumerated fruits_dict.
            # So, index is:
            #     0
            #     1
            #     2
            # And, fruit is:
            #     apple
            #     orange
            #     pineapple
            # 
            # The for-loop takes 'index' and 'fruit' one by one.
            # 
            # During the 1st cycle, index = 0, fruit = "apple"
            # fruits_dict[fruit] means fruits_dict["apple"], which equals to 0.5
            # orders[index] mean orders[0], which, if 2 apples were ordered, equals to 2.
            # 
            # Hence, result = fruits_dict[fruit] * orders[index] 
            #               = fruits_dict["apple"] * orders[0] 
            #               = 0.5 * 2 
            #               = 1.0
            # 
            # And the cycle/iteration is repeated till the end of fruits_dict.
        
        #  Option 2: List fruit price
        case 2:
            # \n means new line or next line. Equivalent to pressing "Enter" on the keyboard.
            print("""\nFruit Pricing\n-------------""")
            for index, (fruit, price) in enumerate(fruits_dict.items()):
                print(f"{index+1}. {fruit} - ${price}")

            # In Python, the .items() method is a built-in dictionary method 
            # that returns a view object that contains the key-value pairs of the dictionary as tuples.
            # 
            # A tuple is a type of variable that resembles the coordinates. (Can be 2D, 3D, or higher dimension)
            # e.g. 
            # A tuple of integers:
            #     x = (13, 68)
            # A tuple of strings:
            #     primary_colours = (red, green, blue)
            # 
            # Tuple vs List: A list can be modified and manipulated, whereas a tuple cannot.
            # 
            # Of course, the above algorithm can also be performed using multiple lines, 
            # referencing the dictionary's keys and values directly like 
            # print(f"1. apple - {fruits_dict['apple']}")
            #  ...
        
        # Option 3: Update Fruit Price
        case 3:

            # Pick a fruit to update price. Ask again if invalid. Non case sensitive.
            while True:
                fruit_to_update_price = input("\nFruit to update price: ").lower()
                if fruit_to_update_price in ['apple', 'orange', 'pineapple']: break
            
            # Enter its new price. Ask again if invalid. Non case sensitive.
            while True:
                try:
                    new_price = float(input("Please enter new price: "))
                except ValueError:
                    continue
                break
            # User confirmation. Ask again if invalid. Non case sensitive.
            while True:
                update = input("\nProceed to update? (Y/N) ").lower()
                if update in ['y', 'n']: break

            if update == 'y':
                fruits_dict[fruit_to_update_price] = new_price
                print(f"New price for {fruit_to_update_price} is ${new_price}.")
                
        # Option 4: Quit
        case 4:
            break

        case _:
            pass

# End of while-loop



