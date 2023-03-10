# iris-eda-app
Simple Iris EDA app with streamlit

 # Cloning app from github

 - git clone ......


# Create our virtual environnement with pipenv
- install pipenv : pip install pipenv
- install packages : pipenv install streamlit pandas 


# Required Files for deployement
## 1. setup.sh 
setup.sh :  the file where we are going to place all of our credentials as well as our configurations.

There are two options : 

### First option : using our credentials (email)
```
mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"your-email@domain.com\*\n\
" > ~/.streamlit/credentials.toml
```


### Second option : 
```
mkdir -p ~/.streamlit/

echo "\
[server]\n\
headless = true\n\
port = $PORT\n\
enableCORS = false\n\
\n\
" > ~/.streamlit/config.toml
```

## 2. Procfile
Procfile :
    for flaskappp -> web: gunicorn hello:app
    for streamlit -> web: sh setup.sh && streamlit run iris_eda_app.py

Use : sh or bash is the same 

## 3. Requirements.txt
We first need to activate our the virtual environement created with the command (pipenv shell)before freezing our riquirements file
   - pipenv shell
   - pipenv run pip freeze > requirements.txt


# Running the app
Finaly Create the app and run it on a server :
- touch app_name.py
- pipenv run streamlit run app_name.py 


# App Deployement
- git add .
