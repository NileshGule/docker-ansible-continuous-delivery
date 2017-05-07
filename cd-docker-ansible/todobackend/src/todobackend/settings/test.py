from base import *
import os

#installed Apps

INSTALLED_APPS += ('django_nose', )
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEST_OUTPUT_DIR = os.environ.get('TEST_OUTPUT_DIR', '.')
NOSE_ARGS = [
    '--verbosity=2',                # verbose output
    '--nologcapture',               # don't output log capture
    '--with-coverage',              # activate coverage report
    '--cover-package=todo1',        # coverage reports will apply to these packages
    '--with-spec',                  # spec style tests
    '--spec-color',
    '--with-xunit',                 # enable xunit plugin
    '--xunit-file=%s/unittests.xml' % TEST_OUTPUT_DIR,
    '--cover-xml',                   # produce xml coverage information
    '--cover-xml-file=%s/covergae.xml' % TEST_OUTPUT_DIR
]


#database
#https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.environ.get('MYSQL_DATABASE', 'todobackend'),
        'USER': os.environ.get('MYSQL_USER', 'todo1'),
        'PASSWORD': os.environ.get('MYSQL_PASSWORD', 'password'),
        'HOST': os.environ.get('MYSQL_HOST', 'localhost'),
        'PORT': os.environ.get('MYSQL_PORT', '3306')
    }
}
