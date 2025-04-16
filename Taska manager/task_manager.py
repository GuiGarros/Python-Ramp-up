def options():
    print("1 - Criar tarefa")
    print("2 - Deletar tarefa")
    print("3 - Atualizar tarefa")
    print("4 - Visualizar tarefas")
    print("0 - Sair")


def novaTarefa():
    titulo = input("Titulo da tarefa: ")
    if not titulo.strip(): 
        return None
    titulo = titulo.strip() 
    descricao = input("Descricao: ")
    status = "TODO"
    task = {"titulo": titulo, "descricao": descricao, "status": status}
    return task

def deletarTarefa(tasks, titulo):
    for task in tasks:
        if task["titulo"] == titulo:
            tasks.remove(task)
            print(f"Tarefa '{titulo}' removida com sucesso.")
            return True
        print(f"Tarefa '{titulo}' nao encontrada")
        return False
    
def atualizarTarefas(tasks, titulo, novo_status):
    status_validos = ["TODO", "DOING", "DONE"]
    novo_status = novo_status.upper() #avois minors letters

    if novo_status not in status_validos:
        print(f"Status Inválido. Use: {','}.join(status_validos).")
        return False
    
    for tarefa in tasks:
        if tarefa["titulo"] == titulo:
            tarefa["status"] = novo_status
            print(f"Status da tarefa '{titulo}' atualizado para '{novo_status}'.")
            return True

    print(f"Tarefa '{titulo}' não encontrada.")
    return False

def imprimiTasks(tasks):
    if not tasks:
        print("Nenhuma tarefa cadastrada.")
        return
    
    print("\n=== Lista de Tarefas ===")
    for i, tarefa in enumerate(tasks, start=1):
        print(f"\nTarefa {i}:")
        print(f"  Título     : {tarefa['titulo']}")
        print(f"  Descrição  : {tarefa['descricao']}")
        print(f"  Status     : {tarefa['status']}")
    print("========================\n")


option = None
tasks = []
while option != 0:
    options()
    try:
        option = input("Digite a opcao desejada: ")
        option = int(option)
        if option < 0 or option >4:
            print("Opção inválida. Digite um número de 1 a 4 ou 0 para sair.")
            
        if option == 1:
            task = novaTarefa()
            if task != None:
                tasks.append(task)
                print(tasks)
            else:
                print("A tarefa precisa de um titulo") 
        elif option == 2:
            titulo = input("Digite o titulo da tarefa:")
            deletarTarefa(tasks,titulo)
        elif option == 3:
            titulo = input("Digite o titulo da tarefa que deseja atualizar: ")
            status = input("Digite o novo status [TODO, DOING, DONE]: ")
            atualizarTarefas(tasks, titulo, status)
        elif option == 4: 
            imprimiTasks(tasks)
        



    except ValueError:
        print("ERRO: Por favor, digite apenas numero inteiros!")
