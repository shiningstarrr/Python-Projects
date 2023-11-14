# Introduction: Python API Development 
- Video link: https://www.youtube.com/watch?v=0sOvCWFmrtA
- Including Authentication, CRUD Operation, Validation, Documentation
- Will be familar with  []Alembic: database migration tools
                        []Postman: construct HTTP packets
                        []Postgresql
                        []Ubuntu, Heroku: deployment
                        []Docker, fast API


# Setting up:
- Create a virtual environment: ```py -3 -m venv apivenv```
- Switch python interpreter to venv version 
- Switch terminal to venv (use cmd rather than powershell): ```apivenv\Scripts\activate.bat```


# Resources:
- FastAPI documentation: https://fastapi.tiangolo.com/tutorial/
- http methods: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- Python decorator
- Postgres data types: https://www.postgresql.org/docs/current/datatype.html 
- Fastapi password hashing: https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/
- https://acropolium.com/blog/most-popular-backend-frameworks-in-2021-2022-pros-and-cons-what-to-choose/


# Starting FastAPI - host website in Python:
- Create a url path: @app.get("\") -> decorator+http requests+url
- Run fastAPI: ```uvicorn main:app``` or ```uvicorn main:app --reload``` [uvicorn + filename + app instance]
- Test path operation: using Postman
- get: 
    ``` ruby
    @app.get("/")
    def get_user():
        return {"message": "Hello!"}
    ```
## Schema Validation with Pydantic
- post: Extract fields from the body where you can add JSON code in Postman -> Body, and use BaseModel from Pydantic to create the input schema.
    ```ruby
    from pydantic import BaseModel
    class Post(BaseModel):
        title:str
        content:str
        rating:Optional[int] = None # or: rating: str | None = none
    @app.post("/createposts")
    def create_posts(new_post: Post):
        print(new_post.model_dump()) # convert to dictionary
        return{"data":newpost}
    ```
## CRUD(Create, Read, Update, Delete) Operations
-   Create -> @app.post()
    Read   -> @app.get()
    Update -> @app.put/patch()
    Delete -> @app.delete()
## Path Parameter & Path Validation
- ```@app.get("/posts/{id}")```
## Http status code
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- Change response status code:
```ruby 
        from fastapi import FastAPI,Response,status,HTTPException
        # method 1:
        response.status_code = status.HTTP_404_NOT_FOUND  
        # method 2:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail =f"post with id: {id} was not found")
```
- Change status code for a specific path operation
## Deleting & Updating posts
- ```@app.delete("/posts/{id}")```
- ```@app.put("/posts/{id}")```
## Fastapi Documentation
- url+/docs
## Create Python Package
- Create a file with name and put ```__init__.py``` file into it.


# Connect to PostgreSQL database from Python script
Database Management System (DBMS):
- Relational DBMS: Mysql, Postgresql, Oracle, Sql server
- Nosql DBMS: MongoDB, DynamoDB, ORACLE, SQl server
## Postgressql -> pgAdmin4
- Create servers, databases, tables (under schemas)
## Connet to database with python
- Postgres driver: Psycopg2
- Updating pip: ```python.exe -m pip install --upgrade pip```
- Install psycopg2: ```pip install psycopg2``
- Connect to database: 
```ruby
try:
    conn = psycopg2.connect(host = 'localhost',database='fastapi',user='postgres',password='Gnaw2011',cursor_factory=RealDictCursor)
    cursor = conn.cursor() # A cursor is a database object that allows you to traverse the results of a SQL query one row at a time.
    print("database connection was successful")
except Exception as error: 
    print("connecting to dataabse failed, error: ", error)
    
@app.get("/posts")
def get_post():
    cursor.execute("""SELECT * from posts """) # make a query
    posts = cursor.fetchall()
    return {"current_posts":posts}

@app.put("/posts/{id}")
def update_post(id:int,post:Post):
    cursor.execute("""update posts set title = %s,content = %s where id = %s returning * """,(post.title,post.content,(str(id))))
    updated_post = cursor.fetchone()
    conn.commit()
    if not updated_post: raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found id: {id}")
    return {"data":updated_post}
```
- Push changes to postgresql: ```conn.commit()```


# Object Relational Mapper (ORM) intro
- ORM: converting data between a relational database and the heap of an object-oriented programming language.
        · Sqlalchemy is one of the most popular ORMs
- Installation: ```pip install sqlalchemy```
- [Connect to various databases]:(https://docs.sqlalchemy.org/en/20/core/engines.html#postgresql)
- Setting up: create database(database.py) and tables(models.py) seperately, and call them in main file.
In database.py:
```ruby 
        SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:Gnaw2011@localhost/fastapi'
        # URL format: 'postgresql://<username>:<password>@<ip-address/hostname>'
        engine = create_engine(SQLALCHEMY_DATABASE_URL) 
        SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)
        Base = declarative_base()
        def get_db():
            db = SessionLocal()
            try:
                yield db
            finally:
                db.close()
```
In models.py:
```ruby
        class Post(Base):
            __tablename__ = "posts"
            id = Column(Integer,primary_key=True,nullable=False)
            title = Column(String,nullable=False)
            content = Column(String,nullable=False)
            created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
```
In main.py: ```rubymodels.Base.metadata.create_all(bind=engine)```
- Pass into path operation function: 
```ruby
        @app.get("/sqlalchemy")
        def test_posts(db: Session=Depends(get_db)):
            posts = db.query(models.Post).all()
            return {"data":posts}

        @app.post("/posts", status_code=status.HTTP_201_CREATED)
        def create_posts(post:Post,db: Session=Depends(get_db)): 
            new_post = models.Post(title = post.title,content = post.content)
            db.add(new_post) 
            db.commit() # push to database
            db.refresh(new_post) # retrieve post and stored back to variable new_post
            return{"data":new_post}

```
- Use Alembic to modify database attributes without deleting and recreating tables.
- more efficient way to extract from pydantic: 
```ruby
        @app.post("/posts", status_code=status.HTTP_201_CREATED)
        def create_posts(post:Post,db: Session=Depends(get_db)):
            new_post = models.Post(**post.model_dump())
            db.add(new_post)
            db.commit()
            return {"data":new_post}
```


# Schema Models
- Schema/Pydantic models define the structure of a request or response. This ensure that when a user wants to create a post, the request will only go through it if it has a "title" and "content" in the body.
- SQlAlchemy model responsible for defining the column of the "posts" table within postgres, which is used to query, create, delete, and update entries within the database.
## Response Model
- convert sqlalchemy model to pydantic model: ```class Config: orm_mode = True```
- add ```@app.get("/posts/{id}",response_model=schemas.post)``` into path operation to restrict what returns to users


# User Table and Password Hashing
- create users table in schemas, create function same as posts
## Password Hashing
- run command ```pip install passlib[bcrypt]```
- set up bcrypt:
 ```ruby
    from passlib.context import CryptContext
    pwd_context  = CryptContext(schemes=["bcrypt"],deprecated = "auto")
 ```
 - In the function add:
```ruby 
@app.post("/users",status_code=status.HTTP_201_CREATED,response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db:Session = Depends(get_db)):
    # hash the password - user.password
    hashed_password = pwd_context.hash(user.password)
    user.password = hashed_password
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
```
## Retrieve user information:
```ruby
@app.get('/users/{id}',response_model=schemas.UserOut)
def get_user(id:int,db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"user with id:{id} does not exist")
    return user
```


# FastAPI Routers 
- APIRouter class is used to group path operations, for example to structure an app into multiple files.
- seperate path operations in main file into post and user file use ```router = APIRouter()```, and add```app.include_router(post.router)``` 
- simplify path operation:
```ruby
    router = APIRouter(
        prefix = "/posts",
        tags = ['Posts'] # add tags on docs
    )
```
- documentation from SwaggerUI: ```http://127.0.0.1:8000/docs```


# JWT Token Autentication
## Hashing password
- Token incldues Header (metadata about the token), Signature, and Payload (message to send).
- Signature includes Header + Payload + Secret + Algorithm
- add verify function in utils:
```ruby
def verify(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)
```
## Python - jose
- Create ayth.py file and finish password verify system.
- Cnstall OAuth2: ```pip install python-jose[cryptography]```
- Add ```create_access_token()``` function in OAuth2
```ruby
SECRET_KEY,ALGORITHM,ACCESS_TOKEN_EXPIRE_TIME_MINUTES  = "Hello","HS256",30
def create_access_token(data:dict):
    to_encode =  data.copy()
    expire = datetime.now()+timedelta(minutes=ACCESS_TOKEN_EXPIRE_TIME_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt
```
- In auth.py: ```access_token = oauth2.create_access_token(data = {"user_id":user.id})```
- JWT Token can be decryped on: jwt.io 
- OAuth2PasswordRequestForm will return username and password: In postman rather than raw, need to choose Body -> Form data 
```ruby
def login(user_credentials:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(database.get_db)):
```
- After adding authentication in create_post function, select postman -> header -> hidden headers -> add authorization: bearer + token, or postman -> Authorization -> Type -> Enter token


# Postman advanced Features
- Add new environment in Postman and go to request, change: ```http://127.0.0.1:8000/posts``` -> ```{{URL}}posts```
- Add environment for JWT Token in Postman -> Request -> Test and code: ```pm.environment.set("JWT", pm.response.json().access_token);``` 
    + In other request which need authentication: go to Authorization -> Token -> put in the variable name {{JWT}}


# Postgres Foreign keys & SqlAlchemy Foreign Keys
- PgAdmin: Table -> Properties -> Constraints -> Naming [table_name_that_work_on + another_table_name + fkey] -> Set up Column: name of the column we want to create + reference table name and column name -> Set up Action
- Sqlalchemy: 
```ruby
owner_id = Column(Integer,ForeignKey("users.id", ondelete="CASCADE", nullable = False))
```

# Only Retrieving Logged in User's
```ruby
posts = db.query(models.Post).filter(models.Post.owner_id == current_user.id).all()
```

# SqlAlchemy Relationships
- In models.py: ```owner = relationship("User")```
- In schemas.py: add in post ```owner:UserOut```

# Query Parameters
- Query parameters are parameters added to the end of a URL to provide extra information to a web server when making requests. 
- Ex: ```{{URL}}posts?limit=3&skip=2&search=dudu%20lala``` %20 means space in URL
```ruby
def get_post(db: Session=Depends(get_db),current_user:int = Depends(oauth2.get_current_user),limit:int=10, skip:int=0,search:Optional[str] = ""):
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts
```

# Env Variables
- Command -> Edit System Environment -> System Properties -> Environment variable -> Add New
- In Command Prompt: use ```echo %variable_name%```
- Ex in py file: 
```ruby
import os
path = os.getenv("Path")
print(path)
```
- Create a .env file to store environment variables


# Vote/Like Theory
- Composite keys: primary key that spans multiple columns.





9:26:36 Votes Table
9:31:33 Votes Sqlalchemy
9:34:11 Votes Route
9:52:31 SQL Joins














------------------------------------------------------------------------------------------------------------------

Notes:
# SQLAlchemy
- [Connect to various databases]:(https://docs.sqlalchemy.org/en/20/core/engines.html#postgresql)
- Querying the database: 
    + db.query.count()
    + db.query.all()
    + db.query.all()[:3]
    + db.query.first()
    + db.query.filter(...).all()
    + db.query.join(...).filter(...).all()
    + db.query.order_by(desc(...)).all()
    + db.query.limit(3).all()
    + db.query.offset(3).all()
    + db.filter().update()


# Take away: 
- from . import _ means import from current directory