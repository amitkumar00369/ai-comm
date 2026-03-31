from enum import Enum

class RoomType(str, Enum):
    ONE_BHK = "0"
    TWO_BHK = "1"
    THREE_BHK = "2"
    FOUR_BHK = "3"

class userType(str, Enum):
    user="user"
    admin="admin"
    subAdmin="subAdmin"

class bookingType(str,Enum):
    pending = "0"
    accepted = "1"
    completed = "5",
    cancelled = "6",