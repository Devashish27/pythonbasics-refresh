'''Closure is a function having access 
to the scope of its parent function 
after the parent function has returned.'''


def parent_function(person, coins):
    # we are defining separate set of
    # coins here for parent class.
    # coins = 3

    def play_game():
        nonlocal coins
        coins -= 1

        if coins > 1:
            print("\n" + person + " has " +
                  str(coins) + " coins left.")
        elif coins == 1:
            print("\n" + person + " has " +
                  str(coins) + " coin left.")
        else:
            print("\n" + person + " is out of coins.")

    return play_game


aron = parent_function("Arun", 2)
noothan = parent_function("Noothan", 7)

aron()
aron()

noothan()
