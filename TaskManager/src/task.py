from status_enum import Status

class Tarefa:
    def __init__(self, titulo, descricao, status=Status.TODO):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
    
    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descricao": self.descricao,
            "status": self.status.value
        }

    # def from_dict(d):
    #     # Convertendo a string de volta para o Enum quando for lido
    #     status = Status[d['status']] if 'status' in d else Status.TODO
    #     return Tarefa(d['titulo'], d['descricao'], status)
    
    # def atualizar_status(self, novo_status):
    #     status_validos = ["TODO", "DOING", "DONE"]
    #     novo_status = novo_status.upper()
    #     if novo_status not in status_validos:
    #         print(f"Status inválido. Use: {', '.join(status_validos)}.")
    #         return False
    #     self.status = novo_status
    #     print(f"Status da tarefa '{self.titulo}' atualizado para '{self.status}'.")
    #     return True
    
    def __str__(self):
        return f"Título: {self.titulo}\nDescrição: {self.descricao}\nStatus: {self.status}"