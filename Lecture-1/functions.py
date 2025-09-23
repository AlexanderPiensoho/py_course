def say_hello_to(name):
    print(f"Hej {name}!")


say_hello_to("Said")
say_hello_to("Alexander")


def add_numbers(num1,num2):
    result = num1 + num2
    return result

sum_total = add_numbers(42,56)
print(sum_total)


def double(number):
    return number*2

my_number = double(45)
print(my_number)
