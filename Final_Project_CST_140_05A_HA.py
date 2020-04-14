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
# Turtle another feature showing you result.
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

import turtle


def user_turtle():
    def row_one():
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

    def row_two():
        t = turtle.Turtle()
        t.penup()
        t.goto(100,100)
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

    def row_three():
        t = turtle.Turtle()
        t.penup()
        t.goto(100,-100)
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

    if __name__ == '__main__':
        row_one()
        row_two()
        row_three()

        turtle.Screen().exitonclick()


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
    user_input_full_list = (input("To create your list all at once, "
                                  "please first press the ENTER button. "
                                  "Then enter 9 numbers. After you enter one number, press enter and then "
                                  "type your second number, followed by your third and so on. "
                                  "\nAll numbers should be between 1 and 9.\n"))
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
    return user_turtle()


def individually_enter_list():
    # Starting our first row
    # Prompt user to enter first number, for the first row at the first index (0).
    user_input_at_index_zero = int(input("To create your first row of your list, "
                                         "please enter your first "
                                         "number, between 1 and 9:"))
    if 0 < user_input_at_index_zero <= 9:
        print("You entered:", user_input_at_index_zero, "\nYour number at index 0 will be:", user_input_at_index_zero)
    else:
        raise ValueError("You entered: %s You did not enter a number between 1 and 9." % user_input_at_index_zero)

    # Prompt user to enter second number, for the first row at the second Index (1).
    user_input_at_index_one = int(input("To continue your first row of your list, "
                                        "please enter your second number, between 1 and 9:"))
    if 0 < user_input_at_index_one <= 9:
        print("You entered:", user_input_at_index_one, "\nYour number at index 1 will be:", user_input_at_index_one)
    else:
        print("You entered:", user_input_at_index_one, "You did not enter a number between 1 and 9.")
        return play_again()

    # Prompt user to enter third number, for the first row at the third index(2).
    user_input_at_index_two = int(input("To finish your first row of your list, "
                                        "please enter your last number for this row, between 1 and 9:"))
    if 0 < user_input_at_index_two <= 9:
        print("You entered:", user_input_at_index_two, "\nYour number at index 2 will be:", user_input_at_index_two)
    else:
        print("You entered:", user_input_at_index_two, "You did not enter a number between 1 and 9.")
        return play_again()

    # First row user list will display  first row!
    first_row_user_list = [user_input_at_index_zero,user_input_at_index_one,user_input_at_index_two]

    print("Your first row of your list is:\n%s" % first_row_user_list)

    # Starting  our second row!

    # Prompt user to enter the first number, for the second row at the third index (3).
    user_input_at_index_three = int(input("To create your second row of your list, "
                                          "please enter your first "
                                          "number for your second row, between 1 and 9:"))
    if 0 < user_input_at_index_three <= 9:
        print("You entered:", user_input_at_index_three, "\nYour number at index 3 will be:", user_input_at_index_three)
    else:
        print("You entered:", user_input_at_index_three, "You did not enter a number between 1 and 9.")
        return play_again()

    # Prompt user to enter the second number, for the second row at the fourth index (4).
    user_input_at_index_four = int(input("To continue your second row of your list, "
                                         "please enter your second number for your second row, between 1 and 9:"))
    if 0 < user_input_at_index_four <= 9:
        print("You entered:", user_input_at_index_four, "\nYour number at index 4 will be:", user_input_at_index_four)
    else:
        print("You entered:", user_input_at_index_four, "You did not enter a number between 1 and 9.")
        return play_again()

    # Prompt user to enter the third number, for the second row at the fifth index (5).
    user_input_at_index_five = int(input("To finish your second row of your list, "
                                         "please enter your third "
                                         "number for your second row, between 1 and 9:"))
    if 0 < user_input_at_index_five <= 9:
        print("You entered:", user_input_at_index_five, "\nYour number at index 5 will be:", user_input_at_index_five)
    else:
        print("You entered:", user_input_at_index_five, "You did not enter a number between 1 and 9.")
        return play_again()

    # Second row user list will display second row!
    second_row_user_list = [user_input_at_index_three, user_input_at_index_four, user_input_at_index_five]

    # Print second row
    print("Your second row of your list is:\n%s" % second_row_user_list)

    # Print first + second row on new lines
    print("So far your list looks like this:\n%s\n%s" % (first_row_user_list, second_row_user_list))

    # Starting  our third row!
    # Prompt user to enter the first number, for the third row at the sixth index (6).
    user_input_at_index_six = int(input("To create your final row of your list, please enter your first "
                                        "number for your third row, between 1 and 9:"))
    if 0 < user_input_at_index_six <= 9:
        print("You entered:", user_input_at_index_six, "\nYour number at index 6 will be:", user_input_at_index_six)
    else:
        print("You entered:", user_input_at_index_six, "You did not enter a number between 1 and 9.")
        return play_again()

    # Prompt user to enter the second number, for the third row at the seventh index (7).
    user_input_at_index_seven = int(input("To continue your final row of your list,"
                                          " please enter your second number for your third row, between 1 and 9:"))
    if 0 < user_input_at_index_seven <= 9:
        print("You entered:", user_input_at_index_seven, "\nYour number at index 7 will be:", user_input_at_index_seven)
    else:
        print("You entered:", user_input_at_index_seven, "You did not enter a number between 1 and 9.")
        return play_again()

    # Prompt user to enter the final number, for the third row at the eighth index (8).
    user_input_at_index_eight = int(input("To finish your final row of your list, please enter your third "
                                          "number for your third row, between 1 and 9:"))
    if 0 < user_input_at_index_eight <= 9:
        print("You entered:", user_input_at_index_eight, "\nYour number at index 8 will be:", user_input_at_index_eight)
    else:
        print("You entered:", user_input_at_index_eight, "You did not enter a number between 1 and 9.")
        return play_again()

    # third row user list will display third row!
    third_row_user_list = [user_input_at_index_six,user_input_at_index_seven,user_input_at_index_eight]
    # Print third row
    print("Your third row of your list is:\n%s" % third_row_user_list)

    if sum(first_row_user_list) == sum(second_row_user_list) and sum(second_row_user_list) == sum(third_row_user_list):
        print("Congratulations! The sum of your rows equal the same amount!")
    else:
        print("The sum of your numbers do not add up to the same amount.")
        return play_again()

    # Check to make sure the list adds up diagonally
    user_diagonal_list_starting_at_index_zero = [user_input_at_index_zero, user_input_at_index_four,
                                                 user_input_at_index_eight]
    #
    user_diagonal_list_starting_at_index_two = [user_input_at_index_two, user_input_at_index_four,
                                                user_input_at_index_six]
    print("Your first diagonal list is", user_diagonal_list_starting_at_index_zero)
    print("Your second diagonal list is", user_diagonal_list_starting_at_index_two)

    if sum(user_diagonal_list_starting_at_index_zero) == sum(user_diagonal_list_starting_at_index_two):
        print("Congratulations! The sum of each diagonal in your list adds up to the same amount!")
    else:
        print("The sum of your diagonal numbers do not add up to the same amount.")
        return play_again()

    # Check to see if each column is equal to the same amount
    # First column
    user_first_column = [user_input_at_index_zero, user_input_at_index_three, user_input_at_index_six]
    print("Your first column is", user_first_column)
    # Second column
    user_second_column = [user_input_at_index_one, user_input_at_index_four, user_input_at_index_seven]
    print("Your second column is", user_second_column)
    # Third column
    user_third_column = [user_input_at_index_two, user_input_at_index_five, user_input_at_index_eight]
    print("Your third column is", user_third_column)

    if sum(user_first_column) == sum(user_second_column) and sum(user_second_column) == sum(user_third_column):
        print("Congratulations! Your columns all add up to the same amount!")
        # Print final list
        print("Your final list is:\n%s\n%s\n%s" %
              (first_row_user_list, second_row_user_list, third_row_user_list))
    else:
        print("Sorry! Your columns do not add up to the same amount.")
        return play_again()
# This ends the individual list entry!


def win():
        print("Congratulations you have won the game!")
        # return turtle here
        # return counter here ?
        # for k in __:
        #     if __ == k:
        # 	___ +=1


game()


