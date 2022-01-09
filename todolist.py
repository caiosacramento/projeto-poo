class Tarefa:
  def __init__(self, titulo, data, categoria, status='Pendente'):
    self.titulo = titulo
    self.data = data
    self.categoria = categoria
    self.status = status

  def alterar_status(self):
    if self.status == 'Pendente':
      self.status = 'Concluido'
    elif self.status == 'Concluido':
      self.status = 'Pendente'

  def remover_tarefa(self, titulo):
    pass
    #return

  def visualizar_tarefa(self, data_requerida):
    pass
    #return print()

  def __repr__(self):
    return f'{self.titulo}, {self.data}, {self.categoria}, {self.status}'


todolist = {}

fechar = 1

while fechar!=0:
  titulo = input('Digite o titulo da tarefa: ')
  data = input('Digite a data da tarefa: ')
  categoria = input('Digite a categoria da tarefa: ')

  tarefa = Tarefa(titulo, data, categoria)
  todolist[tarefa.titulo] = {tarefa.data, tarefa.categoria}
  #print(tarefa.titulo)

  fechar = int(input('Deseja continuar? 1=Deseja continuar, 0= Encerrar programa: '))

print(todolist)