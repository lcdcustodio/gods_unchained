Gods Unchained - Machine Learning as a Service (MLaaS)
===========


Flask application implementing a REST API in order to expose ML model trained previously. The service returns the card stragegy according card id.


------------

1 - Installation (Guest OS approach)
===========================

Create a virtual environment:

    	# Linux/MacOs
    	python3 -m venv venv-gu #create
    	source venv-gu/bin/activate #activate
    
    	# Windows
    	python -m venv venv-gu #create
    	venv-gu\Scripts\activate.bat #activate

Install version using the following commands:

```
    	git clone https://github.com/lcdcustodio/gods_unchained.git
    	cd gods_unchained
    	pip install -r requirements.txt (to get the dependencies)
```    

Next, initialize the database through:

```
    	python src/db_init.py
```

In order to load dataset into database. The database contains required information for the model training.

Next step is to train the model through: 

```
    	python src/train_model.py
```

The model is ready! Next step is to launch the API service through:

```
    	python src/wsgi.py
```

RESTful API Documentation
=========================
Navigate to the root URL in your terminal to access Swagger doc in order to test the API.

Run Tests
===========================

Run the test suite:

```
    	pytest -v
    	pytest -v --cov=app.strategy  #test coverage
```   

See the test coverage report:

```	
	----------- coverage: platform win32, python 3.9.1-final-0 -----------
	Name                             Stmts   Miss  Cover
	----------------------------------------------------
	src\app\strategy\__init__.py         6      0   100%
	src\app\strategy\controller.py      19      0   100%
	src\app\strategy\model.py           23      1    96%
	src\app\strategy\schema.py           9      0   100%
	src\app\strategy\service.py         39      0   100%
	----------------------------------------------------
	TOTAL                               96      1    99%	
```    


2 - Installation (Container approach using docker)
===========================

Deployment and running in a containerized environment, using docker

```
    	git clone https://github.com/lcdcustodio/gods_unchained.git
    	cd gods_unchained
	docker build -t god_unchained .
	docker run -p <local_port_>:<container_port_> -t god_unchained:latest
``` 	

For container inspection:

``` 
	docker exec -it <CONTAINER ID> /bin/bash
``` 
