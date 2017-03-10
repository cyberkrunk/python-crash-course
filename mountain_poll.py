responses = {}

# Set a flag to indicate that polling is active.

polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is your name? ")
    response = input("\nWhich mountain would you like to climb someday? ")

    # Store the responses in the dictionary.
    responses[name] = response

    # Find out if anyone else is going to take the poll.
    repeat = input("\nWould you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

# Polling is complete, show the response
print ("\n---Polling Results---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")


