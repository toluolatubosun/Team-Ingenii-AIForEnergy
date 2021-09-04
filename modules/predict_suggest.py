from modules.backend import make_dict, model_dict, vehicle_class_dict, transmission_dict, transmission_type_dict, fuel_type_dict, data_clean
import pickle

def predict_suggest(data_dict):
    make = data_dict.get('make')
    make = make_dict.get(make, 0)

    model = data_dict.get('model')
    model = model_dict.get(model, 0)

    vehicle_class = data_dict.get('vehicle_class')
    vehicle_class = vehicle_class_dict.get(vehicle_class, 0)

    engine_size = data_dict.get('engine_size')

    cylinders = data_dict.get('cylinders')

    transmission = data_dict.get('transmission')
    transmission = transmission_dict.get(transmission, 0)

    transmission_type = data_dict.get('transmission_type')
    transmission_type = transmission_type_dict.get(transmission, 0)

    fuel_type = data_dict.get('fuel_type')
    fuel_type = fuel_type_dict.get(fuel_type, 0)

    FC_city = data_dict.get('fc_city') 

    FC_hwy = data_dict.get('fc_hwy') 

    FC_comb_L100 = data_dict.get('fc_comb_l100')

    FC_comb_mpg = data_dict.get('fc_comb_mpg')

    # Predict the emission
    ml_model = pickle.load(open('linear_regression_model.pickle', 'rb'))
    X = [[engine_size, cylinders, FC_city, FC_hwy, FC_comb_L100, FC_comb_mpg]]
    emission = ml_model.predict(X)
    print(f'Predicted CO2 Emission(g/km) {int(emission[0])} \n')

    # loops through the dataset to find a different car that emmits less carbon
    make_list = []
    model_list = []
    suggest = False

    for car in data_clean.values.tolist():
        if car[0] != make and car[1] != model:
            if car[2] == vehicle_class and car[7] == fuel_type and car[5] == transmission:
                if car[12] < emission :
                    suggest = True
                    for c, m in make_dict.items():
                        if m == car[0]:
                            print(f'Make - {c}')
                            make_list.append(c)
                    for c, m in model_dict.items():
                        if m == car[1]:
                            print(f'Model - {c} \n')
                            model_list.append(c)

    if suggest == False:
        print('No alternative car found, You made the right choice : )')

    return int(emission), zip(make_list, model_list)