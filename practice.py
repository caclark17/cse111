def candy(type):
    print('Do you want some ' + type + '?')

# Instead of type, replace with the name of a candy
candy('snickers')
candy('skittles')

def get_initial(name):
    # create a parameter named initial that gets the first initial of
    #the name entere=d
    initial = name[0:1]
    # By returning initial it allows for name to produce just the first
    #initial of the name that is entered
    return initial
#get the user's first name
first_name = input('Enter your first name: ')
# have the function run to get the initial and store it in another variable
first_name_initial = get_initial(first_name)

middle_name = input('Enter your middle name: ')
middle_name_initial = get_initial(middle_name)

last_name = input('Enter your last name: ')
last_name_initial = get_initial(last_name)



print('Your initials are: ' + first_name_initial \
    + middle_name_initial \
    + last_name_initial)

