import easygui

#Dictionary
Cards = {"Stoneling":{"Name": "Stoneling", "Strength": 7, "Speed": 1, "Stealth": 25, "Cunning": 15},
         "Vexscream":{"Name": "Vexscream", "Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
         "Downmirage":{"Name": "Downmirage", "Strength": 1, "Speed": 6, "Stealth": 21, "Cunning": 19},
         "Blazegolem":{"Name": "Blazegolem", "Strength": 15, "Speed": 20, "Stealth": 23, "Cunning": 6},
         "Websnake":{"Name": "Websnake", "Strength": 7, "Speed": 15, "Stealth": 10, "Cunning": 5},
         "Moldvine:":{"Name": "Moldvine", "Strength": 21, "Speed": 18, "Stealth": 14, "Cunning": 5},
         "Vortexwing":{"Name": "Vortexwing", "Strength": 19, "Speed": 13, "Stealth": 19, "Cunning": 2},
         "Rotthing"{"Name": "Rotthing", "Strength": 16, "Speed": 7, "Stealth": 4, "Cunning": 12},
         "Froststep"{"Name": "Froststep", "Strength": 14, "Speed": 14, "Stealth": 17, "Cunning": 4},
         "Wispghoul"{"Name": "Wispghoul", "Strength": 17, "Speed": 19, "Stealth": 3, "Cunning": 2}}

def display_menu():
    choices = ["add new cards", "Delete cards", "Edit", "Print Catalogue", "Output All", "Exit"]
    choice = eg.buttonbox("Choose an option:", choices=choices)
    return choice