from pydantic import BaseModel, field_validator, model_validator



class User(BaseModel):
    username: str

    @field_validator("username")
    def username_validator(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v


class Signup(BaseModel):
    username: str
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def password_match_validator(self):
        if len(self.password) < 8:
            raise ValueError("Password must be at least 8 characters")
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self
