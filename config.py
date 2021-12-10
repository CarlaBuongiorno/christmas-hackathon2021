import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://something-here'
    MONGO_DBNAME = os.environ.get('MONGO_DBNAME') or 'elf_service'