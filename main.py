import easygui as gui

catalogue = []


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
    card_name = gui.enterbox("Enter the name of the monster card")
    for card in catalogue:
        if card["name"] == card_name:
            catalogue.remove(card)
            gui.msgbox(f"Deleted {card_name} from the catalogue.")
            return


def print_catalogue():
    catalogue_title = "Name\t\t\t Type\n"
    for card in catalogue:
        catalogue_title += f"{card['name']}\t\t\t{card['type']}\n"
    gui.msgbox(catalogue_title, title="Catalogue")


# Define a function to search for a monster card in the catalogue
def search_card():
    search = gui.enterbox("Enter the name of the monster card")
    match_cards = []
    for card in catalogue:
        if card["name"].lower() == search.lower():
            match_cards.append(card)
    if match_cards:
        search_results_str = "Name\t\t\tType\n"
        for card in match_cards:
            search_results_str += f"{card['name']}\t{card['type']}\n"
        gui.msgbox(search_results_str, title=f"Search Results for "
                                             f"'{search}'")
    else:
        gui.msgbox(f"No cards matches '{search}' in your catalogue.")


while True:
    choice = gui.buttonbox("Choose an action:",
                           choices=["Catalogue", "Add card", "Delete card",
                                    "Find a card", "Exit"])
    if choice == "Add card":
        add_card()
    elif choice == "Delete card":
        delete_card()
    elif choice == "Find a card":
        search_card()
    elif choice == "Catalogue":
        print_catalogue()
    elif choice == "Exit":
        break
