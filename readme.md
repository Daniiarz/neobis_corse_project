# Course project

Neobis course project was created as part of our study plan, using django and django rest framework.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Pipenv package manager is required for creating virtual environment
```
pip install pipenv
```

### Installing

Install all the requirements

```
pipenv install -r requirements.txt
```

Run your virtual environment
```
pipenv shell
```
### Documentation

Documentation was made by swagger and OpenAPI 2.0 and available locally on localhost:8000/

## Running the tests

To run tests use

```
$python manage.py test 
```
### Coverage

You also can use coverage to run tests and get report of how much of your code 
has been covered with tests

To run tests with coverage
```
$python coverage run manage.py test -v 2
```
Get results in terminal
```
$python coverage report 
```
Get results in a html format. Later you can see your results in browser and get more detailed 
information about test coverage
```
$python coverage html
```
## Deployment

Project is not ready for deployment

## Built With

* [Django](https://www.djangoproject.com/) - The web framework used
* [Django REST framework](https://www.django-rest-framework.org/) - The REST framework for django 


## Authors

* **Daniiar Mukash uulu**  - [Daniiarz](https://github.com/Daniiarz)

## License

There is no license for this project :(


