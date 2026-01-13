import random


class Plane:
    def __init__(self, plane_type, flight_stats, fuel, course, speed, altitude, location):
        self.plane_type = plane_type

        self.flight_stats = flight_stats
        self.fuel = fuel
        self.course = course
        self.speed = speed
        self.altitude = altitude
        self.location = location
        self.angle = 0
    plane_type_random_list = ['ATR-42', 'ATR-72', 'B737', 'B747', 'A320']
    flight_stats_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                                 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    flight_stats_random_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    planes_stats = {
        'ATR-42': {'speed': (220, 300), 'altitude': (0, 25000), 'fuel': (0, 144)},
        'ATR-72': {'speed': (170, 520), 'altitude': (0, 25000), 'fuel': (0, 158)},
        'B737': {'speed': (100, 541), 'altitude': (0, 41000), 'fuel': (0, 480)},
        'B747': {'speed': (130, 640), 'altitude': (0, 43100), 'fuel': (0, 840)},
        'A320': {'speed': (130, 350), 'altitude': (0, 39100), 'fuel': (0, 480)}
    }
    def fsrnds(Plane):
        fsrfl = random.choice(Plane.flight_stats_letters)
        fsrsl = random.choice(Plane.flight_stats_letters)
        fsrfd = random.choice(Plane.flight_stats_random_digits)
        fsrsd = random.choice(Plane.flight_stats_random_digits)
        fsrtd = random.choice(Plane.flight_stats_random_digits)
        return f'{fsrfl}{fsrsl}{fsrfd}{fsrsd}{fsrtd}'
    def OBJECT_CREATOR(Plane):
        plane_type_chooser = random.choice(Plane.plane_type_random_list)
        stats = Plane.planes_stats[plane_type_chooser]
        flight_number_picker = Plane.fsrnds(Plane)
        fuel_picker = random.randint(stats['fuel'][0], stats['fuel'][1])
        speed_picker = random.randint(stats['speed'][0], stats['speed'][1])
        alt_picker = random.randint(stats['altitude'][0], stats['altitude'][1])

        return Plane(plane_type = plane_type_chooser,flight_stats = flight_number_picker,fuel = fuel_picker,course = None,speed = speed_picker,altitude = alt_picker,location = None)
AAA = Plane.OBJECT_CREATOR(Plane)
print(f"bruhAAA{AAA.plane_type}, bruhAAA{AAA.flight_stats}, bruhAAA{AAA.fuel}, bruhAAA{AAA.course}, bruhAAA{AAA.speed}, bruhAAA{AAA.altitude}, bruhAAA{AAA.location}")



