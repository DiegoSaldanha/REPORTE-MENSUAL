#regla 1

import pandas as pd
#ruta del archivo csv intermedio
 try: 
#leer el archivo csv
data = pd.read_csv(archivo_csv)

#ordenar los datos por nombre
data_ordenada = data.sort_values(by='Nombre1')


#nuevas reglas por directorio telefonico


# Exportar a Excel
archivo_excel = 'clientes_ordenados.xlsx'
data_ordenada.to_excel(archivo_excel, index=False)
    
print(f"Datos exportados exitosamente a {archivo_excel}")
except Exception as e:
print(f"Error al transformar los datos: {e}")