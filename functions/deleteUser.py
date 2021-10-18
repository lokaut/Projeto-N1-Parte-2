import inquirer

def deleteUser(users):

    options = users['Email'].values.tolist()

    questions = [
        inquirer.List('option',
            message="Certo, qual usuário deseja deletar?",
            choices=options,
        ),
    ]
    answers = inquirer.prompt(questions)

    index = options.index(answers['option'])
    users = users.drop(users.index[index])
    users.to_csv('data/users.csv')
    return