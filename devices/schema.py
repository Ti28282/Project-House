from pydantic import BaseModel, Field, root_validator, Extra, validator


class DeviceSchema(BaseModel):
    device_id: str = Field(min_length = 15, max_length = 50)
    user_id: int = Field(ge = 1)
    device_name: str = Field(min_length = 4, max_length = 20)
    device_type: str = Field(min_length = 4, max_length = 40)
    ip: str =  Field(min_length = 7, max_length = 20)
    online: bool = False


    @validator('ip')
    def validate_ip(cls, value):
        if not all(part.isdigit() and 0 <= int(part) <= 255 for part in value.split('.')):
            raise ValueError("Uncorrecrt IP-address")
        return value