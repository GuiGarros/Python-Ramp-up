from task_manager import TaskManager

manager = TaskManager()

def options():
    print("1 - Criar tarefa")
    print("2 - Deletar tarefa")
    print("3 - Atualizar tarefa")
    print("4 - Visualizar tarefas")
    print("0 - Sair")

def menu():
    option = None
    while True:
        options()
        try:
            option = input("Digite a opcao desejada: ")
            option = int(option)
            if option < 0 or option >4:
                print("Opção inválida. Digite um número de 1 a 4 ou 0 para sair.")
                
            if option == 1:
                manager.nova_tarefa()
            elif option == 2:
                titulo = input("Digite o titulo da tarefa:")
                manager.deletar_tarefa(titulo)
            elif option == 3:
                titulo = input("Digite o titulo da tarefa que deseja atualizar: ")
                status = input("Digite o novo status [TODO, DOING, DONE]: ")
                manager.atualizar_tarefa(titulo, status)
            elif option == 4: 
                manager.imprimir_tarefas()
            elif option == 0:
                break
            



        except ValueError:
            print("ERRO: Por favor, digite apenas numero inteiros!")