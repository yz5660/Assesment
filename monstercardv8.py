import easygui

#Dictionary
 catalogue = {"Stoneling":{"Name": "Stoneling", "card_strength": 7, "card_speed}": 1, "card_stealth": 25, "card_cunning": 15},
         "Vexscream":{"Name": "Vexscream", "card_strength": 1, "card_speed}": 6, "card_stealth": 21, "card_cunning": 19},
         "Downmirage":{"Name": "Downmirage", "card_strength": 1, "card_speed}": 6, "card_stealth": 21, "card_cunning": 19},
         "Blazegolem":{"Name": "Blazegolem", "card_strength": 15, "card_speed}": 20, "card_stealth": 23, "card_cunning": 6},
         "Websnake":{"Name": "Websnake", "card_strength": 7, "card_speed}": 15, "card_stealth": 10, "card_cunning": 5},
         "Moldvine:":{"Name": "Moldvine", "card_strength": 21, "card_speed}": 18, "card_stealth": 14, "card_cunning": 5},
         "Vortexwing":{"Name": "Vortexwing", "card_strength": 19, "card_speed}": 13, "card_stealth": 19, "card_cunning": 2},
         "Rotthing":{"Name": "Rotthing", "card_strength": 16, "card_speed}": 7, "card_stealth": 4, "card_cunning": 12},
         "Froststep":{"Name": "Froststep", "card_strength": 14, "card_speed}": 14, "card_stealth": 17, "card_cunning": 4},
         "Wispghoul":{"Name": "Wispghoul", "card_strength": 17, "card_speed}": 19, "card_stealth": 3, "card_cunning: 2}}

def manu():
    choices = ["add new cards", "Delete cards", "Edit", "Print Catalogue", "Output All", "Exit"]
    choice = easygui.buttonbox("Choose an option:", choice=choice)


def print_catalogue():
    catalogue_title = "Name\t\t\t Type\n"
    for card in catalogue:
        catalogue_title += f"{card['name']}\t\t\t{card['type']}\n"
    easygui.msgbox(catalogue_title, title="Catalogue")


 def add_card():
        card_name = easygui.enterbox("Enter the name of the monster card:")
        card_strength = easygui.enterbox("Enter the strength of the monster card:")
        card_speed = easygui.enterbox("Enter the speed of the monster card:")
        card_stealth = easygui.enterbox("Enter the stealth of the monster card:")
        card_cunning = easygui.enterbox("Enter the cunning of the monster card:")
     catalogue.append()
easygui.msgbox(print("Added {card_name} ({card_strength}) ({card_speed}) ({card_stealth}) ({card_cunning}) to the catalogue."))


def delete_card():
        card_name = easygui.enterbox("Enter the name of the monster card")
        for card in catalogue:
            if card["name"] == card_name:
                catalogue.remove(card)
                easygui.msgbox(f"Deleted {card_name} from the catalogue.")
                return


while True:
        choice = easygui.buttonbox("Choose an action:",
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