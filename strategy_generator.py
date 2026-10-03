import random
import json
import pandas as pd
from classes import Driver, Tyre
from simulation import run_race_strategy

#driver stats
driver = Driver(pace=95.0, racecraft=92.0, smoothness=90.0)

#race conditions
total_laps=44
base_laptime=90.0
circuit_tyrewear=1.32

compounds = ["SOFT", "MEDIUM", "HARD"]

all_strategies = []
race_id = 0
for tyre1 in compounds:
    for tyre2 in compounds:
        if tyre1==tyre2:
            continue

        for pit_lap in range (1, total_laps):
            schedule = [(tyre1, pit_lap), (tyre2, total_laps)]
            total_time, telemetry = run_race_strategy(
                driver=driver,
                strategy_schedule=schedule,
                total_laps=total_laps,
                base_laptime=base_laptime,
                circuit_tyrewear=circuit_tyrewear, #1 keeps the tyre wear at the base rate of the compound
                list_each_lap=False    #changing to false stops every lap time being listed
            )
            race_id +=1
            #print(f"Race ID: {race_id}")
            strategy_data = {
                "id": f"STRAT_{race_id}",
                "type": "1-Stop",
                "strategy_name": f"{tyre1} -> {tyre2}",
                "pit_lap": [pit_lap],
                "total_time": total_time,
            }

            all_strategies.append(strategy_data)


for tyre1 in compounds:
    for tyre2 in compounds:
        for tyre3 in compounds:
            if tyre1==tyre2:
                continue
            for pit_lap1 in range (1, total_laps):
                for pit_lap2 in range (pit_lap1+1, total_laps):
                    schedule = [(tyre1, pit_lap1), (tyre2, pit_lap2), (tyre3, total_laps)]
                    #print (f"CURRENT STRAT: {tyre1} - {tyre2}   BOXING: Lap {pit_lap}")
                    total_time, telemetry = run_race_strategy(
                        driver=driver,
                        strategy_schedule=schedule,
                        total_laps=total_laps,
                        base_laptime=base_laptime,
                        circuit_tyrewear=circuit_tyrewear, #1 keeps the tyre wear at the base rate of the compound
                        list_each_lap=False    #changing to false stops every lap time being listed
                    )
                    race_id +=1
                    strategy_data = {
                        "id": f"STRAT_{race_id}",
                        "type": "2-Stop",
                        "strategy_name": f"{tyre1} -> {tyre2} -> {tyre3}",
                        "pit_lap": [pit_lap1, pit_lap2],
                        "total_time": total_time,
                    }

                    all_strategies.append(strategy_data)

all_strategies.sort(key=lambda x: x["total_time"]) #sorting the strats by total_time

top_10_strats = all_strategies[:10]

print(f"The top 10 fastest strategy for a {total_laps} lap race with a laptime of {base_laptime}s and circuit tyre wear of {circuit_tyrewear}")
for rank, strat in enumerate(top_10_strats, start=1):  
    print(f"#{rank}     ID: {strat["id"]}       Strategy: {strat["strategy_name"]}          PitLap: {strat["pit_lap"]}\
                Type: {strat["type"]}           Total time: {strat["total_time"]}")



        