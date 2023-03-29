import datetime

# Obtener la fecha y hora actual
now = datetime.datetime.now()

# Formatear la fecha y hora en inglés
formatted_date = now.strftime("%B %d, %Y %I:%M %p")

# Imprimir la fecha y hora formateada
print(datetime.datetime.now().strftime("%B %d, %Y %I:%M %p"))
