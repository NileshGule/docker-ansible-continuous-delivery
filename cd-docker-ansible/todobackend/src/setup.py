from setuptools import setup, find_packages

setup (
    name                    = "todobackend",
    version                 = "0.1.0",
    description             = "Todobackend Django REST service",
    packages                = find_packages(),
    include_package_data    = True,
    scripts                 = ["manage.py"],
    install_requires        = [
                                "Django==1.9",
                                "django-cors-headers==1.1.0",
                                "django-nose==1.4.4",
                                "djangorestframework==3.3.0",
                                "MySQL-python==1.2.5",
                                "packaging==16.8",
                                "pyparsing==2.2.0",
                                "uwsgi>=2.0"
                            ],
    extras_require          = {
                                "test": [
                                            "colorama==0.3.9",
                                            "coverage==4.3.4",
                                            "django-nose==1.4.4",
                                            "nose==1.3.7",
                                            "pinocchio==0.4.2"
                                        ]
                                }
)
