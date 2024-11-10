from guitar import Guitar


def main():
    print("Let's rock with your guitars!")
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("Current guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nSorted guitars:")
    display_guitars(guitars)

    add_new_guitars(guitars)
    save_guitars(guitars, filename)


def load_guitars(filename):
    guitars = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 3:
                    guitars.append(Guitar(*parts))
    except FileNotFoundError:
        print(f"No existing file named {filename}. Starting fresh.")
    return guitars


def display_guitars(guitars):
    for index, guitar in enumerate(guitars, start=1):
        vintage_status = "(Vintage)" if guitar.is_vintage() else ""
        print(f"{index}: {guitar} {vintage_status}")


def add_new_guitars(guitars):
    print("\nAdd a new guitar to your collection. Leave name empty to stop.")
    while True:
        name = input("Name: ")
        if not name:
            break
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} added.")


def save_guitars(guitars, filename):
    with open(filename, 'w') as file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=file)
    print("Guitars saved.")


main()
