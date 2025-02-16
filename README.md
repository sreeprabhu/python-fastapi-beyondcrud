# python-fastapi-beyondcrud

## windows

### Install python version 3.13.0

### Install fastapi - pip install fastapi

### Install fastapi standard version - pip install "fastapi[standard]"

#### Add python and python/scripts into the system path if not already present

#### Check python version: py --version

#### Goto project folder and create python virtual environment - py -m venv

#### Activate virtual environment - .venv\Scripts\activate

#### To Run Application - fastapi dev src/

### Requirements and Dev versions

#### Install - pip freeze > requirements.txt

### pydantic settings - pip install pydantic-settings

#### helps to read env variables

#### provides optional pydantic features for loading a settings or config class from env variables or secret files

### Database - PostgreSQL

#### create a postgres live db in neon

#### install asyncpg - pip install asyncpg

### ORM - SQLModel(SQLAlchemy)

#### pip install sqlmodel

#### while using PostgreSQL, we shall need to choose a way to interact with the database using the Python language. An Object Relational Mapper does that.

#### An ORM translates between a programming language, such as Python, and a database, like PostgreSQL

#### Basic Working of ORMs:

##### Mapping Objects to Tables - You create Python classes to represent tables in the database.

##### Each object of these classes corresponds to a row in the database table.

##### Interacting with data - You can then interact with these python objects as if they were regular objects in your code, like setting attributes and calling methods.

##### When you perform operations on these objects, like saving or deleting, the ORM translates these actions into the appropriate SQL queries that the database understands.

##### Data Conversion - The ORM handles converting Python data types into database-specific types and vice versa.
