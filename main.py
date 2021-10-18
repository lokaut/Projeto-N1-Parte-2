from functions.updateUser import updateUser
from functions.addUser import addUser
from functions.listUsers import listUsers
from functions.deleteUser import deleteUser
from functions.findUser import findUser
from functions.listOrderUsers import listOrderUsers

import inquirer

options = [
    'Adicionar usuário',
    'listar usuários por ordem de criacão',
    'listar usuários por ordem alfabetica',
    'verificar se o usuário existe na lista', 
    'remover usuário cadastrado', 
    'atualizar usuário cadastrado',
    'encerrar a sessão'
]

questions = [
    inquirer.List('option',
                message="Sobre qual dos assuntos deseja tratar?",
                choices=options,
            ),
]


selectFuntions = {
    "1": addUser,
    "2": listUsers,
    "3": listOrderUsers,
    "4": findUser,
    "5": deleteUser,
    "6": updateUser
}

def main():


    while True:

        answers = inquirer.prompt(questions)

        index = options.index(answers['option'])+1


        if index > 0 and index <= 6:
            selectFuntions[str(index)]()
        elif index == 7:
            print('Certo, vou encerrar a sua conversa! Até logo!')
            break







if(__name__ =="__main__"):
    main()