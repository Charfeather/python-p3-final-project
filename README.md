# Python Object-Relational Mapping with a CLI 

## Introduction

This is a Phase 3 project for [Flatiron School](https://flatironschool.com/). Its primary purpose is to help students master the following learning goals:

- Implement a Python application that includes a Command Line Interface.
    - The CLI must display menus with which a user may interact.
    - The CLI must include options to create, delete, display all objects, view related objects, and find an object by attribute.
    - The CLI should validate user input and object creations/deletions, providing informative errors to the user.
- Implement a set of Object-Relational Mapping functions for two or more model classes.
- Define a Python object model that includes a one-to-many relationship between two classes.
- Exercise best practices in CLI design.
- Exercise best practices in OOP.

This project was created by [Charles Featherstone](https://github.com/Charfeather), [Joseph Agramonte](https://github.com/Jagramonte), and [David Stinnette](https://github.com/dastinnette).

---

## Getting Started

To get this app running on your local machine, first **fork** a copy into your Github account then **clone** from that copy. Once you've opened the code files from your terminal, install any additional dependencies you know you'll need for your project by adding them to the `Pipfile`. Then run the commands:

```console
pipenv install
pipenv shell
```

---

## Project Breakdown

Start by running the following command in your terminal:

```console
python lib/cli.py
```

You will then see a menu with 4 options. You can exit the program, see a list of various Gods from ancient mythology, add a God to the list, or remove a God. Follow the prompts to interact with the app.

All of this functionality comes from our `cli.py` file. This contains a `main()` function that is responsible for the initial menu the user sees and invokes the various CRUD functions depending on user input. These CRUD fuctions use methods from the Parent and Child classes defined in the `Parent.py` file. In our app, a Parent God can have many children but a child God can only have one parent. Here is an example of a function that creates a God from the `cli.py` file and uses methods defined in the `Parent.py` file:

```py
# lib/cli.py

def create_sub():
    while True:
        create_sub_menu()
        new_name = input("> ")

        if new_name == "back":
            break
        if new_name in Parent.parent_names:
            print(f"[{new_name} already exists]")
            break
        if new_name in Child.name_list:
            print(f"[{new_name} already exists]")
            break
        if new_name in Parent.deleted_parents_name:
            print(f"[{new_name} was deleted but has been restored]")
            for a in Parent.deleted_parents:
                if a.name == new_name:
                    a.restore_delete()
            break
        else:
            new_bio = input("Enter the new god's bio: ")
            if new_bio == "back":
                break
            else:
                parent = input("Enter the new god's parent (enter 'none' if new god has no parent): ")
                if parent == "back":
                    break
                else:
                    if parent == "none":
                        Parent.create(new_name, new_bio)
                        print(f"God {new_name} created successfully.")
                    else:
                        if parent in Parent.parent_names:
                            for a in Parent.all_parents:
                                parent_name = ""
                                if a.name == parent:
                                    parent_name = a
                                    Child.create(new_name, new_bio, parent_name)
                                    print(f"God {new_name} created successfully.")
                        else:
                            print(f"Parent {parent} not found. Please enter a valid parent name.")
```

In the `create_sub()` function shown above, a user enters the number 2 from the main menu to access this create a God sub menu. The user is then instructed to enter a new God's name, bio, and if they have a Parent or not. We added error handling if a user tries to enter a God name (Parent or Child) that already exists using the `parent_names` method from the `Parent` class and the `name_list` method from the `Child` class. The user then decides whether the new God has a parent or not. If they enter a name for the new God's parent, that input invokes `parent_names` and `all_parents` methods defined in the `Parent` class and checks if the input name matches a God name already in the database. At any point in this 3 step process the user can enter the command "back" to exit the create sub menu.
