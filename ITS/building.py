from ITS.room import Room


class Building:
    
    def __init__(self, name: str, address: str, floors: tuple[int, int]):
        self.name: str = name
        self.address: str = address
        self.floors: int = floors
        self.rooms: list[Room] = []
        
    def get_floors(self) -> tuple[int, int]:
        return self.floors
    
    def get_rooms(self) -> list[Room]:
        return self.rooms
        
    def add_room(self, room: Room):
        floors = self.get_floors()
        if room and isinstance(room, Room) and room not in self.rooms\
            and floors[0] <= room.get_floor() <= floors[1]:
            self.rooms.append(room)
            
    def area(self) -> float:
        sum_area: float = 0
        for room in self.rooms:
            sum_area += room.get_area()
        return sum_area
        
    def __str__(self) -> str:
        s: str = f'{self.name} @ {self.address}\n'
        s += "With Rooms:\n"
        for room in self.get_rooms():
            s += room.__str__() + "\n"
        return s + f'Area = {self.area()}m2'