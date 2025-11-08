clients = [
    {"id": 1, "name": "Иван Петров", "email": "ivan@mail.com", "phone": "89101112233"},
    {"id": 2, "name": "Мария Смирнова", "email": "maria@mail.com", "phone": "89223334455"},
]

countries = [
    {"id": 1, "name": "Франция"},
    {"id": 2, "name": "Япония"},
    {"id": 3, "name": "Италия"},
]

cities = [
    {"id": 1, "name": "Париж", "country_id": 1},
    {"id": 2, "name": "Токио", "country_id": 2},
    {"id": 3, "name": "Рим", "country_id": 3},
]

hotels = [
    {"id": 1, "name": "Hotel Parisienne", "city_id": 1, "stars": 4},
    {"id": 2, "name": "Tokyo Stay", "city_id": 2, "stars": 5},
]

flights = [
    {"id": 1, "from_city_id": 1, "to_city_id": 2, "price": 500, "duration": 720},
    {"id": 2, "from_city_id": 2, "to_city_id": 3, "price": 450, "duration": 600},
]

bookings = [
    {"id": 1, "client_id": 1, "hotel_id": 1, "flight_id": 1, "date_from": "2025-10-01", "date_to": "2025-10-10"},
    {"id": 2, "client_id": 2, "hotel_id": 2, "flight_id": 2, "date_from": "2025-11-05", "date_to": "2025-11-15"},
]
#1
print("1. Клиенты с бронированиями:")
for booking in bookings:
    for client in clients:
        if client["id"] == booking["client_id"]:
            break
    for hotel in hotels:
        if hotel["id"] == booking["hotel_id"]:
            break
    for city in cities:
        if city["id"] == hotel["city_id"]:
            break
    for country in countries:
        if country["id"] == city["country_id"]:
            break
    print(f'{client["name"]} — {hotel["name"]}, {city["name"]}, {country["name"]}, {booking["date_from"]} - {booking["date_to"]}')

#2
print("\n2. 5★ отели в Японии:")
japan_id = 0
for country in countries:
    if country["name"] == "Япония":
        japan_id = country["id"]
        break

for hotel in hotels:
    for city in cities:
        if city["id"] == hotel["city_id"] and city["country_id"] == japan_id:
            if hotel["stars"] == 5:
                print(f'{hotel["name"]} — {hotel["stars"]}★')

# 3. Кол-во бронирований по клиентам
print("\n3. Кол-во бронирований по клиентам:")
counts = {}
for booking in bookings:
    cid = booking["client_id"]
    if cid in counts:
        counts[cid] += 1
    else:
        counts[cid] = 1

for client in clients:
    cid = client["id"]
    print(f'{client["name"]}: {counts.get(cid, 0)} бронирований')

# 4. Города назначения рейсов
print("\n4. Города, куда летают рейсы:")
dest_ids = []
for flight in flights:
    if flight["to_city_id"] not in dest_ids:
        dest_ids.append(flight["to_city_id"])

for city in cities:
    if city["id"] in dest_ids:
        print(city["name"])

# 5. Стоимость поездок
print("\n5. Стоимость всех поездок (перелёт + отель):")
for booking in bookings:
    for flight in flights:
        if flight["id"] == booking["flight_id"]:
            flight_price = flight["price"]
            break
    date_from = datetime.strptime(booking["date_from"], "%Y-%m-%d")
    date_to = datetime.strptime(booking["date_to"], "%Y-%m-%d")
    days = (date_to - date_from).days
    hotel_cost = days * 100
    total_cost = flight_price + hotel_cost
    print(f'Бронирование {booking["id"]}: {total_cost} у.е.')

# 6. Добавление клиента и бронирования
print("\n6. Добавление нового клиента и бронирования:")
new_client = {"id": 3, "name": "Алексей Козлов", "email": "alex@mail.com", "phone": "89998887766"}
clients.append(new_client)

new_booking = {"id": 3, "client_id": 3, "hotel_id": 1, "flight_id": 1, "date_from": "2025-12-01", "date_to": "2025-12-07"}
bookings.append(new_booking)

print(f'Добавлен клиент: {new_client["name"]}')
print(f'Добавлено бронирование ID {new_booking["id"]}')

# 7. Обновление телефона по email
print("\n7. Обновление телефона по email:")
target_email = "ivan@mail.com"
new_phone = "80000000000"
for client in clients:
    if client["email"] == target_email:
        client["phone"] = new_phone
        print(f'{client["name"]} — новый номер: {client["phone"]}')

# 8. Удаление прошедших бронирований
print("\n8. Удаление просроченных бронирований:")
today = datetime.today()
updated_bookings = []
for booking in bookings:
    date_to = datetime.strptime(booking["date_to"], "%Y-%m-%d")
    if date_to >= today:
        updated_bookings.append(booking)
    else:
        print(f'Удалено бронирование ID {booking["id"]}')
bookings = updated_bookings

# 9. Страна → количество туристов
print("\n9. Страна -> количество туристов:")
country_tourists = {}
for booking in bookings:
    for hotel in hotels:
        if hotel["id"] == booking["hotel_id"]:
            city_id = hotel["city_id"]
            break
    for city in cities:
        if city["id"] == city_id:
            country_id = city["country_id"]
            break
    if country_id in country_tourists:
        country_tourists[country_id] += 1
    else:
        country_tourists[country_id] = 1

for country in countries:
    count = country_tourists.get(country["id"], 0)
    print(f'{country["name"]}: {count} туристов')

# 10. Средняя длительность перелётов
print("\n10. Средняя длительность перелётов:")
total_duration = 0
flight_count = 0
for flight in flights:
    total_duration += flight["duration"]
    flight_count += 1

if flight_count > 0:
    avg_duration = total_duration / flight_coun_
