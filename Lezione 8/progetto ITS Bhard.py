""
class Room:

    def __init__(self, id: str, floor: int, seats: int) -> None:
        self.id: str = id
        self.floor: int = floor
        self.seats: int = seats

    def get_id(self):
        return self.id
    
    def get_floor(self):
        return self.floor

    def get_seats(self):
        return self.seats
            



class Building:

    def __init__(self, name: str, address: str,num_floors: int, rooms: list = []) -> None:
        
        self.name: str = name
        self.address: str = address
        self.rooms: list = rooms
        self.num_floors: int = num_floors

    def add_room(self, room: Room):
        if room and isinstance(room, Room) and room not in self.rooms and room.get_floor <= self.num_floors:

            self.rooms.append(room)
            

    def __str__(self) -> str:
        return f"{self.name.capitalize()} @ {self.address}"
    

b: Building = Building("SMI","Via Sierra Nevada 60", 4,[])
armellini: Building = Building("ITIS", "Basilica San Paolo", 3, [])





    



        