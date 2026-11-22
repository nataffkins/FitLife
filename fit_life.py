# FitLife — консольный бот: знакомство, расчёт ИМТ и нормы воды.
# Константы
WATER_PER_KG = 30  # мл воды на 1 кг веса в день
ML_PER_LITER = 1000  # миллилитров в одном литре

# Шаг 1 Знакомство
print("Здравствуйте! Я бот FitLife.")
print("Я помогу Вам рассчитать индекс массы тела и норму потребления воды.")

user_name = input("Как вас зовут? ")
user_age = int(input("Сколько вам лет? "))

# Шаг 2 Сбор данных
user_weight = float(input("Введите ваш вес в кг (например, 65.5): "))
user_height = float(input("Ваш рост в метрах (например, 1.75): "))

# расчёт индекса массы тела
bmi = user_weight / (user_height ** 2)
bmi = round(bmi, 1)

# расчёт нормы воды
water_ml = user_weight * WATER_PER_KG
water_l = water_ml / ML_PER_LITER

# Шаг 3 Вывод результата
print()
print(f"Отчет для пользователя: {user_name} ({user_age} г.)")
print(f"Твой Индекс Массы Тела: {bmi}")
print(f"Рекомендуемая норма воды: {water_l:.1f} л. в день")
print()
print("Расчет окончен. Будьте здоровы!")
