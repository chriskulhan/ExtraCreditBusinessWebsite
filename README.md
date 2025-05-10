# FamilyArchiveWebsite
This is a test website so I can see if what my group has planned for our capstone website will work.

Crew: It's essential you install the correct dependencies and are in the correct place when running them.

#0 check to see if the app runs: python app.py
if it doesn't, install everything in the flask_business_site folder (venv will appear)
to get there type: cd flask_business_site

#1: create a virtual environment:
python -m venv venv

#2: activate the environment:
source venv/bin/activate


#3 install flask:
pip install flask
#also need to install the upgrade:
pip install --upgrade pip

#4 install flask Alchemy so database things are easier:
pip install flask-sqlalchemy

#5 install flask_wtf and wtforms to use with uploading photos
pip install flask_wtf wtforms

#6: You should be in the flask_business_site directory in terminal. if not, you'll need to reinstall venv
cd flask_business_site

#7: now you can run the app.py that should show the site:
python app.py

#8 to stop running press ctrl-c

#9 having trouble getting the csv to export with the database portion. This might be a problem. 

Experimenting with features for the capstone group project:

How to upload files with flask using python:
https://www.youtube.com/watch?v=GeiUTkSAJPs

how to do flask authentication (flask login):
https://www.youtube.com/watch?v=71EU8gnZqZQ

python upload and view photo tutorial:
https://www.youtube.com/watch?v=dP-2NVUgh50

css photo gallery option:
https://www.w3schools.com/css/css_image_gallery.asp

#To run all the requirements.txt file: pip install -r requirements.txt