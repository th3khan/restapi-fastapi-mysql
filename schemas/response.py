from pydantic.generics import GenericModel
from typing import TypeVar, Generic, Optional

DataType = TypeVar("DataType")

class ResponseBase(GenericModel, Generic[DataType]):
    message: str = ""
    data: Optional[DataType] = None