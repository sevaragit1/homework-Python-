import json
from datetime import datetime
from tabulate import tabulate

notes = []

def load_notes():
    global notes
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
    except FileNotFoundError:
        notes = []

def save_notes():
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)

def show_all_notes():
    if not notes:
        print("No notes available.")
    else:
        table = [[note["id"], note["created"], note["text"]] for note in notes]
        print(tabulate(table, headers=["ID", "Created Date", "Text"], tablefmt="rounded_grid"))

def show_note_details():
    try:
        note_id = int(input("Please enter the note ID: "))
        for note in notes:
            if note["id"] == note_id:
                print(f"ID: {note['id']}\nCreated: {note['created']}\nText: {note['text']}")
                return
        print("Note is not found.")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")

def create_note():
    note_id = len(notes) + 1
    text = input("Please enter the note text: ")
    created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append({"id": note_id, "text": text, "created": created})
    save_notes()
    print("Note created successfully!")

def update_note():
    try:
        note_id = int(input("Please enter the note ID to update: "))
        for note in notes:
            if note["id"] == note_id:
                new_text = input("Please enter the new text: ")
                note["text"] = new_text
                save_notes()
                print("Note updated successfully!")
                return
        print("Note not found.")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")

def delete_note():
    try:
        note_id = int(input("Please enter the note ID to delete: "))
        for i, note in enumerate(notes):
            if note["id"] == note_id:
                del notes[i]
                save_notes()
                print("Note deleted successfully!")
                return
        print("Note not found.")
    except ValueError:
        print("Invalid input. Please enter a valid ID.")

def main():
    load_notes()

    while True:
        print("\nChoose option:")
        print("1: Show all notes")
        print("2: Show note details")
        print("3: Create note")
        print("4: Update note")
        print("5: Delete note")
        print("Q: Quit")
        print("M: Menu")
        
        choice = input("Choice: ").strip().lower()

        if choice == '1':
            show_all_notes()
        elif choice == '2':
            show_note_details()
        elif choice == '3':
            create_note()
        elif choice == '4':
            update_note()
        elif choice == '5':
            delete_note()
        elif choice == 'q':
            print("Goodbye!")
            break
        elif choice == "M":
            continue
        else:
            print("Error!")
main()