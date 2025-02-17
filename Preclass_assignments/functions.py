#Excercise 1

def greet(names):
    for name in names:
        print(f"Hello, {name}!")
          

#Excercise 2

def goldilocks(length):
    if length < 140:
        print("Too short!")
    elif length > 150:
        print("Too long!")
    else:
        print("Just right!")

#Excercise 3

def square_list(numbers):
    return [number**2 for number in numbers]


#Excercise 4
def fibonacci_stop(value):
    fibonacci = [1, 1]
    while True:
        next_value = fibonacci[-1] + fibonacci[-2]
        if next_value >= value:
            break
        fibonacci.append(next_value)
    return fibonacci


#Excercise 5
def clean_pitch(pitch_angles, status_signals):
    cleaned_angles = []
    for angle, status in zip(pitch_angles, status_signals):
        if (angle < 0 or angle > 90) and status > 0:
            cleaned_angles.append(-999)
        else:
            cleaned_angles.append(angle)
    return cleaned_angles

