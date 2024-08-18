from fastapi import APIRouter, HTTPException
from models import AddUser, UpdateUser
from database import get_conn
from sqlalchemy.orm import sessionmaker
from schemas import Users
from sqlalchemy.exc import SQLAlchemyError

router = APIRouter()

engine = get_conn()

@router.post("/users")
def create_user(data: AddUser):
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    try:
        user_data = Users(
            username=data.username,
            password=data.password
        )
        session.add(user_data)
        session.commit()
        return {"message": "User added successfully", "id": user_data.id}
    
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while adding the user.")
    
    finally:
        session.close()

@router.get("/users")
def get_users():
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    try:
        users = session.query(Users).filter(Users.status == "Active").all()
        return users
    
    except SQLAlchemyError as e:
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while retrieving users.")
    
    finally:
        session.close()

@router.delete("/users/{user_id}")
def delete_user(user_id: str):
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    try:
        user = session.query(Users).filter(Users.id == user_id).first()
        if user:
            user.status = "Inactive"
            session.commit()
            return {"message": "User status updated to Inactive"}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while updating user status.")
    
    finally:
        session.close()

@router.put("/users/{user_id}")
def update_user(user_id: str, data: UpdateUser):
    SessionLocal = sessionmaker(bind=engine)
    session = SessionLocal()

    try:
        user = session.query(Users).filter(Users.id == user_id).first()
        if user:
            if data.username is not None:
                user.username = data.username
            if data.password is not None:
                user.password = data.password
            session.commit()
            return {"message": "User updated successfully"}
        else:
            raise HTTPException(status_code=404, detail="User not found")
    
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error occurred: {e}")
        raise HTTPException(status_code=500, detail="An error occurred while updating the user.")
    
    finally:
        session.close()