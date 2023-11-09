# lib/cli.py
from models.Parent import Parent,Child

def reset_database():
    Parent.drop_table()
    Parent.create_table()
    Child.drop_table()
    Child.create_table()
reset_database()
Poseidon=Parent.create('Poseidon','Poseidon, the god of the sea, wielded a mighty trident and ruled the oceans with his tempestuous power, often associated with earthquakes and storms.')
Demeter=Parent.create('Demeter','Demeter, the goddess of agriculture, nurtured the earth\'s bountiful harvests and was deeply connected to the changing seasons, particularly her grief over her daughter Persephone\'s time in the Underworld.')
Zeus=Parent.create('Zeus','Zeus, the king of the gods and ruler of Mount Olympus, was the supreme deity in Greek mythology. His thunderbolt and eagle were symbols of his authority and power, and he was known for his role in the governance of the world and the enforcement of divine order.')
Hera=Parent.create('Hera','Hera, the queen of the gods, was known for her marriage to Zeus and her unwavering commitment to protecting the sanctity of marriage and family within the Greek pantheon.')
Hades=Parent.create('Hades','Hades, the ruler of the Underworld, presided over the realm of the dead and was a figure of solemnity and darkness in Greek mythology.')

Melinoe=Child.create('Melinoe','Melinoe was a minor goddess associated with ghosts and nightmares, often invoked to protect against the restless spirits of the deceased.',Hades)
Zagreus=Child.create('Zagreus','Zagreus was a mysterious deity, sometimes identified as a son of Zeus and Persephone, with connections to both the mysteries of the afterlife and Dionysian revelry.',Hades)

Proteus=Child.create('Proteus','Proteus was a shape-shifting sea god and an ancient prophetic figure who could foretell the future.',Poseidon)
Aeolus=Child.create('Aeolus','Aeolus was the god of the winds, responsible for controlling and directing the various winds that blew across the Mediterranean.',Poseidon)
Despoena=Child.create('Despoena','Despoena was a goddess of mysteries and initiations, often associated with the Eleusinian Mysteries, a significant religious event in ancient Greece.',Poseidon)

Ploutos=Child.create('Ploutos','Ploutos, the god of wealth and abundance, represented the concept of wealth as a blessing from the gods.',Demeter)

Hebe=Child.create('Hebe', 'Hebe was the youthful cupbearer of the gods, symbolizing youth and eternal vitality.', Hera)
Eileithyia=Child.create('Eileithyia','Eileithyia was the goddess of childbirth and labor pains, called upon by women in labor for a safe delivery.',Hera)

Dionysus=Child.create('Dionysus','Dionysus, the god of wine and revelry, brought joy and ecstasy to his followers through the consumption of his sacred beverage.', Zeus)
Apollo=Child.create('Apollo','Apollo, the god of music, poetry, and the sun, was a multifaceted deity associated with both artistic and prophetic talents.',Zeus)
Persephone=Child.create('Persephone','Persephone, the queen of the Underworld, was also a goddess of spring and vegetation, symbolizing the cycle of life, death, and rebirth.',Zeus)
Artemis=Child.create('Artemis', 'Artemis, the goddess of the hunt and the moon, was known for her independence and her fierce protection of the wilderness and its creatures.',Zeus)
Athena=Child.create('Athena','Athena, the goddess of wisdom and warfare, was a strategic deity known for her intelligence and martial prowess.',Zeus)
Ares=Child.create('Ares','Ares, the god of war, embodied the brutality and violence of conflict, often contrasted with the more disciplined aspects of Athena.',Zeus)
Hephaestus=Child.create('Hephaestus','Hephaestus, the blacksmith god, was a master craftsman who forged the divine weapons and tools of the gods.',Zeus)



from helpers import (
    exit_program,
    helper_1
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        
        elif choice == "1":
            list_sub()
        
        elif choice == "2":
            create_sub()

        elif choice == "3":
            delete_sub()

        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. A list of the Gods")
    print("2. Add a God")
    print("3. Delete a god")


def list_sub():
    while True:
        list_sub_menu()
        print(f'{Parent.get_all_parents()+Child.get_all_children()}')
        sub_choice = input("> ")
        if sub_choice in Parent.parent_names:
            for a in Parent.all_parents:
                bio=''
                if a.name == sub_choice:
                    print('[BIO]')
                    print(a.bio)
                    print('[CHILDREN]')
                    print(f'{a.name}\'s children are {a.get_children()}')
                    a.get_children()
                    
        elif sub_choice in Child.name_list:
            for a in Child.spawn:
                bio=''
                if a.name == sub_choice:
                    print('[BIO]')
                    print(a.bio)
                    print('[PARENT]')
                    a.my_parent()
        elif sub_choice == "back":
            break
        else:
            print('[invalid choice, try again.]')

def create_sub():
    while True:
        create_sub_menu()
        # need to incorporate input validation
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

def delete_sub():
    while True:
        delete_sub_menu()
        sub_choice=input("> ")
        if sub_choice in Parent.parent_names:
            Parent.parent_names.remove(sub_choice)
            for a in Parent.all_parents:
                if a.name == sub_choice:
                    a.update_delete()
                    Parent.all_parents.remove(a)
                    print(f'{a.name} has been deleted')
        elif sub_choice in Child.name_list:
            Child.name_list.remove(sub_choice)
            for a in Child.spawn:
                if a.name == sub_choice:
                    a.delete()
                    Child.spawn.remove(a)
                    print(f'{a.name} has been deleted')
        elif sub_choice == "back":
            break
        else:
            print('invalid')

def create_sub_menu():
    print('[Options]')
    print('type back to go back')
    print('type a new God\'s name to create them')

def delete_sub_menu():
    print('[Options]')
    print('type back to go back')
    print('type a God\'s name to delete them')

def list_sub_menu():
    print('[Options]')
    print('Type back to go back')
    print('(Type a God\'s name from the names below)')


if __name__ == "__main__":
    main()