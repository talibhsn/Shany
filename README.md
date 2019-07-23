# Shany
RASA-powered Horoscope Chatbot

## Installation

*Installing python3.6
RASA NLU works with upto 3.6 version otherwise, it will raise errors and problems. So it’s better you follow this or you might face issues with installation and changing the default versions of python. Setting it up is easy and you can just follow this tutorial. I’ll link up the tutorials I followed if you need more reference.

Navigate in your bash terminal to the location you would like to have your environment:

```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.6
```

To install Rasa, run the following pip command that we’ll be using Rasa version 0.13.2.

$pip install rasa-nlu==0.13.2

Let’s go to our data folder that we created earlier in our terminal and run the following command:

$rasa-nlu-trainer

We run the below snippet to call our train_horoscopebot method. After running this code, we will get an output

$python -m rasa_nlu.train -c config.yml --data data/data.json -o models --fixed_model_name nlu --project current --verbose

Let’s try to run this code file to train our model as per the given parameters.

$python train_initialize.py

After the script is done executing you should see some successful messages.

Now, we need to go to another tab of our terminal or a fresh command line and execute the following command in our project directory (the place where our actions.py file is):

$python -m rasa_core_sdk.endpoint --actions actions

Let’s run the train_online.py in a fresh command line terminal.

$python3 train_online.py

After a successful training of the dialog model, we’ll be getting a message and start your conversation.
