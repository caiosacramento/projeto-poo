import csv
class Tarefa:
  def __init__(self, titulo, data, categoria, status='Pendente',ativo= 1):
    self.titulo = titulo
    self.data = data
    self.categoria = categoria
    self.status = status
    self.ativo = ativo
  
  def alterar_status(self):
    if self.status == 'Pendente':
      self.status = 'Concluido'
    elif self.status == 'Concluido':
      self.status = 'Pendente'

  def remover_tarefa(titulo):
    with open ('base_de_dados.csv') as arquivo: 
      tabela = csv.reader(arquivo, delimiter=';', lineterminator='\n') 
 
      conteudo = list(tabela) 
 
    for linha in conteudo: 
      if linha[0] == titulo: 
        linha[4] = 0 
    
    with open ('base_de_dados.csv', 'w') as arquivo: 
      escritor = csv.writer(arquivo, delimiter=';', lineterminator='\n') 
      escritor.writerows(conteudo)
    print(f'a atividade de titulo {titulo}, foi removida!')
  
  def visualizar_tarefa(data_requerida):
    with open ('base_de_dados.csv') as arquivo: 
      tabela = csv.reader(arquivo, delimiter=';', lineterminator='\n') 
 
      conteudo = list(tabela) 
 
    for linha in conteudo: 
      if linha[1] == data_requerida and linha[4] == '1': 
        print(linha)
  
  def criar_tarefa(self):
    with open('base_de_dados.csv', 'a') as arquivo:
      tabela = csv.writer(arquivo, delimiter=';', lineterminator='\n')
      tabela.writerow([self.titulo, self.data, self.categoria, self.status, self.ativo])

  def __repr__(self):
    return f'{self.titulo}, {self.data}, {self.categoria}, {self.status}'


menu = input('digite a opção que você gostaria de seguir (1- cadastrar nova tarefa, 2- remover uma tarefa, 3- visualizar uma tarefa, 0- sair do programa): ')
while menu!='0': 
  if menu == '1':
    titulo = input('Digite o titulo da tarefa: ')
    data = input('Digite a data da tarefa: ')
    categoria = input('Digite a categoria da tarefa: ')

    tarefa = Tarefa(titulo, data, categoria)
    tarefa.criar_tarefa()
  
  if menu == '2':
    titulo = input('Digite o titulo da tarefa que irá ser removida: ')  
    Tarefa.remover_tarefa(titulo)
  
  if menu == '3':
    data = input('Digite a data da tarefa que você deseja visualizar: ')  
    Tarefa.visualizar_tarefa(data)

  menu = input('digite a opção que você gostaria de seguir (1- cadastrar nova tarefa, 2- remover uma tarefa, 3- visualizar uma tarefa, 0- sair do programa): ')

#print(todolist)