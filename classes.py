import random


class Car: #Based on mclaren
    def __init__(self):
        self.aero_rating = 120
        self.power_rating = 100
        self.tyre_wear_rate = 1.0

    def overall_pace(self):
        car_pace=((self.aero_rating+self.power_rating)/2)/100
        return car_pace


class Driver:
    def __init__(self, pace: float = 80.0, racecraft: float = 80.0, smoothness: float = 80.0):
        #Driver scores
        self.pace_score = pace
        self.racecraft_score = racecraft
        self.smoothness = smoothness

    @property
    def pace_delta(self) -> float:
        #converts score into laptime
        return (self.pace_score - 70.0) *0.025

    @property
    def tyre_wear_modifier(self) -> float:
        #higher smoothness score reduces tyre wear rate
        return 1.15 - (self.smoothness_score/200.0)


    #works out the varience in pace based on racecraft score
    def consistency_penalty(self) -> float:

        max_variance_ms = int((100.0-self.racecraft_score)*10)
        penalty_ms = random.randint(0, max(1, max_variance_ms))
        return penalty_ms/1000.0 #converts to ms


class Tyre:

    def __init__(self, compound):
        self.wear=100.0 #tyre wear as a %
        self.compound=compound.upper()

        #tyre compounds
        if self.compound == "SOFT":
            self.wear_rate = 2.0
            self.pace_delta = 0.0

        elif self.compound == "MEDIUM":
            self.wear_rate = 1.5
            self.pace_delta = 0.5

        elif self.compound == "HARD":
            self.wear_rate = 1.0
            self.pace_delta = 1.0
        else:
            print("Error: no tyre compound")

    #tyre degradation over a stint
    def degradation(self, wear_multiplier):
        self.wear = max(0.0, self.wear-(self.wear_rate*wear_multiplier)) #cant drop below 0

    def get_time_loss(self) -> float:
        percentage_used = 100.0-self.wear

        #extra time loss for puncture
        if self.wear <=0:
            return self.pace_delta+25.0

        #quadratic equation for wear so it isnt linear
        wear_penalty = 0.0009*(percentage_used**2)

        return self.pace_delta + wear_penalty

