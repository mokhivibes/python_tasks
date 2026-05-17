def get_car_info(manufacturer, model, **other_infos):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in other_infos.items():
        car[key] = value
    return car
