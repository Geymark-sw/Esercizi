class Room:
    
    def __init__(self, id: str, floor: int, seats: int):
        self.id: str = id
        self.floor: int = floor
        self.seats: int = seats
        self.area: float = 2 * self.seats
        
    def get_floor(self) -> int:
        return self.floor
    
    def get_seats(self) -> int:
        return self.seats
    
    def get_id(self) -> str:
        return self.id
    
    def get_area(self) -> float:
        return self.area
        
    def __str__(self) -> str:
        return f'Room(id={self.get_id()}, floor={self.get_floor()}, seats={self.get_seats()})'