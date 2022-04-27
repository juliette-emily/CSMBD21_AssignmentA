def shuffle_flights(mapper_out):
    data = {}
    flight_ids = []
    #For each [flight_id, from_airport] key in mapper_out, if we haven't counted the fight yet, then add it into the dictionary
    for k, v in mapper_out:
        if k[0] not in flight_ids:
            flight_ids.append(k[0])
            if k[1] not in data:
                data[k[1]] = [v]
            else:
                data[k[1]].append(v)    
    return data

def shuffle_passengers(mapper_out):
    data = {}
    #For each passenger_id key in mapper_out, if we haven't counted the passenger flight yet, then set the value, otherwise append to the values
    for k, v in mapper_out:
        if k not in data:
            data[k] = [v]
        else:
            data[k].append(v)  
    return data