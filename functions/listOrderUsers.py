def listOrderUsers(users):

    print("\nos usuários cadastrados em ordem alfabetica são:\n")

    print(users.sort_values(['Nome']))
    return