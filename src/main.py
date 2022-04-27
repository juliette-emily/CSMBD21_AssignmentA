import os
import pandas as pd
from mapper import *
from reducer import *
from shuffle import *
from functools import reduce
def cls():
    os.system("cls" if os.name == "nt" else "clear")

def main():

    cls()

    df = pd.read_csv("data/AComp_Passenger_data_no_error.csv", names=[
                "passenger_id",
                "flight_id",
                "from_airport",
                "to_airport",
                "departure_time",
                "flight_duration",
            ])

    df = df.drop_duplicates()

    ## Task 1

    map_in = df.loc[:,["flight_id", "from_airport"]].values.tolist()
    reduce_out = {}
    map_out = map(map_func, map_in)
    reduce_in = shuffle_flights(map_out)
    for key, values in reduce_in.items():
        reduce_out[key] = reduce(reduce_func, values)
    print("Task 1")
    print(reduce_out)

    ## Task 2
    map_in = df.loc[:,"passenger_id"].values.tolist()
    reduce_out = {}
    map_out = map(map_func, map_in)
    reduce_in = shuffle_passengers(map_out)
    for key, values in reduce_in.items():
        reduce_out[key] = reduce(reduce_func, values)
    max_keys = [[k,v] for k, v in reduce_out.items() if v == max(reduce_out.values())]
    print("Task 2")
    print(max_keys)
    
if __name__ == "__main__":
    main()
