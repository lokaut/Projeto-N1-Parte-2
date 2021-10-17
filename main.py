from functions.updateUser import updateUser
from functions.addUser import addUser
from functions.listUsers import listUsers
from functions.deleteUser import deleteUser
from functions.findUser import findUser
from functions.listOrderUsers import listOrderUsers

listOptions = [
    "1 - Adicionar usuário",
    "2 - listar usuários por ordem de criacão",
    "3 - listar usuários por ordem alfabetica",
    "4 - verificar se o usuário existe na lista",
    "5 - remover usuário cadastrado",
    "6 - atualizar usuário cadastrado",
    "7 - encerrar a sessão"
]

selectFuntions = {
    "1": addUser,
    "2": listUsers,
    "3": listOrderUsers,
    "4": findUser,
    "5": deleteUser,
    "6": updateUser,
}

while True:
    for x in listOptions:
        print(x)

    selectOption = int(input("\nSobre qual dos assuntos deseja tratar? "))

    if selectOption > 0 and selectOption <= 6:
        selectFuntions[str(selectOption)]
    elif selectOption == 7:
        break
    else:
        print("\nPor favor, digite um valor válido da lista \n")