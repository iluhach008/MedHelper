from flask import Flask
from flask_cors import CORS

# Приложение
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Импорт ендпоинтов
from routes import *
app.register_blueprint(routes)

# Запуск
print(app.url_map)
app.run(debug=True)