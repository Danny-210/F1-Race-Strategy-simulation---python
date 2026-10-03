from classes import Driver, Tyre
from simulation import run_race_strategy

#driver stats
driver = Driver(pace=95.0, racecraft=92.0, smoothness=90.0)

#define pit stop strategy for manual race
strategy = [("HARD", 23), ("SOFT", 36), ("SOFT", 44)] #last stint must end on same lap as the final lap

#manually runs a single race - race conditions can be changed below
total_time, telemetry = run_race_strategy(
    driver=driver,
    strategy_schedule=strategy,
    total_laps=44,
    base_laptime=90.0,
    circuit_tyrewear=1.32, #1 keeps the tyre wear at the base rate of the compound
    list_each_lap=True    #changing to false stops every lap time being listed
)
