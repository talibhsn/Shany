# Horoscope query without horoscope_sign

##  story_001
* greet
 - utter_name 
 
 
## story_002
* goodbye
 - utter_goodbye

## story_003
* thanks
 - utter_thanks
 
## story_004
* name{"person_name":null} 
 - action_greet

## story_005
* greeting
  - utter_greet
* get_horoscope
  - utter_ask_horoscope_sign
* get_horoscope{"horoscope_sign": "Capricorn"}
  - slot{"horoscope_sign": "Aries"}
  - get_todays_horoscope
  - utter_subscribe
* bye

## story_006
* greeting
  - utter_greet
* get_horoscope{"horoscope_sign": "Capricorn"}
  - slot{"horoscope_sign": "Cancer"}
  - get_todays_horoscope
  - utter_subscribe
* subscription
  - slot{"subscribe": "True"}
  - subscribe_user
* bye

# Horoscope query with horoscope_sign

## story_007
* greeting
    - utter_greet
* get_horoscope
    - utter_ask_horoscope_sign
* get_horoscope{"horoscope_sign": "capricorn"}
    - slot{"horoscope_sign": "capricorn"}
    - get_todays_horoscope
    - slot{"horoscope_sign": "capricorn"}
    - utter_subscribe
* subscription{"subscribe": "True"}
    - slot{"subscribe": "True"}
    - subscribe_user
    - slot{"subscribe": true}
* bye

## story_008
* greeting
    - utter_greet
* get_horoscope{"horoscope_sign": "leo"}
    - slot{"horoscope_sign": "leo"}
    - get_todays_horoscope
    - slot{"horoscope_sign": "leo"}
    - utter_subscribe
* subscription{"subscribe": "True"}
    - slot{"subscribe": "True"}
    - subscribe_user
    - slot{"subscribe": true}
* bye

# When user directly asks for subscription

## story_009
* greeting
    - utter_greet
* subscription{"subscribe": "True"}
    - slot{"subscribe": "True"}
    - subscribe_user
    - slot{"subscribe": true}
* bye
