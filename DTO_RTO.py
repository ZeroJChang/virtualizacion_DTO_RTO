import pyodbc

server = 'ZEROJCHANG'
database = 'AdventureWorks2019'
username = 'admin'
password = '1234'
driver = 'ODBC:2019'

# Definición del RTO (por ejemplo, 30 segundos como tiempo máximo para conectar)
RTO = 30

# Definición del DTO (por ejemplo, 5 segundos como tiempo máximo de ejecución de la consulta)
DTO = 5

try:
    conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server +
                          ';DATABASE=' + database + ';UID=' + username +
                          ';PWD=' + password, timeout=RTO)
    # Establecer el tiempo máximo de ejecución de la consulta
    conn.timeout = DTO
    
    # Crear un cursor para ejecutar la consulta
    cursor = conn.cursor()

    # Ejecutar la consulta SQL
    cursor.execute("SELECT * FROM HumanResources.Employee")

    for row in cursor:
        print(row)

    # Cerrar el cursor y la conexión
    cursor.close()
    conn.close()

except pyodbc.Error as e:
    # En caso de que se exceda el RTO
    print("Error de conexión a la base de datos:", e)
except pyodbc.DatabaseError as e:
    # En caso de que se exceda el DTO
    print("Error al ejecutar la consulta:", e)
