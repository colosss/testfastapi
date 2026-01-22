"""
Docstring for users.crud

Create
Read
Update
Delete
  |
 \ /
CRUD
"""


from users.schemas import CreateUser

def create_user(user_in:CreateUser):
    user=user_in.model_dump()
    return{
        "success": "success",
        "user": user,
    }

