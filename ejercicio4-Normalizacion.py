import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Cargar el dataset
df = pd.read_csv('movies_data.csv', encoding='ISO-8859-1')

# Mostrar el DataFrame original y sus tipos de datos
print("DataFrame original:")
print(df)
print("\nTipos de datos originales:")
print(df.dtypes)

# Definir las posiciones de las columnas a normalizar
columnas = [2, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Convertir las columnas a tipo float (asegúrate de que estas columnas existan en tu DataFrame)
df.iloc[:, columnas] = df.iloc[:, columnas].astype(float)

# Inicializar el escalador Min-Max
scaler = MinMaxScaler()

# Normalizar las columnas especificadas
df.iloc[:, columnas] = scaler.fit_transform(df.iloc[:, columnas])

# Mostrar el DataFrame normalizado
print("\nDataFrame normalizado (Min-Max):")
print(df)  # Imprime todas las columnas

# Guardar el DataFrame normalizado en un archivo Excel
df.to_excel('output_datos_normalizados.xlsx', index=False)

print("Los datos han sido guardados en 'output_datos_normalizados.xlsx'.")
