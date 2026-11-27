# Examples of reading JSON files in Python.
# The json module allows us to convert JSON data into Python
# data types, such as dictionaries, lists, strings, and numbers.
# A JSON object becomes a Python dictionary.
# A JSON array becomes a Python list.

import json


def read_student(filename):
    """Read and display information about a student."""

    with open(filename, "r") as file:
        # Read a JSON object into a Python dictionary
        data = json.load(file)

        # data is a dictionary
        # Access individual values using dictionary keys
        print("Name:", data["name"])
        print("Major:", data["major"])
        print("Year:", data["year"])
        print("GPA:", data["gpa"])

        # The value associated with the key "courses" is a list
        print("Courses:")
        for course in data["courses"]:
            print(course)


def read_books(filename):
    """Read and display information about all books."""

    with open(filename, "r") as file:
        # Read an array of JSON objects into a list of dictionaries
        data = json.load(file)

        # Each dictionary contains information about one book
        for book in data:
            print("Title:", book["title"])
            print("Author:", book["author"])
            print("Price:", book["price"])
            print("Available:", book["available"])
            print()


def find_available_books(filename):
    """Return a list of titles of available books."""

    available_books = []
    with open(filename, "r") as file:
        data = json.load(file)

        for book in data:
            if book["available"]:
                available_books.append(book["title"])

    return available_books


def main():
    read_student("student.json")

    print()
    read_books("books.json")

    available = find_available_books("books.json")
    print("Available books:", available)


if __name__ == "__main__":
    main()