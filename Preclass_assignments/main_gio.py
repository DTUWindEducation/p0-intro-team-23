from functions_gio import greet, goldilocks, square_list, fibonacci_stop, clean_pitch

# Example usages
greet("world")  # Prints "Hello, world!"
goldilocks(139)  # Prints "Too small!"
goldilocks(140)  # Prints "Just right. :)"
goldilocks(151)  # Prints "Too large!"
goldilocks(150)  # Prints "Just right. :)"
print(square_list([1, 2, 3]))  # Prints [1, 4, 9]
print(fibonacci_stop(30))  # Prints Fibonacci sequence up to 30
print(clean_pitch([-1, 2, 6, 95], [1, 0, 0, 0]))  # Cleans pitch data
