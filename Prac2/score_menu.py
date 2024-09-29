def main():
    score = get_valid_score()
    menu = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell!")


def get_valid_score():
    """Prompt the user for a valid score between 0 and 100, inclusive."""
    score = float(input("Enter a score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. It must be between 0 and 100.")
        score = float(input("Enter a score (0-100): "))
    return score


def print_result(score):
    """Determine the result from the score and print it."""
    if score < 50:
        print("Bad")
    elif score < 90:
        print("Passable")
    else:
        print("Excellent")


def show_stars(score):
    """Print as many stars as the score."""
    print("*" * int(score))


main()