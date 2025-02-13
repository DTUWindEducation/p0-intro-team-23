def greet(name):
    # Prints a greeting message with the provided name
    print(f"Hello, {name}!")


def goldilocks(bed_length):
    # Determines if the bed length is suitable for Goldilocks
    if bed_length < 140:
        print("Too small!")
    elif bed_length > 150:
        print("Too large!")
    else:
        print("Just right. :)")


def square_list(numbers):
    # Returns a list where each number is squared
    return [num ** 2 for num in numbers]


def fibonacci_stop(max_value):
    # Generates a Fibonacci sequence up to a given maximum value
    fib_sequence = [1, 1]
    while True:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        if next_value > max_value:
            break
        fib_sequence.append(next_value)
    return fib_sequence


def clean_pitch(pitch_angles, status_signals):
    # Cleans the pitch angle data by setting invalid values to -999
    cleaned_data = []
    for angle, status in zip(pitch_angles, status_signals):
        if (angle < 0 or angle > 90) and status > 0:
            cleaned_data.append(-999)
        else:
            cleaned_data.append(angle)
    return cleaned_data


# Example usages
greet("world")  # Prints "Hello, world!"
goldilocks(139)  # Prints "Too small!"
goldilocks(140)  # Prints "Just right. :)"
goldilocks(151)  # Prints "Too large!"
goldilocks(150)  # Prints "Just right. :)"
print(square_list([1, 2, 3]))  # Prints [1, 4, 9]
print(fibonacci_stop(30))  # Prints Fibonacci sequence up to 30
print(clean_pitch([-1, 2, 6, 95], [1, 0, 0, 0]))  # Cleans pitch data
