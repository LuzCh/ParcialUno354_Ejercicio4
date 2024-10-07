import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Cargar el dataset
df = pd.read_csv('movies_data.csv', encoding='ISO-8859-1')

# Mostrar el DataFrame original
print("DataFrame original:")
print(df)

# Inicializar el codificador OneHotEncoder
one_hot_encoder = OneHotEncoder()  # Sin el argumento sparse

# Aplicar OneHotEncoder a las columnas categóricas
encoded_features = one_hot_encoder.fit_transform(df.select_dtypes(include=['object']))

# Crear un DataFrame con las características codificadas
encoded_df = pd.DataFrame(encoded_features.toarray(), columns=one_hot_encoder.get_feature_names_out(df.select_dtypes(include=['object']).columns))

# Concatenar el DataFrame original sin las columnas categóricas
df_encoded = pd.concat([df.reset_index(drop=True), encoded_df.reset_index(drop=True)], axis=1)

# Mostrar el DataFrame con las columnas categóricas codificadas
print("\nDataFrame con columnas categóricas codificadas usando OneHotEncoder:")
print(df_encoded)

# Tomar una muestra de 100 filas para guardar
df_sample = df_encoded.sample(n=100, random_state=1)  # Cambia el número de filas si es necesario

# Guardar la muestra en un archivo Excel
df_sample.to_excel('output_datos_OneHotEncoder_muestra.xlsx', index=False, engine='openpyxl')

print("Los datos han sido guardados en 'output_datos_OneHotEncoder_muestra.xlsx'.")
