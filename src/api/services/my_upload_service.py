from uuid import uuid4
from os import path
from fastapi import File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import aiofiles
from dataclasses import asdict
from .upload_service_response_dto import UploadResponseDto, UploadResponseData
from .upload_service import UploadService


class MyUploadService(UploadService):
    def __init__(self, assets_path):
        self.assets_path = assets_path

    async def upload_scv(self, file: UploadFile = File(...)) -> JSONResponse:
        try:
            content_type = file.content_type

            if content_type == "text/csv":
                id = str(uuid4())
                file_location = path.join(self.assets_path, f"{id}.csv")
                async with aiofiles.open(file_location, "wb") as file_object:
                    while True:
                        contents = await file.read(1024)
                        if not contents:
                            break
                        await file_object.write(contents)
                return JSONResponse(
                    content=asdict(self.__return_successful_response(id))
                )

            if content_type != "text/csv":
                raise HTTPException(400, "Wrong file type")

        except HTTPException as http_e:
            raise http_e
        except Exception as e:
            raise HTTPException(500, "Internal server error")

    def __return_successful_response(self, id: str) -> UploadResponseDto:
        return UploadResponseDto(
            status="OK", error=None, data=UploadResponseData(id=id)
        )
