from db import get_connnection

# try:
#     connection = get_connnection()
#     with connection.cursor() as cursor:
#         cursor.execute('call consultar_alumnos()')
#         resultset = cursor.fetchall()
#         for row in resultset:
#             print(row)
# except Exception as ex:
#     print(ex)

# try:
#     connection = get_connnection()
#     with connection.cursor() as cursor:
#         cursor.execute('call consulta_alumnos(%s)', (2,))
#         resultset = cursor.fetchall()
#         print(resultset)
# except Exception as ex:
#     print(ex)

try:
    connection = get_connnection()
    with connection.cursor() as cursor:
        cursor.execute('call agregar_alumnos(%s, %s, %s)', (22,))
        resultset = cursor.fetchall()
        print(resultset)
except Exception as ex:
    print(ex)