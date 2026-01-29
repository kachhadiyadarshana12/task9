import logging
#logging module create
logging.basicConfig(
    filename="error_log.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def perform_division(a, b):
    #try, except, else, finally blocks
    try:
        result = a / b
    except ZeroDivisionError:
        logging.error("Division by zero error occurred.")
        print("Error: You cannot divide by zero.")
    except TypeError:
        logging.error("Invalid input type for division.")
        print("Error: Please enter numeric values only.")
    else:
        print("Result:", result)
    finally:
        print("Division operation finished.\n")

def access_list(data, index):
    try:
        value = data[index]
    except IndexError:
        logging.error("Index out of range while accessing list.")
        print("Error: List index is out of range.")
    else:
        print("Element found: ", value)
    finally:
        print("List access completed.")

#runtome error
print("---- Error Handling Demo ----\n")
perform_division(10, 0)
perform_division(10, "two")
perform_division(10, 2)
numbers = [1, 2, 3]
access_list(numbers, 5)