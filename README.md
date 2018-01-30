# Python-Arduino-Weather-Station

This project is a work in progress. I am currently waiting for parts to arrive in the mail. Below is the status of the Arduino and the Python side as well as command line instructions.

I made this project to gain more experience with real time data and Python. The project consist of an Arduino, stationed outside within Wifi range, taking a wind speed sample over an interval and updating the database. I used the Django web framework to set up a model for the Weather Data, for the Controller to update the View. Currently the View is plain containing just the latest wind speed. 

After the Arduino is set to report accurate wind speed data and can successfully update the database, I plan to make asthetic modifications to the View, then add more weather sensors to the Arduino, and make the according modifications to the database and framework.

Arduino
==================
Summary:
  - Currently produces random integers in 2 minute intervals to represent wind speed data
  
Libraries:
  - TimerOne for the Interupt Service Routine
  - MyPrintf for a C-like print option that uses Flash memory
  
Parts coming in mail:
  - Wifi shield
  - Differential pressure sensor to read wind speed
  
 Python side
 =================
 Summary:
  - Python version 2.7
  - Django version 1.7
  - Sqlite3 database
  - Project built based on djangoproject.com documentation
  - There is a Weather Data app with a Wind model that has 3 attributes: speed, direction, station ID
  - The view currently shows the Wind speed for the model with the station ID equal to "scholz_farm"
  
  Command line instructions
  ===========================
  You will need to set up your own virtual environment
  
  run server:
  - env_weatherStation\scripts\activate
  - cd ./weatherStation
  - python manage.py runserver
    
  view page:
  - http://127.0.0.1:8000/
    
  change models:
  - python manage.py makemigrations
  - python manage.py migrate
    
  run shell and modify main model:
  - python manage.py shell
  - from weatherData.models import Wind
  - w = Wind(stationID="scholz_farm")
  - w.save()
  - w.id
  - w.speed
  - w.stationID  
    
