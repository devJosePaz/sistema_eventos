import pandas as pd

def filtrar(dataframe, mes=None, ano=None):
    """Filtra o DataFrame de eventos pelo mês e/ou ano especificados."""
    dataframe['Data'] = pd.to_datetime(dataframe['Data'])
    
    if mes is not None:
        dataframe = dataframe[dataframe['Data'].dt.month == mes]
    if ano is not None:
        dataframe = dataframe[dataframe['Data'].dt.year == ano]
    
    return dataframe

def adicionar_evento(dataframe):
    """Solicita ao usuário as informações do evento e adiciona ao DataFrame."""
    data = input("Digite a data do evento (AAAA-MM-DD): ")
    titulo = input("Digite o título do evento: ")
    descricao = input("Digite a descrição do evento: ")
    local = input("Digite o local do evento: ")

    # Cria um dicionário com as informações do evento
    novo_evento = {
        'Data': data,
        'Título': titulo,
        'Descrição': descricao,
        'Local': local
    }

    # Cria um DataFrame para o novo evento
    df_novo_evento = pd.DataFrame([novo_evento])

    # Concatena o novo evento ao DataFrame existente
    dataframe = pd.concat([dataframe, df_novo_evento], ignore_index=True)
    return dataframe

def excluir_evento(dataframe):
    
