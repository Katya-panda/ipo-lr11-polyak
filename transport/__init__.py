# импортируем классы из модулей пакета transport
from .client import Client
from .vehicle import Vehicle
from .airplane import Airplane
from .van import Van
from .transport_company import TransportCompany
__all__ = [
    "Client",
    "Vehicle",
    "Airplane",
    "Van",
    "TransportCompany"
]