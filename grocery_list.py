
import os
import fnmatch

#look in /lists directory and create a list of file names for the grocery categories

list_of_lists = os.listdir('lists')
categories = []

for i in list_of_lists:
    i = i.replace('.txt', '')
    categories.append(i)


#create a dict and for each category item, add a key for the item
grocery_inventory = dict()

for i in categories:
    grocery_inventory[i] = []


#for each key (category item), open the text file with its name and add each line as a value to the appropriate key

for i in grocery_inventory:
    with open('lists/' + i +'.txt', 'r') as f:
        for line in f:
            line = line.replace('\n', '')
            grocery_inventory[i].append(line)
            if 'str' in line:
                f.close()
                break


items = grocery_inventory.values()

flat_list = []
for sublist in items:
    for item in sublist:
        flat_list.append(item)



def take_inventory():
    for i in flat_list:
        while True:
            answer = input('Do we need ' + i)
            if answer not in ('y', 'n'):
                print("Use 'y' or 'n'.")
            else:
                if answer == 'y':
                    grocery_list.append(i)
                    break
                elif answer == 'n':
                    break
                else:
                    print("you broke it")
                    
def extra_stuff():
    while True:
        answer = input("Anything else? Type out items or enter 'no'.")
        if answer != 'no':
            grocery_list.append(answer)
        elif answer == 'no':
            break
        else:
            print('You broke it.')

            
def make_list():
    take_inventory()
    extra_stuff()



grocery_list = []
make_list()



print(grocery_list)

