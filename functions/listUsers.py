import pandas as pd

def listUsers():

    users = pd.read_excel('data/users.xlsx', sheet_name=None)

    print("\nos usuários cadastrados são:\n")

    print(users['users'])
    return