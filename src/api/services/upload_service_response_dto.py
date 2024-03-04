from dataclasses import dataclass
from typing import Optional


@dataclass
class UploadResponseData:
    id: str


@dataclass
class UploadResponseDto:
    status: str
    error: Optional[str] = None
    data: Optional[UploadResponseData] = None
