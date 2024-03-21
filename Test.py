# a = 1  # погода штиль
a = 2   # слабый дождь
# a = 3   # сильный дождь

#b = 1  # взял зонт
b = 2   # не взял зонт

calm = a == 1  #(штиль)
without_umbrella = b == 2  #(без зонта)

if calm:
    is_dry = True
else:
    if without_umbrella:
        is_dry = False
    else:
        is_dry = True
print(is_dry)  # является ли человек сухой
# Придумать способ и реализвцию ветвления при а=2 и а=3
