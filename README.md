# Shany
RASA-powered Horoscope Chatbot

## Installation

###Installing python3.6
RASA NLU works with upto 3.6 version otherwise, it will raise errors and problems. So it’s better you follow this or you might face issues with installation and changing the default versions of python. Setting it up is easy and you can just follow this tutorial. I’ll link up the tutorials I followed if you need more reference.

Navigate in your bash terminal to the location you would like to have your environment and Now, let’s install python3.6

```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6
```
### Setting up a virtual environment
Let’s install the required development tools required for the same:
```
sudo apt-get install libpq-dev python-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev
sudo apt-get update
sudo apt-get -y upgrade
```
Let’s install the virtual environment now:
```
sudo apt-get install -y python3.6-venv
```
You should now be in the Documents folder (or where ever you would like to have your environment)in your terminal and type the following commands:
```
mkdir environments
cd environments
```
Let’s set up a virtual environment called “my_env” (you could also call it something fancier)
```
python3.6 -m venv my_env
```
To make sure it’s set up, you could check with
```
ls my_env
```
and the output would have the following files and folders:
bin    include    lib    lib64    pyvenv.cfg    share

Now, to activate the virtual environment, type the following in the command line:
```
source my_env/bin/activate
```
And the output you should see is along the lines of
(my_env) fancyname@yourname:~/environments$

### Installing Rasa NLU:
Please type in the following commands to install the requirements for Rasa NLU. Then run the following pip command to install Rasa that we’ll be using Rasa version 0.13.2 
```
sudo apt-get install python3.6-dev
pip install twisted
pip install rasa-nlu==0.13.2
```
We shall now install two of the most popular pipelines (I’ll explain all of these fancy words to you in the next blog post). Install the spacy pipeline. It will take a little time, don’t worry!
```
pip install rasa_nlu[spacy]
python -m spacy download en_core_web_md
python -m spacy link en_core_web_md en
```
Install the TensorFlow pipeline 
```
pip install rasa_nlu[tensorflow]
```

### Execution of RASA-NLU

Let’s go to our data folder that we created earlier in our terminal and run the following command:
```
rasa-nlu-trainer
```
We run the below snippet to call our train_horoscopebot method. After running this code, we will get an output
```
python -m rasa_nlu.train -c config.yml --data data/data.json -o models --fixed_model_name nlu --project current --verbose
```
Let’s try to run this code file to train our model as per the given parameters.
```
python train_initialize.py
```
After the script is done executing you should see some successful messages.

Now, we need to go to another tab of our terminal or a fresh command line and execute the following command in our project directory (the place where our actions.py file is):
```
python -m rasa_core_sdk.endpoint --actions actions
```
Let’s run the train_online.py in a fresh command line terminal.
```
python3 train_online.py
```
After a successful training of the dialog model, we’ll be getting a message and start your conversation.
