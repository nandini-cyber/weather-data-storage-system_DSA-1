
class WeatherRecord:
    def __init__(self, date, city, temp):
        self.date = date
        self.city = city
        self.temp = temp

    def __repr__(self):
        return f"({self.date}, {self.city}, {self.temp})"



class WeatherStorage:
    def __init__(self, years, cities):
        self.years = years
        self.cities = cities
        self.data = [[[] for _ in cities] for _ in years]

    def insert(self, record):
        y = self.years.index(int(record.date.split('/')[-1]))
        c = self.cities.index(record.city)
        self.data[y][c].append(record)

    def delete(self, date, city):
        year = int(date.split('/')[-1])
        if year in self.years and city in self.cities:
            y = self.years.index(year)
            c = self.cities.index(city)
            for r in self.data[y][c]:
                if r.date == date:
                    self.data[y][c].remove(r)
                    return True
        return False

    def retrieve(self, city, year):
        if year in self.years and city in self.cities:
            y = self.years.index(year)
            c = self.cities.index(city)
            return self.data[y][c]
        return []

    def row_major(self):
        for i, year in enumerate(self.years):
            for j, city in enumerate(self.cities):
                print(year, city, self.data[i][j])

    def col_major(self):
        for j, city in enumerate(self.cities):
            for i, year in enumerate(self.years):
                print(year, city, self.data[i][j])



def main():
    years = [2024, 2025]
    cities = ["Delhi", "Mumbai"]
    ws = WeatherStorage(years, cities)

    # insert some records
    ws.insert(WeatherRecord("01/01/2025", "Delhi", 25))
    ws.insert(WeatherRecord("02/01/2025", "Delhi", 26))
    ws.insert(WeatherRecord("01/01/2024", "Mumbai", 30))

    print("Retrieve:", ws.retrieve("Delhi", 2025))
    ws.delete("02/01/2025", "Delhi")
    print("After delete:", ws.retrieve("Delhi", 2025))

    print("\nRow-major:")
    ws.row_major()
    print("\nColumn-major:")
    ws.col_major()
