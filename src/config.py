class Config:
    SECRET_KEY = 'mysecretkey'


class DevelopmentConfig(Config):
    # Inicia el servidor en modo depuración
    DEBUG = True
    # Manejo DB
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'ghoprobt'

# Creamos un diccionario para la configuración
config = {
    'development': DevelopmentConfig
}
