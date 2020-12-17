# Django Rest api

### Getting Started

### Clone or pull project
```
git clone projet repository or
git pull origin master
```
### Create an environnement file ".env" at the root of the project with the following variables setted:
```
POSTGRES_DB=db_name
POSTGRES_USER=db_user_name
POSTGRES_PASSWORD=db_password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```
### Build the image
```
docker-compose build
```
### Run the api
```
docker-compose up
```
By default, the folloowing admin user is created:
```
login: admin@admin.com
password: admin
```
### Running the tests
```
docker-compose exec api python manage.py test
```

## Documentation

### Api Schema

Schema is available on url "api/schema/?format=json"

### Swagger

Documentation is available on url or "api/schema/swagger-ui/" or "api/schema/redocs" 

### Other docs

* [Django](https://docs.djangoproject.com/) - The backend web framework used
* [Pip](https://pypi.org/project/pip/) - Dependency Management

## Authors

* **Sylvain Boussier** - *Initial work* - [email](sylvain.boussier@gmail.com)

