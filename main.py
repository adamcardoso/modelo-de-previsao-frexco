import pandas as pd  # pip install pandas
import matplotlib.pyplot as plt  # pip install matplotlib
from statsmodels.tsa.arima.model import ARIMA  # pip install statsmodels

try:
    data = pd.read_excel('dados.xlsx')  # leitura de dados
    data_frame = pd.DataFrame(data)  # criação de data frame
    data_frame['Data'] = pd.to_datetime(data_frame['Data'], format='%d/%m/%Y')  # conversão de data
    data_frame.set_index('Data', inplace=True)  # definição de índice
except Exception as e:
    print(f'Erro ao carregar dados: {e}')  # tratamento de exceção
    exit(1)  # encerramento do programa


