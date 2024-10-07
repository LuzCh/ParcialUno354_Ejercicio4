import pandas as pd
from sklearn.preprocessing import KBinsDiscretizer

# Cargar el dataset
df = pd.read_csv('movies_data.csv', encoding='ISO-8859-1')

# Mostrar el DataFrame original y sus tipos de datos
print("DataFrame original:")
print(df)
print("\nTipos de datos originales:")
print(df.dtypes)

# Definir las posiciones de las columnas a discretizar
columnas = [2, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Convertir las columnas a tipo float (asegúrate de que estas columnas existan en tu DataFrame)
df.iloc[:, columnas] = df.iloc[:, columnas].astype(float)

# Inicializar el discretizador
discretizer = KBinsDiscretizer(n_bins=5, encode='ordinal', strategy='uniform')

# Discretizar las columnas especificadas
df.iloc[:, columnas] = discretizer.fit_transform(df.iloc[:, columnas])

# Mostrar el DataFrame discretizado
print("\nDataFrame discretizado:")
print(df)  # Imprime todas las columnas

# Guardar el DataFrame discretizado en un archivo Excel
df.to_excel('output_datos_discretizados.xlsx', index=False)

print("Los datos discretizados han sido guardados en 'output_datos_discretizados.xlsx'.")
