class Config:
    SECRET_KEY ='B!1weNAt1T^%kvhUI*S^'

class DevelopmentConfig(Config):
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'jlramirez'
    MYSQL_PASSWORD = 'Aguila17.'
    MYSQL_DB = 'flask_login'

config = {
    'development': DevelopmentConfig
}    