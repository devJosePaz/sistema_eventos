import pandas as pd
from utils import filtrar, adicionar_evento

# Lista inicial de eventos
eventos = [
    {'Data': '2024-10-01', 'Título': 'Reunião de Equipe', 'Descrição': 'Reunião semanal', 'Local': 'Sala 1'},
    {'Data': '2024-10-05', 'Título': 'Workshop de Python', 'Descrição': 'Aprender Pandas', 'Local': 'Sala 2'},
]

# Cria o DataFrame da lista de eventos
df = pd.DataFrame(eventos)

def mostrar_menu():
    print("\nMenu de Eventos:")
    print("1. Adicionar Evento")
    print("2. Excluir Evento")
    print("3. Filtrar Eventos")
    print("4. Sair")

def excluir_evento(dataframe):
    """Solicita ao usuário o título do evento a ser excluído e remove o evento do DataFrame."""
    titulo = input("Digite o título do evento que deseja excluir: ")
    dataframe = dataframe[dataframe['Título'] != titulo]
    return dataframe

while True:
    mostrar_menu()
    escolha = input("Escolha uma opção (1-4): ")

    if escolha == '1':
        df = adicionar_evento(df)
        print("Evento adicionado com sucesso!")
    elif escolha == '2':
        df = excluir_evento(df)
        print("Evento excluído com sucesso!")
    elif escolha == '3':
        mes_desejado = int(input("Digite o mês desejado (1-12): "))
        ano_desejado = int(input("Digite o ano desejado: "))
        eventos_filtrados = filtrar(df, mes=mes_desejado, ano=ano_desejado)
        print("Eventos filtrados:")
        print(eventos_filtrados)
    elif escolha == '4':
        break
    else:
        print("Opção inválida. Tente novamente.")

# Salva o DataFrame atualizado como CSV
df.to_csv('eventos.csv', index=False)

# Exibe o DataFrame atualizado ao sair
print("\nEventos finais:")
print(df)
