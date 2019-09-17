def main():
    hex_colours = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntigueWhite1": "#ffefdb",
                   "AntiqueWhite2": "#eedfcc", "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                   "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "Azure1": "#f0ffff"}
    #
    # colour_choice = input("Enter colour name")
    # while colour_choice != "":
    #     print("{}-{}".format(colour_choice,
    #                          HEX_COLOURS.get(colour_choice)))
    #     colour_choice = input("Enter colour name")


    finished = False
    while not finished:
        try:
            for colour in hex_colours:
                colour_choice = input("Enter a colour listed above:")
                if colour_choice == colour:
                    print("{} - {}".format(colour, hex_colours[colour]))

                else:
                    print("Invalid")
                    finished = True

        except ValueError:
            print("Sorry invalid entry.")
            colour_choice = input("Enter a colour listed above:")

    return colour_choice


main()
