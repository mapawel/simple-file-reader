from abc import abstractmethod, ABC
from fastapi import File, UploadFile
from fastapi.responses import JSONResponse


class UploadService(ABC):
    @abstractmethod
    def __init__(self, assets_path):
        pass

    @abstractmethod
    async def upload_scv(self, file: UploadFile = File(...)) -> JSONResponse:
        pass
