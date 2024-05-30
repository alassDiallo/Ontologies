class Device:

    def __init__(self,id,temp=None,hum=None):
        self.id=id
        self.temp=temp
        self.hum=hum
        self.co2 =0
        self.light=0
        self.pm1=0
        self.pm25=0
        self.pm10=0
        self.particule_size=0
        self.comfort=0




    def __str__(self):
        return f"l'appareil {self.id} a pour temperature : {self.temp} et humidité : {self.hum}"