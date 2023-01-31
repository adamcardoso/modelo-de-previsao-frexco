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

try:
    plt.plot(data_frame['Vendas'])  # plotagem de gráfico
    plt.show()  # exibição de gráfico
except Exception as e:
    print(f'Erro ao plotar gráfico: {e}')  # tratamento de exceção
    exit(1)  # encerramento do programa

try:
    model = ARIMA(data_frame['Vendas'], order=(3, 1, 0))  # criação de modelo ARIMA
    model_fit = model.fit()  # treinamento de modelo
    print(model_fit.summary())  # exibição de resumo
    future_predictions = model_fit.forecast(steps=5)[0]  # previsão de demanda
    future_predictions = round(future_predictions, 2)  # arredondamento de previsão
    print("Previsão de demanda para os próximos 5 dias:", future_predictions)  # exibição de previsão
except Exception as e:
    print(f'Erro ao treinar ou prever modelo ARIMA: {e}')  # tratamento de exceção
    exit(1)  # encerramento do programa
