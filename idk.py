user = input("please Enter your name: ")
print("Hello " + user + " hope your doing well")

 #fav_food = input("whats your fav food: ")
# print(fav_food + '?' + " thats my fav food to!") 
with open("foodlistproject.py", "r") as Food:                                                                               # having trouble as the code printsd all at once 
    food = Food.read()
    food_search = input("Whats your fav food: ")
    if food_search in food:
        print("Thats my fav food too!!")
    else:
        input("Please Enter the correct food name: ")



                                                                                                                                                #### it keeps pinting the loop

#API start 
import requests

ask_user = input("Ok " + user + " Now Please enter the Food name you would like Nutritional information on: ") 



api_url = 'https://api.calorieninjas.com/v1/nutrition?query='.format(ask_user)
query = ask_user
response = requests.get(api_url + query, headers={'X-Api-Key': 'y9/ENrvbCRY867zt8PajAw==smFGPsGiFyL2FUUA'})
if response.status_code == requests.codes.ok:
    print(response.text)
else:
    print("Error:", response.status_code, response.text)


after_user = input("which other food would you like nutritional information on: ")