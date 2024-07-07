class MainData:
    def __init__(self, temp: float, feels_like: float, temp_min: float, temp_max: float, pressure: int, humidity: int, sea_level: int, grnd_level: int):
        self.temp = temp
        self.feels_like = feels_like
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.pressure = pressure
        self.humidity = humidity
        self.sea_level = sea_level
        self.grnd_level = grnd_level
