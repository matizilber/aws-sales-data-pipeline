import pandas as pd

# Leer archivo original (forzamos separador coma)
df = pd.read_csv("../data/ventas_raw.csv", sep=",")

print("Columnas detectadas:")
print(df.columns)

print("\nDatos originales:")
print(df.head())

df = df.dropna()

df["total"] = df["precio"] * df["cantidad"]

df.to_csv("../data/ventas_procesado.csv", index=False, header=False)

print("\nArchivo procesado correctamente")