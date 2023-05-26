import easygui

#Dictionary
 catalogue = {"Stoneling":{"Name": "Stoneling", "Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
         "Vexscream":{"Name": "Vexscream", "Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
         "Downmirage":{"Name": "Downmirage", "Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
         "Blazegolem":{"Name": "Blazegolem", "Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
         "Websnake":{"Name": "Websnake", "Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
         "Moldvine:":{"Name": "Moldvine", "Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
         "Vortexwing":{"Name": "Vortexwing", "Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
         "Rotthing":{"Name": "Rotthing", "Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
         "Froststep":{"Name": "Froststep", "Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
         "Wispghoul":{"Name": "Wispghoul", "Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}}

def manu():
    choices = ["add new cards", "Delete cards", "Edit", "Print Catalogue", "Output All", "Exit"]
    choice = easygui.buttonbox("Choose an option:", choice=choice)

 def add_card():
        card_name = easygui.enterbox("Enter the name of the monster card:")
        card_strength = easygui.enterbox("Enter the strength of the monster card:")
        card_speed = easygui.enterbox("Enter the speed of the monster card:")
        card_stealth = easygui.enterbox("Enter the stealth of the monster card:")
        card_cunning = easygui.enterbox("Enter the cunning of the monster card:")
     catalogue.insert()
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