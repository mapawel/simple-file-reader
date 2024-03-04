from os import path
from api import App, MyUploadService, UploadService

assets_path: str = path.join(path.dirname(__file__), "..", "assets")

my_upload_service: UploadService = MyUploadService(assets_path)

app = App(my_upload_service)
