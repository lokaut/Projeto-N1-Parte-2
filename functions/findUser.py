def findUser(users):

    nome = input("Qual o nome que deseja buscar? ")

    engine = users.loc[users['Nome'].str.contains(nome, case=False)]

    if engine.index.value_counts().count() == 0:
        print('\nNenhum usuário foi encontrado nessa lista')
    else:
        print('\nO(s) usuário(s) encontrado(s) foi/foram:\n')
        print(engine)

    return