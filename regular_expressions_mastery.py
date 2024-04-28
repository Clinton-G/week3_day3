import re




names = ["Abraham Lincoln", "Andrew P Garfield", "peter pan", "Connor Milliken", "Jordan Alexander Williams", "Madonna", "programming is cool"]


#   Expected Outcome:
# --------------------
# Abraham Lincoln
# Andrew P Garfield
# Invalid name
# Connor Milliken
# Jordan Alexander Williams
# Invalid name
# Invalid name


# def func that takes the list, run a loop over it, validate if its a good name, print if it is, invalid if it isnt, print end


def validate_names(names): # define
    pattern = r'^[A-Z]'    # regex combo

    for verify in names:   # for correct names in 'names'
        if re.match(pattern, verify):   # if it matches the pattern and correct
            print(verify)   # print only correct names
        else:
            print("Invalid name")   # invalid for wrong names

print(validate_names(names))    # print the validated names list