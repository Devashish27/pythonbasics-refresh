name = "Tyron"
count = 1

# def greeting(firstname):
# def greeting(name):
#     color = 'yellow'
#     print(color)
#     print(name)
# print(firstname)


# greeting('Rama')


def another():
    color = 'yellow'
    # count = 2
    global count
    count += 1
    # count += 1
    print(count)

    def greeting(name):
        nonlocal color
        color = 'red'
        print(color)
        print(name)

    greeting('Tyron')


another()
