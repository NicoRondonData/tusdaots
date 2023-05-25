from pydantic import BaseModel, EmailStr, Field, validator


class UserLogin(BaseModel):
    username: str
    password: str


class UserResponse(BaseModel):
    username: str


class UserInput(BaseModel):
    username: str
    password: str = Field(max_length=256, min_length=6)
    password2: str
    email: EmailStr

    @validator("password2")
    def password_match(cls, v, values, **kwargs):
        """
        Validate that the password and the confirmation password match.

        Args:
            v (str): The value of the confirmation password.
            values (dict): The values of the fields in the model.

        Returns:
            str: The value of the confirmation password.

        Raises:
            ValueError: If the password and the confirmation password do not match.
        """
        if "password" in values and v != values["password"]:
            raise ValueError("passwords don't match")
        return v
