import random
import json
import pandas as pd
from classes import Driver, Tyre




#runs the full race strategy simulation
def run_race_strategy(driver:Driver, strategy_schedule:list, total_laps: int, base_laptime:float, circuit_tyrewear:float, list_each_lap):
    total_race_time = 0.0
    pit_stop_loss = 22.0
    race_telemetry = []

    stint_index = 0
    current_compound, stint_end_lap = strategy_schedule[stint_index]
    current_tyre = Tyre(current_compound)

    if list_each_lap:
        print ("RACE START")

    for current_lap in range(1, total_laps +1):
        fuel_advantage = (current_lap-1)*0.03
        current_tyre.degradation(circuit_tyrewear)

        tyre_loss = current_tyre.get_time_loss()

        driver_consistency = driver.consistency_penalty()

        lap_time = base_laptime - driver.pace_delta + tyre_loss - fuel_advantage + driver_consistency
        total_race_time += lap_time

        #store lap data
        lap_data = {
            "lap":current_lap,
            "compound":current_tyre.compound,
            "wear_remaining":current_tyre.wear,
            "lap_time":round(lap_time, 3),
            "fuel_advantage":round(fuel_advantage, 3),
            "tyre_loss":round(tyre_loss, 3),
            "is_pit_lap":False
        }

        #pitstop
        if current_lap == stint_end_lap and current_lap <total_laps:
            total_race_time += pit_stop_loss
            lap_data["is_pit_lap"] = True
            lap_time = base_laptime - driver.pace_delta + tyre_loss - fuel_advantage + driver_consistency + pit_stop_loss

            if list_each_lap:
                print(f"BOXING LAP {current_lap}    Time lost in pits +{pit_stop_loss}")

            stint_index +=1
            next_compound, stint_end_lap = strategy_schedule[stint_index]
            current_tyre = Tyre(next_compound)  #Tyre change

        mins = int(lap_time//60)
        secs = lap_time%60
        if list_each_lap:
            print (f"Lap {current_lap:02d}  Time: {mins}:{secs:06.3f}     Compound: {current_tyre.compound}\
                      Tyre Wear: {current_tyre.wear}    Fuel Gain: -{fuel_advantage}")

        race_telemetry.append(lap_data)

    total_mins = int(total_race_time//60)
    total_secs = total_race_time%60
    if list_each_lap:
        print(f"Race Finished       Total Time: {total_mins}m {total_secs:.3f}s     Time in Seconds: {total_race_time}")

    return total_race_time, race_telemetry

