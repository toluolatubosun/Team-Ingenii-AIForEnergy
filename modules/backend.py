import pandas as pd

data = pd.read_csv('dataset.csv')

if set(data.all()) == {True} and set(data.all(axis ='columns')) == {True}:
  print("Data is Complete")

make_dict = {}
i = 1
for unique_make in set(data['Make']):
  make_dict[unique_make] = i
  i = i + 1
  
model_dict = {}
i = 1
for unique_model in set(data['Model']):
  model_dict[unique_model] = i
  i = i + 1

vehicle_class_dict = {}
i = 1
for unique_vehicle_class in set(data['Vehicle Class']):
  vehicle_class_dict[unique_vehicle_class] = i
  i = i + 1

transmission_dict = {}
i = 1
for unique_transmission in set(data['Transmission']):
  transmission_dict[unique_transmission] = i
  i = i + 1
  
transmission_type_dict = {}
i = 1
for unique_transmission_type in set(data['Transmission Type']):
  transmission_type_dict[unique_transmission_type] = i
  i = i + 1

fuel_type_dict = {}
i = 1
for unique_fuel_type in set(data['Fuel Type']):
  fuel_type_dict[unique_fuel_type] = i
  i = i + 1

data_clean = data
data_clean['Make'] = data_clean['Make'].map(make_dict, 0)
data_clean['Model'] = data_clean['Model'].map(model_dict, 0)
data_clean['Vehicle Class'] = data_clean['Vehicle Class'].map(vehicle_class_dict, 0)
data_clean['Transmission'] = data_clean['Transmission'].map(transmission_dict, 0)
data_clean['Transmission Type'] = data_clean['Transmission Type'].map(transmission_type_dict, 0)
data_clean['Fuel Type'] = data_clean['Fuel Type'].map(fuel_type_dict, 0)
