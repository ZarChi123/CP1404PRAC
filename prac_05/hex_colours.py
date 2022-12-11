"""Hexadecimal program"""
COLOUR_CODES={"Acid Green":"#b0bf1a","Aqua":"#00ffff","Bronze":"#cd7f32","AntiqueWhite1":"#ffefdb","aquamarine2": "#76eec6","azure4": "#838b8b","Corn": "#fbec5d","beige": "#f5f5dc","bisque1": "#ffe4c4","Brink Pink":"#fb607f"}
colour_name=input("Enter a colour name:").upper()
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_CODES.get(colour_name)}")
    colour_name = input("Enter a colour name: ")