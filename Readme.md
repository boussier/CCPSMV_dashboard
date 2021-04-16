# Django Rest api

### Getting Started

### Clone or pull project
```
git clone projet repository or
git pull origin main
```
### Environment variables
The following environemnt variables must be setted in a file called .env and palced at the project root directory: 
LOAD_INITIAL_DATA=True or Falase
POSTGRES_DB= databse name
POSTGRES_USER= database user
POSTGRES_PASSWORD= database password
POSTGRES_HOST= (should be setted to db)
POSTGRES_PORT= (5433)
API_PORT= api port
SECRET_KEY= Django secret key (should be unique and secret)
DEBUG=should be equal to True for developpement purpose and to False in production environement

### Build the image
```
docker-compose build
```
### Run the api
```
docker-compose up
```
By default, the following admin user is created:
```
login: admin@admin.com
password: admin
```
### Access
```
The rest api is accessible at the url: /api
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

