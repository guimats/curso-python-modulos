# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz

from datetime import datetime
# from pytz import timezone

# timezone
# data = datetime.now(timezone('Asia/Tokyo'))
# data = datetime(2022, 4, 20, 7, 49, 23, tzinfo=timezone('Asia/Tokyo'))

# timestamp
data = datetime.now()
print(data.timestamp())  # Isso está na base de dados
print(datetime.fromtimestamp(1715097984))

# # data_str = '2022-04-20 07:49:23'
# # data_str_formato = '%Y-%m-%d %H:%M:%S'
# data_str = '20/04/2022'
# data_str_formato = '%d/%m/%Y'


# # data = datetime(2022, 4, 20, 7, 49, 23)
# data = datetime.strptime(data_str, data_str_formato)
# print(data)
