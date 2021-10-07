card = []

suits = ["Черви", "Бубни", "трефы", "Пики"]
card_type = ["Шесть", "Семь", "Восьем", "Девять", "Десять", "Валет", "Дама", "Кароль", "Туз"]

for suit in suits:
    for type in card_type:
        card.append(suit + " " + type)

print(card)
print(len(card))
