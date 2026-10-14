# Import the two functions from my diary tools file.
from diary_tools import save_entry, search_entries


def main():
    # Show the program name.
    print("Diary Entry Application")

    # Ask which text file to use for diary entries.
    diary_file = input("Enter diary file name (example: my_diary.txt): ")

    # Repeat the menu until the user chooses Exit.
    while True:
        print("\n1. Write a diary entry")
        print("2. Read or search diary entries")
        print("3. Exit")

        choice = input("Choose 1, 2, or 3: ")

        if choice == "1":
            # Get the date and text, then save the entry.
            entry_date = input("Enter date (YYYY-MM-DD): ")
            entry_text = input("Write your diary entry: ")
            save_entry(diary_file, entry_date, entry_text)

        elif choice == "2":
            # Find diary entries for a date.
            search_date = input("Enter a date to search (YYYY-MM-DD): ")
            search_entries(diary_file, search_date)

        elif choice == "3":
            # Leave the menu loop.
            print("Goodbye!")
            break

        else:
            # Ask again when the choice is not valid.
            print("Invalid choice. Please try again.")


# Run main only when this file is started directly.
if __name__ == "__main__":
    main ()