def hello_world():
    print("Hello world!!")


hello_world()


# def sum(num1, num2=3):
def sum(num1=0, num2=0):
    # print(num1 + num2)
    if (type(num1) is not int or type(num2) is not int):
        return 0
    return num1 + num2


# total = sum(2, 3)
# total = sum("a", 3)
# total = sum(3)
# total = sum(1, 2)
total = sum(7, 2)
print(total)

# sum(2, 4)
# sum(1, 7)
# sum(5, 11)


def multiple_items(*args):
    print(args)
    print(type(args))


multiple_items("Tyron", "Anvitha", "Rithika")


def mul_named_items(**kwargs):
    print(kwargs)
    print(type(kwargs))

mul_named_items(first="Dev", last="Ashish")

