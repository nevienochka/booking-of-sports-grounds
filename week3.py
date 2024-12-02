   <!DOCTYPE html>
   <html lang="ru">
   <head>
       <meta charset="UTF-8">
       <title>Бронирование спортивных площадок</title>
       <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
   </head>
   <body>
       <div class="container">
           <h1>Список площадок</h1>
           <ul id="fieldsList" class="list-group mb-4"></ul>
           <h2>Создание брони</h2>
           <form id="bookingForm">
               <div class="form-group">
                   <label for="fieldName">Выберите площадку</label>
                   <select id="fieldName" class="form-control" required></select>
               </div>
               <div class="form-group">
                   <label for="bookingDate">Дата бронирования</label>
                   <input type="date" class="form-control" id="bookingDate" required>
               </div>
               <button type="submit" class="btn btn-primary">Забронировать</button>
           </form>
       </div>
       <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>
       <script src="app.js"></script>
   </body>
   </html>
      $(document).ready(function() {
       $.get('path/to/your/api/fields', function(data) {
           const fieldsList = $('#fieldsList');
           const fieldNameSelect = $('#fieldName');
           data.forEach(item => {
               fieldsList.append(`<li class="list-group-item">${item.name}</li>`);
               fieldNameSelect.append(`<option value="${item.id}">${item.name}</option>`);
           });
       });
   });
   