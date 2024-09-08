from room import Room
class Hotel:
    def __init__(self,name:str):
        self.name = name
        self.rooms = []
        self.guests = 0
    @classmethod
    def from_stars(cls,stars_count:int):
        return cls(f'{stars_count} stars Hotel')
    
    def add_room(self,room: Room):
        self.rooms.append(room)

    def take_room(self,room_number:int,people:int):
        for room in self.rooms:
            if room.number == room_number:
                result = room.take_room(people)
                if result is None:
                    self.guests += people
        return f'Room number {room_number} does not exist'
        
    def free_room(self, room_number: int) -> str:
        for room in self.rooms:
            if room.number == room_number:
                result = room.free_room()
                if result is None: 
                    self.guests -= room.guests
                return result
        return f"Room number {room_number} does not exist"
    
    def print_status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        print(f"Hotel {self.name} has {self.guests} total guests")
        print(f"Free rooms: {', '.join(free_rooms) if free_rooms else 'None'}")
        print(f"Taken rooms: {', '.join(taken_rooms) if taken_rooms else 'None'}")

    

