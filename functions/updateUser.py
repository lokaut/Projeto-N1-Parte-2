import inquirer
import pandas as pd

def updateUser(users):
    options = users['Email'].values.tolist()

    questions = [
        inquirer.List('option',
            message="Certo, qual usuário deseja alterar?",
            choices=options,
        ),
    ]
    answers = inquirer.prompt(questions)

    index = options.index(answers['option'])

    nome = input("Qual o novo nome de usuário? ")

    print(nome)

    new_df = pd.DataFrame({'Nome': [nome, ]}, index=[index])

    users.update(new_df)
    users.to_csv('data/users.csv')

    return