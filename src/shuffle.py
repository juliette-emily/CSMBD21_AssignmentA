def shuffle_flights(mapper_out):
    data = {}
    flight_ids = []
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
    for k, v in mapper_out:
        if k not in data:
            data[k] = [v]
        else:
            data[k].append(v)  
    return data