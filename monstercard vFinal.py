import easygui
#Dictionary
catalogue = {
    "Stoneling": {"Name": "Stoneling", "card_strength": 7, "card_speed": 1,
                  "card_stealth": 25, "card_cunning": 15},
    "Vexscream": {"Name": "Vexscream", "card_strength": 1, "card_speed": 6,
                  "card_stealth": 21, "card_cunning": 19},
    "Dowmirage": {"Name": "Dowmirage", "card_strength": 1, "card_speed": 6,
                   "card_stealth": 21, "card_cunning": 19},
    "Blazgolem": {"Name": "Blazgolem", "card_strength": 15, "card_speed": 20,
                   "card_stealth": 23, "card_cunning": 6},
    "Websnake": {"Name": "Websnake", "card_strength": 7, "card_speed": 15,
                 "card_stealth": 10, "card_cunning": 5},
    "Moldvine": {"Name": "Moldvine", "card_strength": 21, "card_speed": 18,
                 "card_stealth": 14, "card_cunning": 5},
    "Vortexwing": {"Name": "Vortexwing", "card_strength": 19, "card_speed": 13,
                   "card_stealth": 19, "card_cunning": 2},
    "Rotthing": {"Name": "Rotthing", "card_strength": 16, "card_speed": 7,
                 "card_stealth": 4, "card_cunning": 12},
    "Froststep": {"Name": "Froststep", "card_strength": 14, "card_speed": 14,
                  "card_stealth": 17, "card_cunning": 4},
    "Wispghoul": {"Name": "Wispghoul", "card_strength": 17, "card_speed": 19,
                  "card_stealth": 3, "card_cunning": 2}
}

#print function
def print_catalogue():
    catalogue_title = "Name\tStrength\tSpeed\tStealth\tCunning\n"
    for card in catalogue.values():
        catalogue_title += "{}\t{}\t{}\t{}\t{}\n".format(
            card["Name"], card["card_strength"], card["card_speed"],
            card["card_stealth"], card["card_cunning"])
    easygui.msgbox(catalogue_title, title="Catalogue")

#adding function
def add_card():
    #the enter boxes
    card_name = easygui.enterbox("Enter the name of the monster card:")
    card_strength = easygui.enterbox("Enter the strength of the monster card:")
    card_speed = easygui.enterbox("Enter the speed of the monster card:")
    card_stealth = easygui.enterbox("Enter the stealth of the monster card:")
    card_cunning = easygui.enterbox("Enter the cunning of the monster card:")
    #add it to the catalogue
    catalogue[card_name] = {
        "Name": card_name,
        "card_strength": max(int(card_strength), 25),
        "card_speed": max(int(card_speed), 25),
        "card_stealth": max(int(card_stealth), 25),
        "card_cunning": max(int(card_cunning), 25)
    }
    easygui.msgbox("Added {} to the catalogue.".format(card_name))

#Delete function
def delete_card():
    card_name = easygui.enterbox("Enter the name of the monster card:")
    #if found in the catalogue
    if card_name in catalogue:
        del catalogue[card_name]
        easygui.msgbox("Deleted {}.".format(card_name))
    #if not
    else:
        easygui.msgbox("Card {} does not exist in the catalogue."
                       .format(card_name))

#Search function
def search_card():
    search = easygui.enterbox("Enter the name of the monster card")
    match_cards = []
    for card in catalogue.values():
        if card["Name"].lower() == search.lower():
            match_cards.append(card)
    #if found the card in the catalogue
    if match_cards:
        search_results_str = "Name\tStrength\tSpeed\tStealth\tCunning\n"
        for card in match_cards:
            search_results_str += "{}\t{}\t{}\t{}\t{}\n".format(
                card["Name"], card["card_strength"], card["card_speed"],
                card["card_stealth"], card["card_cunning"])
        easygui.msgbox(search_results_str, title="Search Results for '{}'".format(search))
    #if not
    else:
        easygui.msgbox("No cards match '{}' in your catalogue.".format(search))

#output function
def output():
    #subtitles
    print("Name\tStrength\tSpeed\tStealth\tCunning")
    for card in catalogue.values():
        #details of the cards
        print("{}\t{}\t{}\t{}\t{}".format(
            card["Name"], card["card_strength"], card["card_speed"],
            card["card_stealth"], card["card_cunning"]))

#Menu
while True:
        choice = easygui.buttonbox("Choose an action:",
                                   choices=["Catalogue", "Add card",
                                            "Delete card","Find a card",
                                            "Output", "Exit"])
        #Add cards
        if choice == "Add card":
            add_card()
        #Delete Cards
        elif choice == "Delete card":
            delete_card()
        #search a cars
        elif choice == "Find a card":
            search_card()
        #Print catalogue
        elif choice == "Catalogue":
            print_catalogue()
        #output catalogue
        elif choice == "Output":
            output()
        #exit the program
        elif choice == "Exit":
            break