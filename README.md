# Python-Arduino-Weather-Station

This project is a work in progress. I am currently waiting for parts to arrive in the mail.

I made this project to gain more experience with in situ, real time data and Python. The project consist of an Arduino, stationed outside within Wi-Fi range, taking a wind speed sample over an interval of time and updating the database. I used the Django web framework to set up a model for the Weather Data, for the Controller to update the View. Currently the View is plain containing just the latest wind speed. 

After the Arduino is set to report accurate wind speed data and can successfully update the database, I plan to make asthetic modifications to the View however a farmer may find it most useful. Then I may add more weather sensors to the Arduino, and make the according modifications to the database and framework.

This project could be useful to farmers interested in saving time and travel. Real time, in situ data like wind speed can let farmers know if it is a good time or day to spray chemical, or if it is just too windy. Another relevant addition I may add is a rainfall sensor. Sometimes it rains overnight, during harvest, and the farmer has to drive out the next morning to check and see if their field recieved enough rainfall to delay the harvest. Having real time, in situ precip data can let the farmer decide whether to harvest that day, wait until the afternoon so the field can dry, or let the hired hands know it's a shop day. They could do this from their home computer or mobile phone at any time.

The disadvantage to this project is that it is restricted to Wi-Fi range. If the project proves worth while, I would consider researching to transmit data by SMS messaging then figure out how to handle that data into the database.

Below is the status of the Arduino and the Python framework, as well as shell instructions.

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
  
  Shell instructions
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
    
