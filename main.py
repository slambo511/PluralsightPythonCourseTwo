# functions
# a function is a piece of reusable code which allows you to do something over and over again without rewriting code
# remember to be DRY and not WET (Don't Repeat Yourself and not Write Everything Twice)
# a function should fo ONE thing, if your function does more than that, you need to separate out the other thing(s) to
# new function(s)

# Python has many, many "built in" functions, these include print(), str(), int(), input(), etc.
# can you see the one thing that links them all? Can you think of any others?
# If you need to do something in Python like input text, be sure there is not a built in function before you go writing
# one, this falls under the DRY principle.

# So here are some functions to examine

students = []

def get_students_titles():
    students_titles = []
    for student in students:
        students_titles = student.title()
    return students_titles


def print_students_titles():
    students_titles = []
    for student in students:
        students_titles = student.title()
    print(students_titles)


def add_student(name):
    students.append(name)


# so, note the "def" keyword, this tells Python that everything in the following code block is part of the function we
# are designing. The next word is the function name, you will use this to call the function when you need to use it.
# As you noted looking at the built in functions, they must end with (), this is make it clear when you call it, that
# you are calling a function.
# Function one has a "return" at the end, this lets you pass out a result from the function to the calling code, so one
# way we could use it is like so:

# all_titles = get_student_titles()

# this would return the array created by the method into the array all_titles
# Function three has something in the parentheses, this is known as an argument or parameter (they are called arguments
# when you pass them into a function and parameters in the function that uses them)and it lets you pass thing(s) into
# the function for the function to use. In this case a name is passed in and appended (added) to the list of students,
# it is used like so:

# add(student("James Earl Jones")

# so you pass the argument "James Earl Jones" in the name parameter of the add_student function, simple, right?
# You may look at the second function and think "why do you need that, you are repeating yourself, the only difference
# is that it prints the result instead of returning it as an array?", if you thought this, you are starting to think
# like a programmer. You can see that we have repeated ourselves twice effectively, so how can we fix this. Well the
# print_student_titles() function uses an array of student title to print them out, well get_student_titles() creates
# and returns such an array, do why not use it to adhere to the DRY principle? How, like this:

# def print_students_titles():
#     students_titles = get_student_titles()
#     print(student_titles)

# Much better we have reused code instead of rewriting it. Also testing this code is going to be much easier.

# So what about a function that needs parameters and returns something? Well:


def add_together(number_one, number_two):
    result = number_one + number_two
    return result

# A simple example, I know, but that is the gist of it, to use it we just need to input:

print(add_together(3, 4))

# Out pops 7, the sum of 3 and 4.
# Function arguments (the bits in the parentheses) can be passed in externally or manually entered at the time of
# writing the function:


def example_function_external(student_id, student_name):
    students.append(student_name)
    students.id = student_id

# To use this function you will need to pass both a student_id and a student_name, you can however declare them at code
# time:


def example_function_declared(student_name, student_id=223):
    students.append(student_name)
    students.id = student_id

# So, notice that we have swapped the arguments around, this is because "default" arguments (declared ones) must go last
# As a side note, the function name and any arguments it takes are as a unit is known as the method's "signature"
# Be aware that if you try to pass a student_id into example_function_declared() you will receive an error.


