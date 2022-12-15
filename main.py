# Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.
# если человек регистрирует больше трёх человек на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.

tickets = int(input("количество: "))
total_price = 0

for i in range(tickets):
    age = int(input("возраст: "))
    if age <= 25 and age >=18:
        total_price += 990
    elif age > 25:
        total_price += 1390

if tickets >3:
    total_price = total_price * 0.9

print(total_price)


