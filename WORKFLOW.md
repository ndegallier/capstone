# capstone

This file is meant to track and log the progress and development of my capstone
project in sequential order.

7/10/17 -- Created project folder, uploaded to github, created README and
WORKLOW text files.

7/11/17 -- Got miniconda working, successfully rendered dataframe of data into 
html

7/12/17 -- Successfully made intrinio API calls on a time loop

Next step is to create db and have intrinio data be posted to the database
Goal for today: call historical price data for apple, commit it, and display
it in a graph in html -- note not live feed graph yet

7/14/17 -- Intrinio data added to database.

Muting api.py, api_post.py, and decorators.py files and moving them to API folder
Making database modular using models.py file
Add timestamp to intrinio equity data

7/15/17 --- Successfully commited data to capstone db

When commiting equity data it is comitted twice, most likely an issue with config
and moduling



