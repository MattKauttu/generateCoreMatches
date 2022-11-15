def get_dual_type_from_user():
    print("Select a dual type")
    print("Enter the first type, a space, and then the second type")
    print("Only enter the first type if there is no second type")
    print("Example: Dragon Fighting")
    types = input("Enter the dual type: ").split(" ")

    if len(types) == 1:
        pass
    elif len(types) == 2:
        pass
    else:
        pass

    key = types[0] + "_" + types[1]

    return key