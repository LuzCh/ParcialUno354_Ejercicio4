import pandas as pd
from sklearn.preprocessing import LabelEncoder

# Cargar el dataset
df = pd.read_csv('movies_data.csv', encoding='ISO-8859-1')

# Mostrar el DataFrame original
print("DataFrame original:")
print(df)

# Inicializar el codificador
label_encoder = LabelEncoder()

# Supongamos que tienes varias columnas categóricas
for column in df.select_dtypes(include=['object']).columns:
    df[column] = label_encoder.fit_transform(df[column])

# Mostrar el DataFrame con las columnas codificadas
print("\nDataFrame con columnas codificadas:")
print(df)

df.to_excel('output_datos_LabelEncoder.xlsx', index=False)

print("Los datos han sido guardados en 'output_datos_LabelEncoder.xlsx'.")