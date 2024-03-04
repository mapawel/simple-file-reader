from fastapi import FastAPI
from .services.upload_service import UploadService


class App(FastAPI):
    def __init__(self, upload_service: UploadService):
        FastAPI.__init__(self)
        self.upload_service = upload_service
        self.add_api_route("/upload", self.upload_service.upload_scv, methods=["POST"])
