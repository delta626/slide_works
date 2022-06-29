ang = input('Язык программирования:')
old = int(input('Сколько Вам лет: '))
opyt = int(input('Ваш опыт: '))
zp = int(input('Желаемая зарплата: '))


if lang =='python' or lang == 'java' or lang == 'javascript':
  if old >= 18 and old <= 65:
    if opyt >= 3:
      if zp <= 60000:
        print("Кандидат подходит")
else:
  print("Кандидат не подходит")
