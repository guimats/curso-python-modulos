# Usando calendar para calendários e datas
# https://docs.python.org/3/library/calendar.html
# calendar é usado para coisas genéricas de calendários e datas.
# Com calendar, você pode saber coisas como:
# - Qual o último dia do mês (ex.: monthrange)
# - Qual o nome e número do dia de determinada data (ex.: weekday)
# - Criar um calendário em si (ex.: monthcalendar)
# - Trabalhar com coisas específicas de calendários (ex.: calendar, month)
# Por padrão dia da semana começa em 0 até 6
# 0 = segunda-feira | 6 = domingo
import calendar

for week in calendar.monthcalendar(2022, 12):
    for day in week:
        if day == 0:
            continue
        print(day)

# print(calendar.calendar(2022))
# print(calendar.month(2022, 12))
# print(calendar.monthrange(2022, 12))
# primeiro_dia, ultimo_dia = calendar.monthrange(2022, 12)
# print(list(enumerate(calendar.day_name)))
# print(calendar.day_name[primeiro_dia])
# print(calendar.weekday(2022, 12, ultimo_dia))
# day = calendar.weekday(2022, 12, ultimo_dia)
# print(calendar.day_name[day])
