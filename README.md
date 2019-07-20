# Shany
RASA-powered Horoscope Chatbot

To install Rasa, run the following pip command that we’ll be using Rasa version 0.13.2.

#pip install rasa-nlu==0.13.2

Let’s go to our data folder that we created earlier in our terminal and run the following command:

#rasa-nlu-trainer

We run the below snippet to call our train_horoscopebot method. After running this code, we will get an output

#python -m rasa_nlu.train -c config.yml --data data/data.json -o models --fixed_model_name nlu --project current --verbose

Let’s try to run this code file to train our model as per the given parameters.

#python train_initialize.py

After the script is done executing you should see some successful messages.

Now, we need to go to another tab of our terminal or a fresh command line and execute the following command in our project directory (the place where our actions.py file is):

#python -m rasa_core_sdk.endpoint --actions actions

Let’s run the train_online.py in a fresh command line terminal.

#python3 train_online.py

After a successful training of the dialog model, we’ll be getting a message and start your conversation.
