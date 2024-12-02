{
  "courts": [
    {
      "id": 1,
      "name": "Футбольное поле №1",
      "location": "Москва, ул. Ленина, д. 10",
      "description": "Отличная футбольная площадка с искусственным покрытием.",
      "price_per_hour": 2000,
      "availability": ["09:00-12:00", "13:00-16:00"]
    },
    {
      "id": 2,
      "name": "Теннисный корт №2",
      "location": "Санкт-Петербург, пр-т Невский, д. 20",
      "description": "Современный теннисный корт с профессиональным освещением.",
      "price_per_hour": 1500,
      "availability": ["08:00-11:00", "14:00-17:00"]
    }
  ]
}
{
  "bookings": [
    {
      "court_id": 1,
      "date": "2023-05-01",
      "time_slot": "09:00-12:00",
      "customer_name": "Иван Иванов",
      "phone_number": "+7 999 123-45-67"
    },
    {
      "court_id": 2,
      "date": "2023-06-15",
      "time_slot": "14:00-17:00",
      "customer_name": "Петр Петров",
      "phone_number": "+7 888 987-65-43"
    }
  ]
}
from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Загрузка данных из файлов при старте сервера
with open('courts.json', 'r') as f:
    courts_data = json.load(f)

with open('bookings.json', 'r') as f:
    bookings_data = json.load(f)

@app.route('/courts', methods=['GET'])
def get_courts():
    return jsonify(courts_data), 200

@app.route('/bookings', methods=['GET'])
def get_bookings():
    return jsonify(bookings_data), 200

@app.route('/booking', methods=['POST'])
def create_booking():
    data = request.get_json()
    
    # Проверка обязательных полей
    required_fields = ['court_id', 'date', 'time_slot', 'customer_name', 'phone_number']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Не все обязательные поля заполнены'}), 400
    
    # Добавление новой брони
    booking_id = len(bookings_data['bookings']) + 1
    data['id'] = booking_id
    bookings_data['bookings'].append(data)
    
    # Сохранение изменений в файл
    with open('bookings.json', 'w') as f:
        json.dump(bookings_data, f, indent=2)
        
    return jsonify({"message": "Бронирование успешно создано"}), 201

if __name__ == '__main__':
    app.run(debug=True)
