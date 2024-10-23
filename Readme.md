# Team Ingenii

This repository contains the project for, the AI For Energy Hackaton 2020, of Team Ingenii

## [Live Demo](https://team-ingenii-aiforenergy.onrender.com/)

## [Official Project Documentation](https://drive.google.com/file/d/1PK_7uUS_KQb-udFKvXjJnC-qv9JaMbyi/view?usp=sharing)

## File Structure
- model.ipynb - Backend Code
- dataset.csv - Data on cars used in the project
- `ingenii` - Django Project (UI)

## Development Setup
- Pull the code to your local machine
```cmd
git init
git branch -M main
git remote add origin https://github.com/toluolatubosun/Team-Ingenii-AIForEnergy.git
git pull origin main
```
- Setup a virtual enviroment
```cmd
pip install virtualenv
virtualenv venv
```
- Install the needed packages
```cmd
pip install -r requirements.txt
```
- Run the django UI
```cmd
cd ingenii
python manage.py runserver
```
- It is advised to run the model.ipynb file on google collaboratory

## Team Members
- Olatubosun John ( Team Leader )
- Oghene Victor
- Djoyi Toluwani
- Solomon Marvellous
- Docemo Adekanmi

## About The Dataset
The data set contains various features of different cars and thier carbon emission

### Keys

Model	
- 4WD/4X4 = Four-wheel drive
- AWD = All-wheel drive
- FFV = Flexible-fuel vehicle
- SWB = Short wheelbase
- LWB = Long wheelbase
- EWB = Extended wheelbase

Transmission	
- A = automatic
- AM = automated manual
- AS = automatic with select shift
- AV = continuously variable
- M = manual
- 3 - 10 = Number of gears

Fuel type	
- X = regular gasoline
- Z = premium gasoline
- D = diesel
- E = ethanol (E85)
- N = natural gas

Fuel consumption	
City and highway fuel consumption ratings are shown in litres per 100 kilometres (L/100 km) - the combined rating (55% city, 45% hwy) is shown in L/100 km and in miles per imperial gallon (mpg)

CO2 emissions	the tailpipe emissions of carbon dioxide (in grams per kilometre) for combined city and highway driving

## Functionality Of The AI

The AI has three main functionalities
- Feature Selection
- Predicting Emission Of Cars
- Suggest Alternative Cars

### Feature Selection
This has to do with determining which features of the car actually contribute towards carbon emission

### Predicting Emission Of Cars
After the important features are selected, different ML algorithms are used to create models that predict the carbon emission of various cars

### Suggest Alternative 
The model created is then used to predict the carbon emission of cars based on the inputed specifications and then suggests similar cars that generates less carbon




