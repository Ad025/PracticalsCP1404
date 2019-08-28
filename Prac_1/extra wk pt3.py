def main():
    name = input("please enter name:")
    print("(H)ello\n(G)oodbye\n(Q)uit")
    choice = input("please enter a letter:")
    while choice.upper() != "Q":
        if choice.upper() == "H":
            print()
            print("hello", name)
            print("(H)ello\n(G)oodbye\n(Q)uit")
            choice = input("please enter a letter")

        elif choice.upper() == "G":
            print()
            print( "Goodbye", name)
            print("(H)ello\n(G)oodbye\n(Q)uit")
            choice = input("please enter a letter")
        else:
            print()
            print("Invalid letter")
            print()
            print("(H)ello\n(G)oodbye\n(Q)uit")
            choice = input("please enter a letter")
    print("Finished")





main()