from task import Tarefa
from db import tarefas_collection
from status_enum import Status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def nova_tarefa(self):
        titulo = input("Titulo da tarefa: ").strip()
        if not titulo:
            print("A tarefa precisa de um titulo") 
            return 
        descricao = input("Descricao: ").strip()
        tarefa = Tarefa(titulo, descricao)
        if tarefas_collection.find_one({"titulo": titulo}):
            print("Já existe uma tarefa com esse titulo.")
            return
        tarefas_collection.insert_one(tarefa.to_dict())
        print(f"Tarefa '{titulo}' criada com sucesso.")

    def deletar_tarefa(self, titulo):
        resultado = tarefas_collection.delete_one({"titulo": titulo})
        if resultado.deleted_count:
            print(f"Tarefa '{titulo}' removida.")
        else:
            print(f"Tarefa '{titulo}' não encontrada.")
            
    def atualizar_tarefa(self, titulo, novo_status):
        try:
            novo_status = Status[novo_status.upper()]  # Tentando mapear para o Enum
        except KeyError:
            print(f"Status inválido. Use: {[status.name for status in Status]}")
            return False

        resultado = tarefas_collection.update_one(
            {"titulo": titulo},
            {"$set": {"status": novo_status.value}}
        )
        if resultado.modified_count:
            print(f"Tarefa '{titulo}' atualizada para '{novo_status}'.")
        else:
            print(f"Tarefa '{titulo}' não encontrada.")
        
    def imprimir_tarefas(self):
        tarefas = list(tarefas_collection.find())
        if not tarefas:
            print("Nenhuma tarefa encontrada")
            return
        
        print("\n=== Lista de Tarefas ===")
        
        for i, tarefa in enumerate(tarefas, 1):
            print(f"\nTarefa {i}:")
            print(f"  Título: {tarefa['titulo']}")
            print(f"  Descrição: {tarefa['descricao']}")
            print(f"  Status: {tarefa['status']}")
            print("-" * 30)  # Linha separadora para cada tarefa

        print("========================\n")
        input("Pressione Enter para continuar...")