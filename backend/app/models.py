from pydantic import BaseModel
from typing import Optional

class PacketOut(BaseModel):
    timestamp: Optional[float]
    src_ip: Optional[str]
    dst_ip: Optional[str]
    protocol: Optional[str]
    src_port: Optional[int]
    dst_port: Optional[int]
    length: Optional[int]
    info: Optional[str]
