from project.band import Band
from project.band_members.drummer import Drummer
from project.band_members.guitarist import Guitarist
from project.band_members.singer import Singer
from project.concert import Concert


class ConcertTrackerApp:
    VALID_MUSICIANS = {'Guitarist': Guitarist, 'Drummer': Drummer, 'Singer': Singer}

    def __init__(self):
        self.bands = []
        self.concerts = []
        self.musicians = []

    def create_musician(self, musician_type: str, name: str, age: int):
        if musician_type not in self.VALID_MUSICIANS:
            raise ValueError("Invalid musician type!")
        musician_obj = self._find_musician_by_name(name, self.musicians)
        if musician_obj:
            raise Exception(f"{name} is already a musician!")
        self.musicians.append(self.VALID_MUSICIANS[musician_type](name, age))
        return f"{name} is now a {musician_type}."

    def create_band(self, name: str):
        band_obj = self._find_band_by_name(name, self.bands)
        if band_obj:
            raise Exception(f"{name} band is already created!")
        self.bands.append(Band(name))
        return f"{name} was created."

    def create_concert(self, genre: str, audience: int, ticket_price: float, expenses: float, place: str):
        concert_obj = self._find_concert_by_place(place, self.concerts)
        if concert_obj:
            raise Exception(f"{place} is already registered for {genre} concert!")
        self.concerts.append(Concert(genre, audience, ticket_price, expenses, place))
        return f"{genre} concert in {place} was added."

    def add_musician_to_band(self, musician_name: str, band_name: str):

        musician_obj = self._find_musician_by_name(musician_name, self.musicians)
        band_obj = self._find_band_by_name(band_name, self.bands)
        if musician_obj is None:
            raise Exception(f"{musician_name} isn't a musician!")
        if band_obj is None:
            raise Exception(f"{band_name} isn't a band!")
        band_obj.members.append(musician_obj)
        return f"{musician_name} was added to band {band_name}."

    def remove_musician_from_band(self, musician_name: str, band_name: str):
        band_obj = self._find_band_by_name(band_name, self.bands)
        if band_obj is None:
            raise Exception(f"{band_name} isn't a band!")
        musician_obj = self._find_musician_by_name(musician_name, self.musicians)
        if musician_obj not in band_obj.members:
            raise Exception(f"{musician_name} isn't a member of {band_name}!")
        band_obj.members.remove(musician_obj)
        return f"{musician_name} was removed from {band_name}."

    def start_concert(self, concert_place: str, band_name: str):
        band = self._find_band_by_name(band_name, self.bands)

        for musician_type in ['Drummer', 'Guitarist', 'Singer']:
            if not any(filter(lambda x: x.__class__.__name__ == musician_type, band.members)):
                raise Exception(f"{band_name} can't start the concert because it doesn't have enough members!")
        concert = self._find_concert_by_place(concert_place, self.concerts)

        if concert.genre == 'Rock':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' and 'play the drums with drumsticks' not in band_member.skills:
                    raise Exception(f"{band_name} is not ready to play at the concert!")
                if band_member.__class__.__name__ == "Guitarist" and 'play rock' not in band_member.skiils:
                    raise Exception(f"{band_name} is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and 'singer high pitch notes' not in band_member.skills:
                    raise Exception(f"{band_name} is not ready to play at the concert!")
        elif concert.genre == "Metal":
            for band_member in band.members:
                if band_member.__class_.__name__ == 'Drummer' and 'play the drums with drumsticks' not in band_member.skills:
                    raise Exception(f"{band_name} is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and 'sing low pitch notes' not in band_member.skills:
                    raise Exception(f"{band_name} is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and 'play metal' not in band.skills:
                    raise Exception(f"{band_name} is not ready to play at the concert!")
        elif concert.genre == 'Jazz':
            for band_member in band.members:
                if band_member.__class__.__name__ == 'Drummer' and 'play the drums with drum brushes' not in band_member.skills:
                    raise Exception(f"{band_name} is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Singer' and \
                    ('sing high pitch notes ' or 'sing low pitch notes') not in band_member.skills:
                    raise Exception(f"{band_name} is not ready to play at the concert!")
                if band_member.__class__.__name__ == 'Guitarist' and 'play zazz' not in band_member.skills:
                    raise Exception(f"{band_name} is not ready to play at the concert!")
        profit = concert.audience * concert.ticket_price - concert.expenses
        return f"{band_name} gained {profit:.2f}$ from the {concert.genre} concert in {concert.place}."




    def _find_concert_by_place(self, place, collection):

        concert = [c for c in collection if c.place == place]
        if not concert:
            return None
        return concert[0]

    def _find_band_by_name(self, name, collections):
        band = [b for b in collections if b.name == name]
        if not band:
            return None
        return band[0]

    def _find_musician_by_name(self, name, collection):

        musician = [m for m in collection if m.name == name]
        if not musician:
            return None
        return musician[0]
