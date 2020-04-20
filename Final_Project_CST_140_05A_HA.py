#########################
# Final Project         #
# Lo Shu Magic Square   #
# Hannah Adcox          #
# CST 140 05A           #
#########################

# Please zip your file with all names (initials) on the zip file, you will lose points.
# You MUST also turn in a video presenting your project.

# Requirements:
# Must throw an exception. I should not be able to type in any a character or character key. [DONE]
# It should not let me enter in any number. It should ask you to enter a number from 1 - 9. [DONE]
# Your code should allow you to play again. You will need a loop. [DONE]
# You should add a feature like a counter to track wins and lost.
# Turtle another feature showing you result. [DONE]
# Allow me to choose option 1 prompt the user or option 2 setting the list, use an if elif. [DONE]
# Please make sure you include instructions in your program. [DONE]
# Your detailed Algorithm should include all for, if statements in the process, all function explanations.
# The input should consist of all explanations of input. Output should consist all the outputs in your program.
# Every line should consist of comment key words like Get, Ask, Prompt the user, Calculate or Compute, and Display.

# Final Project - Lo Shu Magic Square
# The Lo Shu Magic Square is a grid with 3 rows and 3 columns.
# The Lo Shu Magic Square properties:
# The grid contains the numbers 1 though 9 exactly.
# The sum of each row, each column, and each diagonal all add up to the same number.
# Prompt the user to enter a number 1-9 / throw an exception

# user_list = [   at index
#     [4, 9, 2], [0, 1, 2]
#     [3, 5, 7], [3, 4, 5]
#     [8, 1, 6]  [6, 7, 8]
# ]


# Lets start the game!


def win():
        print("Congratulations you have won the game!")
        return play_again()
        # return counter here ?
        # for k in __:
        #     if __ == k:
        # 	___ +=1


def play_again():
    while True:
        again = input("Thank you for playing my game, would you like to start over? Type yes or no!")
        if again not in {"yes","no"}:
            print("Please enter valid input!")
        elif again == "no":
            return "Thank you for playing!"
        elif again == "yes":  # call function to start the game again
            return game()


def game():
    user_choice = input("Would you like to play a game? Please enter yes or no: ")  # Ask user if they want to play!
    if user_choice == "yes":
        print("Lets play! We will create a Lu Shu Magic Square! "
              "To win the game, the sum of each row, each column, "
              "and each diagonal should all add up to the same number.")
        return user_list_choice()
    elif user_choice == "no":
        print("We will not be playing a game.")
        exit(0)
    else:
        print("You did not enter a valid response.")
        return game()


def user_list_choice():
    user_list_choice_one = input("Would you like to enter your list all at once, or individually? "
                                 "Please enter: full list or individually.")
    if user_list_choice_one == "full list":
        print("You have chosen to create your list all at once!")
        return full_list_at_once()
    elif user_list_choice_one == "individually":
        print("You have chosen to create your list individually!")
        return individually_enter_list()
    else:
        print("You did not enter a valid response.")
        return play_again()


def full_list_at_once():
    user_input_full_list = ("To create your list all at once, please enter nine numbers. "
                            "Enter your first number and then hit enter,"
                            " type your second number, followed by your third and so on. "
                            "\nAll numbers should be between 1 and 9.\n")
    print(user_input_full_list)
    lst = []
    n = int(9)
    for i in range(0,n):
        element = int(input())
        if element not in {1,2,3,4,5,6,7,8,9}:
            raise ValueError
        else:
            lst.append(element)
    print(lst)
    print("Your full list is:", lst)

    row_one = lst[0:3]
    row_two = lst[3:6]
    row_three = lst[6:9]
    print(row_one)
    print(row_two)
    print(row_three)
    print("Now lets check your list to see if it is a Lu Shu Magic Square! Your rows, columns and each diagonal need "
          "to equal the same amount!")
    if sum(row_one) == sum(row_two) and sum(row_two) == sum(row_three):
        print("Congratulations! Your rows all add up to the same amount! Now lets check your columns!")
    else:
        print("Sorry! Your rows do not add up to the same amount.")
        return play_again()

    column_one = [lst[0],lst[3],lst[6]]
    column_two = [lst[1],lst[4],lst[7]]
    column_three = [lst[2],lst[5],lst[8]]
    print("Your first column is:",column_one)
    print("Your second column is:",column_two)
    print("Your third column is:", column_three)
    if sum(column_one) == sum(column_two) and sum(column_two) == sum(column_three):
        print("Congratulations! Your columns all add up to the same amount! "
              "Lastly lets check to see if each diagonal adds up to the same amount!")
    else:
        print("Sorry! Your columns do not add up to the same amount.")
        return play_again()
    user_diagonal_list_starting_at_index_zero = [lst[0], lst[4], lst[8]]
    user_diagonal_list_starting_at_index_two = [lst[2], lst[4],lst[6]]
    print("Your first diagonal list is", user_diagonal_list_starting_at_index_zero)
    print("Your second diagonal list is", user_diagonal_list_starting_at_index_two)

    if sum(user_diagonal_list_starting_at_index_zero) == sum(user_diagonal_list_starting_at_index_two):
        print("Congratulations! The sum of each diagonal in your list adds up to the same amount!")
    else:
        print("The sum of your diagonal numbers do not add up to the same amount.")
        return play_again()
    print("Congratulations you have successfully created a Lu Shu Magic Square!")
    print(row_one)
    print(row_two)
    print(row_three)

    import turtle

    def user_turtle():
        def user_row_one():
            t = turtle.Turtle()
            # Turtle first row
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.penup()
            t.back(100)
            t.pendown()
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.penup()
            t.back(100)
            t.pendown()
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.pendown()

        def user_row_two():
            t = turtle.Turtle()
            t.penup()
            t.goto(100, 100)
            t.pendown()
            t.forward(0)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.penup()
            t.back(100)
            t.pendown()
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.penup()
            t.back(100)
            t.pendown()
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.pendown()

        def user_row_three():
            t = turtle.Turtle()
            t.penup()
            t.goto(100, -100)
            t.pendown()
            t.forward(0)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.penup()
            t.back(200)
            t.pendown()
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.penup()
            t.back(100)
            t.pendown()
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.pendown()

        def turtle_user_list():
            t = turtle.Turtle()
            t.penup()
            t.goto(-150,150)
            t.pendown()
            t.write(lst[0], font=("Arial",12,"normal"))
            t.penup()
            t.goto(-50,150)
            t.pendown()
            t.write(lst[1],font=("Arial",12,"normal"))
            t.penup()
            t.goto(50,150)
            t.pendown()
            t.write(lst[2], font=("Arial",12,"normal"))
            t.penup()
            t.goto(50,50)
            t.pendown()
            t.write(lst[5], font=("Arial",12,"normal"))
            t.penup()
            t.goto(-50,50)
            t.pendown()
            t.write(lst[4], font=("Arial", 12, "normal"))
            t.penup()
            t.goto(-150,50)
            t.pendown()
            t.write(lst[3], font=("Arial", 12, "normal"))
            t.penup()
            t.goto(-150,-50)
            t.pendown()
            t.write(lst[6], font=("Arial", 12, "normal"))
            t.penup()
            t.goto(-50,-50)
            t.pendown()
            t.write(lst[7], font=("Arial", 12, "normal"))
            t.penup()
            t.goto(50,-50)
            t.pendown()
            t.write(lst[8], font=("Arial", 12, "normal"))
            t.penup()

        if __name__ == '__main__':
            user_row_one()
            user_row_two()
            user_row_three()
            turtle_user_list()
            turtle.Screen().exitonclick()
    return user_turtle(), win()


def individually_enter_list():
    # Starting our first row
    # Prompt user to enter first number, for the first row at the first index (0).
    user_input_at_index_zero = ("To create your first row of your list, "
                                         "please enter your first "
                                         "number, between 1 and 9:")
    print(user_input_at_index_zero)
    lst_at_index_0 = []
    n = int(1)
    for i in range(0, n):
        element = int(input())
        if element not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            raise ValueError
        else:
            lst_at_index_0.append(element)
    print(lst_at_index_0)
    print("Your number at index 0 is:", lst_at_index_0)

    user_input_at_index_one = ("To continue your first row of your list, "
                                         "please enter your second "
                                         "number, between 1 and 9:")
    print(user_input_at_index_one)

    lst_at_index_1 = []
    n = int(1)
    for i in range(0, n):
        element = int(input())
        if element not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            raise ValueError
        else:
            lst_at_index_1.append(element)
    print(lst_at_index_1)
    print("Your number at index 1 is:", lst_at_index_1)

    user_input_at_index_two = ("To finish your first row of your list, "
                                         "please enter your third "
                                         "number, between 1 and 9:")
    print(user_input_at_index_two)
    lst_at_index_2 = []
    n = int(1)
    for i in range(0, n):
        element = int(input())
        if element not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            raise ValueError
        else:
            lst_at_index_2.append(element)
    print(lst_at_index_2)
    print("Your number at index 2 is:", lst_at_index_2)

    user_input_at_index_three = ("To start your second row of your list, "
                                         "please enter your first "
                                         "number, between 1 and 9:")
    print(user_input_at_index_three)
    lst_at_index_3 = []
    n = int(1)
    for i in range(0, n):
        element = int(input())
        if element not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            raise ValueError
        else:
            lst_at_index_3.append(element)
    print(lst_at_index_3)
    print("Your number at index 3 is:", lst_at_index_3)

    user_input_at_index_four = ("To continue your second row of your list, "
                                         "please enter your second "
                                         "number, between 1 and 9:")
    print(user_input_at_index_four)
    lst_at_index_4 = []
    n = int(1)
    for i in range(0, n):
        element = int(input())
        if element not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            raise ValueError
        else:
            lst_at_index_4.append(element)
    print(lst_at_index_4)
    print("Your number at index 4 is:", lst_at_index_4)

    user_input_at_index_five = ("To finish your second row of your list, "
                                         "please enter your third "
                                         "number, between 1 and 9:")
    print(user_input_at_index_five)
    lst_at_index_5 = []
    n = int(1)
    for i in range(0, n):
        element = int(input())
        if element not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            raise ValueError
        else:
            lst_at_index_5.append(element)
    print(lst_at_index_5)
    print("Your number at index 5 is:", lst_at_index_5)

    user_input_at_index_six = ("To start your third row of your list, "
                                         "please enter your first "
                                         "number, between 1 and 9:")
    print(user_input_at_index_six)
    lst_at_index_6 = []
    n = int(1)
    for i in range(0, n):
        element = int(input())
        if element not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            raise ValueError
        else:
            lst_at_index_6.append(element)
    print(lst_at_index_6)
    print("Your number at index 6 is:", lst_at_index_6)

    user_input_at_index_seven = ("To continue your third row of your list, "
                                         "please enter your second "
                                         "number, between 1 and 9:")
    print(user_input_at_index_seven)
    lst_at_index_7 = []
    n = int(1)
    for i in range(0, n):
        element = int(input())
        if element not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            raise ValueError
        else:
            lst_at_index_7.append(element)
    print(lst_at_index_7)
    print("Your number at index 7 is:", lst_at_index_7)

    user_input_at_index_eight = ("To finish your third row of your list, "
                                         "please enter your third "
                                         "number, between 1 and 9:")
    print(user_input_at_index_eight)
    lst_at_index_8 = []
    n = int(1)
    for i in range(0, n):
        element = int(input())
        if element not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            raise ValueError
        else:
            lst_at_index_8.append(element)
    print(lst_at_index_8)
    print("Your number at index 8 is:", lst_at_index_8)

    row_one = [lst_at_index_0,lst_at_index_1,lst_at_index_2]
    print("Your first row is:", row_one)

    row_two = [lst_at_index_3,lst_at_index_4,lst_at_index_5]
    print("Your second row is:", row_two)

    row_three = [lst_at_index_6,lst_at_index_7,lst_at_index_8]
    print("Your third row is:",row_three)

    print("Now lets check your list to see if it is a Lu Shu Magic Square! Your rows, columns and each diagonal need "
          "to equal the same amount!")

    if sum(row_one) == sum(row_two) and sum(row_two) == sum(row_three):
        print("Congratulations! Your rows all add up to the same amount! Now lets check your columns!")
    else:
        print("Sorry! Your rows do not add up to the same amount.")
        return play_again()

    column_one = [lst_at_index_0, lst_at_index_3, lst_at_index_6]
    column_two = [lst_at_index_1, lst_at_index_4, lst_at_index_7]
    column_three = [lst_at_index_2, lst_at_index_5, lst_at_index_8]
    print("Your first column is:", column_one)
    print("Your second column is:", column_two)
    print("Your third column is:", column_three)

    if sum(column_one) == sum(column_two) and sum(column_two) == sum(column_three):
        print("Congratulations! Your columns all add up to the same amount! "
              "Lastly lets check to see if each diagonal adds up to the same amount!")
    else:
        print("Sorry! Your columns do not add up to the same amount.")
        return play_again()

    user_diagonal_list_starting_at_index_zero = [lst_at_index_0, lst_at_index_4, lst_at_index_8]
    user_diagonal_list_starting_at_index_two = [lst_at_index_2, lst_at_index_4, lst_at_index_6]
    print("Your first diagonal list is", user_diagonal_list_starting_at_index_zero)
    print("Your second diagonal list is", user_diagonal_list_starting_at_index_two)

    if sum(user_diagonal_list_starting_at_index_zero) == sum(user_diagonal_list_starting_at_index_two):
        print("Congratulations! The sum of each diagonal in your list adds up to the same amount!")
    else:
        print("The sum of your diagonal numbers do not add up to the same amount.")
        return play_again()
    print("Congratulations you have successfully created a Lu Shu Magic Square!")
    print(row_one)
    print(row_two)
    print(row_three)

    import turtle

    def individual_user_turtle():
        def user_row_one():
            t = turtle.Turtle()
            # Turtle first row
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.penup()
            t.back(100)
            t.pendown()
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.penup()
            t.back(100)
            t.pendown()
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.pendown()

        def user_row_two():
            t = turtle.Turtle()
            t.penup()
            t.goto(100, 100)
            t.pendown()
            t.forward(0)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.penup()
            t.back(100)
            t.pendown()
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.penup()
            t.back(100)
            t.pendown()
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.pendown()

        def user_row_three():
            t = turtle.Turtle()
            t.penup()
            t.goto(100, -100)
            t.pendown()
            t.forward(0)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.penup()
            t.back(200)
            t.pendown()
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.penup()
            t.back(100)
            t.pendown()
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.forward(100)
            t.left(90)
            t.pendown()

        def turtle_individual_user_list():
            t = turtle.Turtle()
            t.penup()
            t.goto(-150,150)
            t.pendown()
            t.write(lst_at_index_0, font=("Arial",12,"normal"))
            t.penup()
            t.goto(-50,150)
            t.pendown()
            t.write(lst_at_index_1,font=("Arial",12,"normal"))
            t.penup()
            t.goto(50,150)
            t.pendown()
            t.write(lst_at_index_2, font=("Arial",12,"normal"))
            t.penup()
            t.goto(50,50)
            t.pendown()
            t.write(lst_at_index_5, font=("Arial",12,"normal"))
            t.penup()
            t.goto(-50,50)
            t.pendown()
            t.write(lst_at_index_4, font=("Arial", 12, "normal"))
            t.penup()
            t.goto(-150,50)
            t.pendown()
            t.write(lst_at_index_3, font=("Arial", 12, "normal"))
            t.penup()
            t.goto(-150,-50)
            t.pendown()
            t.write(lst_at_index_6, font=("Arial", 12, "normal"))
            t.penup()
            t.goto(-50,-50)
            t.pendown()
            t.write(lst_at_index_7, font=("Arial", 12, "normal"))
            t.penup()
            t.goto(50,-50)
            t.pendown()
            t.write(lst_at_index_8, font=("Arial", 12, "normal"))
            t.penup()

        if __name__ == '__main__':
            user_row_one()
            user_row_two()
            user_row_three()
            turtle_individual_user_list()
        turtle.Screen().exitonclick()
    return individual_user_turtle(), win()



# This ends the individual list entry!


game()


