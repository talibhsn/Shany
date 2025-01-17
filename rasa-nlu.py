{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "from rasa_nlu.training_data import load_data\n",
    "from rasa_nlu.model import Trainer\n",
    "from rasa_nlu.config import RasaNLUModelConfig\n",
    "from rasa_nlu import config\n",
    "\n",
    "from rasa_nlu.model import Interpreter\n",
    "\n",
    "def train_horoscopebot(data_json, config_file, model_dir):\n",
    "    training_data = load_data(data_json)\n",
    "    trainer = Trainer(config.load(config_file))\n",
    "    trainer.train(training_data)\n",
    "    model_directory = trainer.persist(model_dir, fixed_model_name = 'horoscopebot')\n",
    "\n",
    "\n",
    "def predict_intent(text):\n",
    "    interpreter = Interpreter.load('./models/current/nlu/default/horoscopebot')\n",
    "    print(interpreter.parse(text))\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "/usr/local/lib/python3.6/site-packages/h5py/__init__.py:36: FutureWarning: Conversion of the second argument of issubdtype from `float` to `np.floating` is deprecated. In future, it will be treated as `np.float64 == np.dtype(float).type`.\n",
      "  from ._conv import register_converters as _register_converters\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fitting 2 folds for each of 6 candidates, totalling 12 fits\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "[Parallel(n_jobs=1)]: Done  12 out of  12 | elapsed:    0.1s finished\n"
     ]
    }
   ],
   "source": [
    "train_horoscopebot('./data/data.json', 'config.json', './models/current/nlu')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'intent': {'name': 'get_horoscope', 'confidence': 0.8291659825386053}, 'entities': [{'start': 84, 'end': 89, 'value': 'virgo', 'entity': 'horoscope_sign', 'confidence': 0.977643660424268, 'extractor': 'ner_crf'}], 'intent_ranking': [{'name': 'get_horoscope', 'confidence': 0.8291659825386053}, {'name': 'subscription', 'confidence': 0.07109274867752459}, {'name': 'greeting', 'confidence': 0.06421747064611169}, {'name': 'dob_intent', 'confidence': 0.03552379813775843}], 'text': 'I am looking for my horoscope for today. I am wondering if you can tell me that for Virgo'}\n"
     ]
    }
   ],
   "source": [
    "predict_intent(\"I am looking for my horoscope for today. I am wondering if you can tell me that for Virgo\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'intent': {'name': 'get_horoscope', 'confidence': 0.4203288842437285}, 'entities': [{'start': 7, 'end': 9, 'value': '15', 'entity': 'DD', 'confidence': 0.5842037705839949, 'extractor': 'ner_crf'}, {'start': 10, 'end': 12, 'value': '08', 'entity': 'MM', 'confidence': 0.8802007828058543, 'extractor': 'ner_crf'}], 'intent_ranking': [{'name': 'get_horoscope', 'confidence': 0.4203288842437285}, {'name': 'dob_intent', 'confidence': 0.3503565734158552}, {'name': 'greeting', 'confidence': 0.1471164496944807}, {'name': 'subscription', 'confidence': 0.08219809264593572}], 'text': 'dob is 15-08'}\n",
      "{'intent': {'name': 'get_horoscope', 'confidence': 0.8456705103362621}, 'entities': [{'start': 0, 'end': 9, 'value': 'capricorn', 'entity': 'horoscope_sign', 'confidence': 0.8700039373678508, 'extractor': 'ner_crf'}], 'intent_ranking': [{'name': 'get_horoscope', 'confidence': 0.8456705103362621}, {'name': 'greeting', 'confidence': 0.08371362196161819}, {'name': 'subscription', 'confidence': 0.05447483700155865}, {'name': 'dob_intent', 'confidence': 0.016141030700561228}], 'text': 'Capricorn'}\n"
     ]
    }
   ],
   "source": [
    "predict_intent(\"dob is 15-08\")\n",
    "predict_intent(\"Capricorn\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "{'intent': {'name': 'subscription', 'confidence': 0.8615342349131018}, 'entities': [{'start': 0, 'end': 11, 'value': 'False', 'entity': 'subscribe', 'confidence': 0.8837177393732473, 'extractor': 'ner_crf', 'processors': ['ner_synonyms']}], 'intent_ranking': [{'name': 'subscription', 'confidence': 0.8615342349131018}, {'name': 'get_horoscope', 'confidence': 0.060856452547792886}, {'name': 'greeting', 'confidence': 0.04139289658697123}, {'name': 'dob_intent', 'confidence': 0.03621641595213371}], 'text': 'unsubscribe me'}\n",
      "{'intent': {'name': 'greeting', 'confidence': 0.8472929307505297}, 'entities': [], 'intent_ranking': [{'name': 'greeting', 'confidence': 0.8472929307505297}, {'name': 'get_horoscope', 'confidence': 0.08152686272640515}, {'name': 'subscription', 'confidence': 0.050874120583883686}, {'name': 'dob_intent', 'confidence': 0.02030608593918152}], 'text': 'Hi'}\n"
     ]
    }
   ],
   "source": [
    "predict_intent(\"unsubscribe me\")\n",
    "predict_intent(\"Hi\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {},
   "outputs": [],
   "source": [
    "# import rasa_core\n",
    "# !python -m rasa_core.run --core ./models/current/nlu --endpoints endpoints.yml"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "base_url = \"http://horoscope-api.herokuapp.com/horoscope/{day}/{sign}\"\n",
    "url = base_url.format(**{'day': \"today\", 'sign': 'capricorn'})\n",
    "#http://horoscope-api.herokuapp.com/horoscope/today/capricorn\n",
    "res = requests.get(url)\n",
    "todays_horoscope = res.json()['horoscope']\n",
    "response = \"Your today's horoscope:\\n{}\".format(todays_horoscope)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"Your today's horoscope:\\nDespite repeated failures, very few realise that the key to success is in having the patience of a saint. Vexation invariably leads to an outburst which, in turn, can ruin your reputation and future prospects in innumerable ways. Today, Ganesha advises you to keep your calm and smile back even if faced with an adverse situation. Doing as directed may help you overcome troubles and take the right decisions.\""
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 0,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
