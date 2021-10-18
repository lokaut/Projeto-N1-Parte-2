def addUser(users):

    print('Certo, vou precisar de mais algumas informações:\n')
    print(users.columns.values)

    nome = input("Qual o nome do novo usuário? ")
    email = input("Qual o email do novo usuário? ")

    while True: 

        engine = users.loc[users['Email'].str.contains(email, case=False)]

        if engine.index.value_counts().count() == 0:
            users.loc[users.index.value_counts().count()] = [nome, email]
            users.to_csv('data/users.csv')
            print('\nUsuário cadastrado com sucesso\n')
            print(users.loc[users['Email'].str.contains(email, case=False)])
            break
        else:
            print('\nJá existe um usuário cadastrado com esse email!!\n')
            email = input("Digite um novo email para esse usuário ou digite 'sair' para voltar ao menu principal: ")
            if email == 'sair': break


    
    return