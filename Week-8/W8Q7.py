def create_lists():
    user_input = input("Enter distinct integers separated by spaces: ")
    int_list = list(set(map(int, user_input.split())))

    if len(int_list) % 2 != 0:
        print("Please enter an even number of distinct integers.")
        return

    mid = len(int_list) // 2
    list1 = [x for x in int_list[:mid]]
    list2 = [x for x in int_list[mid:]]

    final_list1 = [x for x in list1 if x < list2[list1.index(x)]]
    final_list2 = [x for x in list2 if x > list1[list2.index(x)]]

    print("List 1 (less than elements of List 2):", final_list1)
    print("List 2 (greater than elements of List 1):", final_list2)


create_lists()
