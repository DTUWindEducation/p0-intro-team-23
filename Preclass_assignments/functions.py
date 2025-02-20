#1 Simple function
def greet(name):
    return print(f'Hello, {name}!')


#2 If/else statements
def goldilocks(bed_length):
    if bed_length < 140:
        print('Too small!')
    elif bed_length > 150:
        print('Too large!')
    else:
        print('Just right. :)')
    return 0


#3 For loops
def square_list(numbers):
    numbers_square = []
    for x in numbers:
        numbers_square.append(x**2)
    return print(numbers_square)


#4 While loops
def fibonacci_stop(max_value):
    Fibonacci_numbers = [1, 1]
    while True:
        next_fib = Fibonacci_numbers[-1] + Fibonacci_numbers[-2]
        if next_fib >= max_value:
            break
        Fibonacci_numbers.append(next_fib)
    return print(Fibonacci_numbers)


#5 Logical operators
def clean_pitch(x, status):
    for i in range(len(x)):
        if status[i] == 1:
            x[i] = -999
    return print(x)

