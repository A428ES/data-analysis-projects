food = "water bottles,meal packs,snacks,chocolate"
equipment = "space suits,jet packs,tool belts,thermal detonators"
pets = "parrots,cats,moose,alien eggs"
sleep_aids = "blankets,pillows,eyepatches,alarm clocks"

# a) Use split to convert the strings into four cabinet lists. Alphabetize the contents of each cabinet.
# b) Initialize a cargo_hold list and add the cabinet lists to it. Print cargo_hold to verify its structure.
# c) Query the user to select a cabinet (0 - 3) in the cargo_hold.
# d) Use bracket notation and format to display the contents of the selected cabinet. If the user entered an invalid number, print an error message.
cargo_hold = []

for string in [food, equipment, pets, sleep_aids]:
    new_hold = string.split(',')
    new_hold.sort()

    cargo_hold.append(new_hold)

hold_index = int(input('Pick a cargo hold(0-3): '))


if hold_index <= 3 and hold_index >= 0:
    search_item = input('Provide an item: ')
    contained = "DOES"

    if search_item not in cargo_hold[hold_index]:
        contained += " NOT"

    print(f"Cabinet {hold_index} {contained} contain {search_item}.")
else:
    print('Error: Invalid index')
