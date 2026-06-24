science = {'Rahul', 'Amit', 'Sneha', 'Aman', 'Kiran'}
arts = {'Sneha', 'Priya', 'Kiran', 'Shivam'}
commerce = {'Amit', 'Kiran', 'Rohit'}

while True:
    print("\n--- MENU ---")
    print("1. Display Members")
    print("2. Show All Unique Members")
    print("3. Show Common Members")
    print("4. Add Member")
    print("5. Remove Member")
    print("6. Check Membership")
    print("7. Members in Only One Club")
    print("8. Members in Exactly Two Clubs")
    print("9. Count Members")
    print("10. Students Not in Any Club")
    print("11. Club with Maximum Members")
    print("12. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        print("Science:", science)
        print("Arts:", arts)
        print("Commerce:", commerce)

    elif choice == '2':
        all_members = science | arts | commerce
        print("All Unique Members:")
        print(all_members)

    elif choice == '3':
        common = science & arts & commerce
        print("Members present in all clubs:")
        print(common)
        print(f"Number of common members: {len(common)}")

    elif choice == '4':
        name = input("Enter member name: ")
        print("1. Science\n2. Arts\n3. Commerce")
        club_choice = input("Enter club choice (1-3): ")

        if club_choice == '1':
            if name in science:
                print(f"{name} already exists in Science club.")
            else:
                science.add(name)
                print(f"{name} added to Science club.")
        elif club_choice == '2':
            if name in arts:
                print(f"{name} already exists in Arts club.")
            else:
                arts.add(name)
                print(f"{name} added to Arts club.")
        elif club_choice == '3':
            if name in commerce:
                print(f"{name} already exists in Commerce club.")
            else:
                commerce.add(name)
                print(f"{name} added to Commerce club.")
        else:
            print("Invalid choice.")

    elif choice == '5':
        name = input("Enter member name to remove: ")
        found = False

        if name in science:
            science.remove(name)
            found = True
        if name in arts:
            arts.remove(name)
            found = True
        if name in commerce:
            commerce.remove(name)
            found = True

        if found:
            print(f"{name} removed from all clubs.")
        else:
            print(f"Warning: {name} does not exist in any club.")

    elif choice == '6':
        name = input("Enter member name to check: ")
        clubs_found = []

        if name in science:
            clubs_found.append("Science")
        if name in arts:
            clubs_found.append("Arts")
        if name in commerce:
            clubs_found.append("Commerce")

        if clubs_found:
            print(f"{name} is a member of: {', '.join(clubs_found)}")
        else:
            print("Not a member of any club")

    elif choice == '7':
        only_science = science - (arts | commerce)
        only_arts = arts - (science | commerce)
        only_commerce = commerce - (science | arts)

        one_club_members = only_science | only_arts | only_commerce
        print("Members in only one club:")
        print(one_club_members)

    elif choice == '8':
        sci_arts = (science & arts) - commerce
        sci_com = (science & commerce) - arts
        arts_com = (arts & commerce) - science

        two_club_members = sci_arts | sci_com | arts_com
        print("Members in exactly two clubs:")
        print(two_club_members)

    elif choice == '9':
        print(f"Science: {len(science)} members")
        print(f"Arts: {len(arts)} members")
        print(f"Commerce: {len(commerce)} members")

    elif choice == '10':
        students_input = input("Enter list of student names separated by commas: ")
        students = set(s.strip() for s in students_input.split(','))

        all_members = science | arts | commerce
        not_in_club = students - all_members

        print("Students not in any club:")
        print(not_in_club)

    elif choice == '11':
        max_count = max(len(science), len(arts), len(commerce))
        max_clubs = []

        if len(science) == max_count:
            max_clubs.append("Science")
        if len(arts) == max_count:
            max_clubs.append("Arts")
        if len(commerce) == max_count:
            max_clubs.append("Commerce")

        if len(max_clubs) == 1:
            print(f"Club with maximum members: {max_clubs[0]} ({max_count} members)")
        else:
            print(f"Clubs with maximum members ({max_count} members each): {', '.join(max_clubs)}")

    elif choice == '12':
        print("End")
        break

    else:
        print("Invalid choice. Please try again.")