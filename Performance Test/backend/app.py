import time
import os
import sys
import numpy as np
import subprocess

# Function to clear the terminal screen
def clear_screen():
    subprocess.run(['clear'])  # For Windows users, use 'cls')

# Function to create a dynamic loading bar based on the duration of the test
def loading_bar(duration):
    start_time = time.time()
    while True:
        elapsed_time = time.time() - start_time
        if elapsed_time >= duration:
            break
        percent_complete = min(100, elapsed_time / duration * 100)
        num_ticks = int(percent_complete / 10)
        progress_bar = '=' * num_ticks + ' ' * (10 - num_ticks)
        print(f"Progress: [{progress_bar}] {percent_complete:.1f}%", end='\r')
        time.sleep(0.1)
    print()  # Move to the next line after the loading bar completes

# First test: Measure performance of NumPy computation
def test_performance(num_elements):
    try:
        # Generate a large list of random numbers using NumPy
        data = np.random.rand(num_elements)

        # Measure the time taken to compute the sum of squares
        start_time = time.time()
        result = np.sum(data ** 2)  # Compute the sum of squares of the data
        end_time = time.time()

        # Calculate the elapsed time by subtracting start time from end time
        elapsed_time = end_time - start_time

        return True, elapsed_time, None
    except Exception as e:
        return False, 0, str(e)

# Second test: Sort a large array of random numbers
def sort_random_numbers(num_elements):
    try:
        data = np.random.rand(num_elements)

        # Record the start time before sorting
        tic = time.perf_counter()

        # Sort the random numbers in ascending order
        sorted_data = np.sort(data, kind="stable")

        # Record the end time after sorting
        toc = time.perf_counter()

        # Return the time taken to sort the numbers
        return True, toc - tic, None
    except Exception as e:
        return False, 0, str(e)

# Third test: Compute Mandelbrot set
def compute_mandelbrot_set(num_elements):
    try:
        def compute_point(c, max_iter):
            z = c
            for n in range(max_iter):
                if abs(z) > 2.0:
                    return n
                z = z * z + c
            return max_iter

        def mandelbrot(width, height, max_iter):
            result = np.zeros((height, width))
            for x in range(width):
                for y in range(height):
                    cx = (x - width / 2) * 4.0 / width
                    cy = (y - height / 2) * 4.0 / width
                    c = complex(cx, cy)
                    color = compute_point(c, max_iter)
                    result[y, x] = color
            return result

        width = 800
        height = 800
        max_iter = 256

        start_time = time.time()
        result = mandelbrot(width, height, max_iter)
        end_time = time.time()

        elapsed_time = end_time - start_time

        return True, elapsed_time, None
    except Exception as e:
        return False, 0, str(e)

# Fourth test: Measure performance of nested loops
def measure_nested_loops_performance(num_elements):
    try:
        start_time = time.time()
        for i in range(num_elements):
            x = np.sin(i) * np.cos(i)  # Perform computation without nested loops
        end_time = time.time()

        elapsed_time = end_time - start_time

        return True, elapsed_time, None
    except Exception as e:
        return False, 0, str(e)


# Fifth test: Print a large range of numbers
def print_large_range_numbers(num_elements):
    try:
        with open(os.devnull, 'w') as f:
            sys.stdout = f
            start_time = time.time()
            for i in range(num_elements):
                print(i)
            end_time = time.time()
            elapsed_time = end_time - start_time
        sys.stdout = sys.__stdout__
        return True, elapsed_time, None
    except Exception as e:
        return False, 0, str(e)

# Function to display test descriptions
def show_test_descriptions():
    print("Available tests:")
    print("1. Test Performance: This is a test to ensure the system is working properly.")
    print("2. Sort Random Numbers: This is a test to ensure the system is working properly.")
    print("3. Compute Mandelbrot set: This is a test to ensure the system is working properly.")
    print("4. Measure performance of nested loops: This is a test to ensure the system is working properly.")
    print("5. Print a large range of numbers: This is a test to ensure the system is working properly.")
    print("Enter the test number for more details (Enter B to go back):")
    option = input()
    if option.lower() == 'b':
        clear_screen()
        handle_user_input()
    else:
        try:
            test_number = int(option)
            if 1 <= test_number <= 5:
                show_test_detail(test_number)
                return
            else:
                print("Invalid test number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    show_test_descriptions()

# Function to display details of a specific test
def show_test_detail(test_number):
    clear_screen()
    test_descriptions = {
        1: "This test measures how fast the computer can add up a lot of numbers and square each one.",
        2: "This test measures how fast the computer can put a bunch of random numbers in order from smallest to biggest.",
        3: "This test measures how fast the computer can draw a pretty picture called the Mandelbrot set.",
        4: "This test measures how fast the computer can do lots of math problems one after the other.",
        5: "This test measures how fast the computer can count from 1 to a really big number."
    }
    description = test_descriptions.get(test_number)
    if description:
        print(f"Test {test_number}: {description}\n")
        print("Enter B to go back.")
    else:
        print("Invalid test number.")

# Function to handle user input and start tests accordingly
def handle_user_input():
    while True:
        print_header()
        option = input("Enter the number you want to go with: ")
        if option == '1':
            clear_screen()
            select_difficulty_level()
            break
        elif option == '2':
            clear_screen()
            show_test_descriptions()
        elif option == '3':
            print("Application cancelled.")
            break
        else:
            clear_screen()
            print("Invalid option. Please enter 1, 2, or 3.")

# Function to select difficulty level
def select_difficulty_level():
    print("Enter the level you want to go with:")
    print("[0] Sample")
    print("[1] Easy")
    print("[2] Medium")
    print("[3] Hard")
    print("[4] Learn about each level")
    print("[5] Press B to go back")
    option = input()
    if option == '0':
        clear_screen()
        start_tests(500000)  # Sample run: 500000 elements
    elif option == '1':
        clear_screen()
        start_tests(1000000)  # Easy level: 1 million elements
    elif option == '2':
        clear_screen()
        start_tests(1000000000)  # Medium level: 1 billion elements
    elif option == '3':
        clear_screen()
        start_tests(1000000000000)  # Hard level: 1 trillion elements
    elif option == '4':
        clear_screen()
        show_difficulty_levels_description()
    elif option.lower() == 'b':
        clear_screen()
        handle_user_input()
    elif option == '5':
        clear_screen()
        handle_user_input()
    else:
        print("Invalid option. Please enter a number between 0 and 5.")
        select_difficulty_level()

# Function to start tests
def start_tests(num_elements):
    print("Starting tests in 5 seconds...")
    loading_bar(5)
    print("Make sure the computer does not power off or sleep during the tests.")
    print("Press Ctrl+C to cancel the tests.")

    # Start the tests directly in the current terminal window
    test_functions = [
        test_performance,
        sort_random_numbers,
        compute_mandelbrot_set,
        measure_nested_loops_performance,
        print_large_range_numbers
    ]
    for i, test_function in enumerate(test_functions, start=1):
        print(f"Test {i}:")
        success, elapsed_time, error = test_function(num_elements)
        if success:
            print(f"Test {i} completed successfully in {elapsed_time:.4f} seconds.")
        else:
            print(f"Test {i} failed.")
            if error:
                print(f"Error: {error}")

    # Prompt to see error details
    for i, test_function in enumerate(test_functions, start=1):
        if not test_function(num_elements)[0]:  # If the test failed
            option = input(f"Do you want to see why test {i} failed? (Y/N): ")
            if option.upper() == 'Y':
                print(f"Error details for test {i}: {test_function(num_elements)[2]}")
            elif option.upper() == 'N':
                continue

    # Prompt to return to main menu or redo tests
    option = input("Do you want to return to the main menu (1) or redo tests (2)? (1/2): ")
    if option == '1':
        clear_screen()
        handle_user_input()
    elif option == '2':
        clear_screen()
        select_difficulty_level()
    else:
        print("Invalid option. Returning to the main menu.")
        clear_screen()
        handle_user_input()

# Function to display descriptions of difficulty levels
def show_difficulty_levels_description():
    print("Sample (500,000): This is a sample test to ensure the system is working properly.")
    print("Easiest (1 million): This level is designed to run tests with a small amount of data, suitable for most computers.")
    print("Medium (1 billion): This level is designed to run tests with a moderate amount of data, suitable for mid-range computers.")
    print("Hardest (1 trillion): This level is designed to run tests with a large amount of data, suitable for high-performance computers.")
    print("Press B to go back:")
    option = input()
    if option.lower() == 'b':
        clear_screen()
        select_difficulty_level()
    else:
        print("Invalid option. Please enter B to go back.")


# Function to print the header
def print_header():
    print("Enter the option you want to go with:")
    print("[1] Start tests")
    print("[2] Know what each test does")
    print("[3] Cancel")

# Main function
# Main function
if __name__ == "__main__":
    clear_screen()  # Clear the terminal screen when the program starts
    handle_user_input()
