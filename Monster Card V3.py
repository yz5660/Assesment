import easygui as gui
# Define the catalogue of monster cards as an empty list
catalogue = []


# Define a function to add a monster card to the catalogue
def add_card():
    # Get input from the user for the card's name and type
    card_name = gui.enterbox("Enter the name of the monster card:")
    card_type = gui.enterbox("Enter the type of the monster card:")

    # Create a dictionary to represent the monster card
    card = {"name": card_name, "type": card_type}

    # Add the card to the catalogue
    catalogue.append(card)

    # Show a message to confirm that the card was added
    gui.msgbox(f"Added {card_name} ({card_type}) to the catalogue.")


# Define a function to delete a monster card from the catalogue
def delete_card():
    # Get input from the user for the card's name to be deleted
    card_name = gui.enterbox("Enter the name of the monster card to be deleted:")

    # Loop through the catalogue to find the card to be deleted
    for card in catalogue:
        if card["name"] == card_name:
            # Remove the card from the catalogue
            catalogue.remove(card)

            # Show a message to confirm that the card was deleted
            gui.msgbox(f"Deleted {card_name} from the catalogue.")
            return

    # If the card was not found, show an error message
    gui.msgbox(f"{card_name} was not found in the catalogue.")


# Define a function to display the current catalogue
def display_catalogue():
    # Create a string with the header of the catalogue
    catalogue_str = "Name\tType\n"

    # Loop through the catalogue to add each card to the string
    for card in catalogue:
        catalogue_str += f"{card['name']}\t{card['type']}\n"

    # Show the catalogue string in a message box
    gui.msgbox(catalogue_str, title="Monster Card Catalogue")


# Define a loop to run the program until the user chooses to quit
while True:
    # Show a menu to the user and get their choice
    choice = gui.buttonbox("Choose an action:", choices=["Add card", "Delete card", "Display catalogue", "Quit"])

    # Call the appropriate function based on the user's choice
    if choice == "Add card":
        add_card()
    elif choice == "Delete card":
        delete_card()
    elif choice == "Display catalogue":
        display_catalogue()
    elif choice == "Quit":
        break


