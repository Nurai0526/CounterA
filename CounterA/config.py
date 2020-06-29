import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'there-are-some-keys'



#SECRET_KEY='some-very-strong-key'
