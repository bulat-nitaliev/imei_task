from pydantic import BaseModel


class Imei(BaseModel):
    imei_or_sn:str