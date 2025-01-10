### How to setup and run

1. Unzip folder
2. cd into folder
3. python -m venv venv
4. .\venv\Scripts\activate (./venv/bin/activate on MacOS)
5. pip install -r requirements.txt
6. python setupDB.py (setup database table Persons)
7. flask --app app run (run application)

### How to test

1. python -m unittest .\tests\test_app.py (to run the unit testing program)
