import os
import pandas as pd
from mapper import *
from reducer import *
from shuffle import *
from functools import reduce
def cls():
    os.system("cls" if os.name == "nt" else "clear") # Clear the terminal for cleaner coding

def main():

    cls()

    #Load in the data file
    df = pd.read_csv("data/AComp_Passenger_data_no_error.csv", names=[
                "passenger_id",
                "flight_id",
                "from_airport",
                "to_airport",
                "departure_time",
                "flight_duration",
            ])
    #Preprocessing - remove duplicate rows
    df = df.drop_duplicates()

    ## Task 1

    #Map in is a list of [flight_id, from_airport]
    map_in = df.loc[:,["flight_id", "from_airport"]].values.tolist()
    reduce_out = {}
    #Map each list item into a tuple with '1'
    map_out = map(map_func, map_in)
    #Shuffle the map_out to give a dictionary instead with just the from_airport
    reduce_in = shuffle_flights(map_out)
    #Reduce to the sum of each key in the dictionary
    for key, values in reduce_in.items():
        reduce_out[key] = reduce(reduce_func, values)
    print("Task 1")
    print(reduce_out)

    ## Task 2
    #Map in a list of passenger_id
    map_in = df.loc[:,"passenger_id"].values.tolist()
    reduce_out = {}
    #Map each passenger_id into a tuple with '1'
    map_out = map(map_func, map_in)
    #Shuffle the map out to give a dictionary
    reduce_in = shuffle_passengers(map_out)
    #Reduce to the sum of each key in the dictionary
    for key, values in reduce_in.items():
        reduce_out[key] = reduce(reduce_func, values)
    #Find the maximum
    max_keys = [[k,v] for k, v in reduce_out.items() if v == max(reduce_out.values())]
    print("Task 2")
    print(max_keys)
    
if __name__ == "__main__":
    main()
