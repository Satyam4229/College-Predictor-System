# College Predictor System
This the project of the Data Science where we predict the collegese for the student after their marks by the model. The model is based on the report of the various NIT and IIT colleges and their admission procedure.

First, we analyze the data of the different colleges and their stat for admission in various programs, then the model suggest the student top colleges as per their features to get admission in it.

## Process to make the model :-
1. Exploratory Data Analysis
2. Pre - Processing
3. Data Visualization 
4. Training and Testing Dataset
5. Creating Model
6. Optimizing the model
7. check accuracy

## Software and Tools Required

1. [Github Account](https://github.com)
2. [Render Account](https://render.com)
3. [VS Code IDE](https://code.visualstudio.com)
4. [Git CLI](https://https://git-scm.com/book/en/v2/Getting-Started-The-Command-Line)

## Steps to generate whole model and deploment

1. ### Generate model and do the analysis of the model at any platform

2. ### Atlast do the pickling

    ```text
    import pickle

    pickle.dump(model, open('FileName', 'wb')) # To generate the pickle file

    pickle_model = pickle.load(open('FileName, 'rb')) # to load the pickle file
    ```

3. ### create a repository of that model with readme file and gitignore

4. ### Now create a folder in your system, open cmd here and clone that repository there

    ```text
    git clone LINK
    ```

5. ### Now open VS Code from that same location after adding your .pynb and the model.pkl.

6. ### Create a new Environment

    ```text
    conda create -p venv python==3.7 -y
    ```

7. ### Get into the environemnt by typing

    ```text
    git activate venv/
    ```

8. ### Very Important - Create Requirements.txt where we just write all the libraries

    1. Flask
    2. numpy
    3. pandas
    4. sklearn
    5. scikit-learn
    6. matplotlib
    7. gunicorn

    ```text
    pip install -r requirements.txt
    ```

9. ### Configure your UserName and Email ID

    ```text
    git config --global user.name "name"

    git config --global user.email "email"
    ```

10. ### For adding files into git

    ```text
    git add FileName

        or

    git add .   (For whole files)
    ```

11. ### Checking the git status

    ```text
    git status
    ```  

12. ### After this we have to commit that all

    ```text
    git commit -m "Message"
    ```

13. ### After all that we have to push the files into the github

    ```text
    git push origin main
    ```

14. ### After all that we have to create the app.py app which act as a main app behind all that with the help of Flask.

15. ### Then we have to create a html page for frontend and visualization.

16. ### Now after all that we have to go on to render.com and deploy our app with the instructions.
