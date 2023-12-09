from fastapi import FastAPI, Response, status, HTTPException,Depends,APIRouter
from .. import models,schemas,utils,oauth2
from sqlalchemy.orm import Session
from ..database import engine,get_db 
from typing import Optional,List

router = APIRouter(
    prefix = "/posts",
    tags = ['Posts'] # For website docs
)

@router.get("/",response_model = List[schemas.Post])
def get_post(db: Session=Depends(get_db),current_user:int = Depends(oauth2.get_current_user),limit:int=10, skip:int=0,search:Optional[str] = ""):
    # cursor.execute("""SELECT * from posts """) # make a query
    # posts = cursor.fetchall()

    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    return posts


@router.post("/", status_code=status.HTTP_201_CREATED,response_model=schemas.Post)
#def create_posts(post:schemas.PostCreate,db: Session=Depends(get_db)):
def create_posts(post:schemas.PostCreate,db: Session=Depends(get_db),current_user:int = Depends(oauth2.get_current_user)): # Extract fields from the body(in postman)
    # cursor.execute("""INSERT INTO posts(title,content) VALUES(%s, %s) RETURNING * """, (post.title,post.content))
    # new_post = cursor.fetchone() # get whatever returned from cursor.execute()
    # conn.commit() # push changes to postgresql

    new_post = models.Post(owner_id = current_user.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@router.get("/{id}",response_model=schemas.Post)
def get_post(id:int,db:Session=Depends(get_db)):
    # cursor.execute("""select * from posts where id = %s returning * """, (str(id)))
    # post = cursor.fetchone()
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"post with id:{id} was not found")
    return post


@router.delete("/{id}")
def delete_post(id:int,db:Session=Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    # cursor.execute("""Delete from posts where id = %s returning * """, (str(id)))
    # post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None: raise HTTPException(status_code=status.HTTP_204_NO_CONTENT,detail = f"204 no content id: {id}")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = f"Not authorized to perform requested action")

    post_query.delete(synchronize_session=False)
    db.commit()
    return {"status":"successfully removed"}


@router.put("/{id}",response_model=schemas.Post) 
def update_post(id:int,new_post:schemas.PostCreate,db:Session=Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):
    # cursor.execute("""update posts set title = %s,content = %s where id = %s returning * """,(post.title,post.content,(str(id))))
    # updated_post = cursor.fetchone()
    # conn.commit()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"not found id: {id}")
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail = f"Not authorized to perform requested action")
    post_query.update(new_post.model_dump(), synchronize_session=False)
    db.commit()
    return post


