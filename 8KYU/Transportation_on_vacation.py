def rental_car_cost(d):
    if d>1 and d<7:
        return (d*40)-20
    elif d>=7:
        return (d*40)-50
    return d*40