import requests

token = "25109659b63e813d5b73926a95e373e3"

'''response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg', json = {
    "trainer_token": token,
    "email": "kalips99@yandex.ru",
    "password": "Gevorglikon6556124"
    }, headers = {"Content-Type" : "application/json"})

print(response.text)'''

'''response_activation = requests.post('https://api.pokemonbattle.me:9104/trainers/confirm_email',
                                  json = {  
   "trainer_token": token                                  
}, headers = {"Content-Type" : "application/json"}) 

print(response_activation.status_code)

if response_activation.status_code == 200:
    print('ok')
else:
    print('not ok')'''


import requests

token = "25109659b63e813d5b73926a95e373e3"


response = requests.post('https://api.pokemonbattle.me:9104/pokemons', json = {
    
    "name": "generate",
    "photo": "generate"

    }, headers = {"Content-Type" : "application/json","trainer_token": token })

print (response.text)


response = requests.put('https://api.pokemonbattle.me:9104/pokemons', json = {
    
    "pokemon_id": "12214",
    "name": "Neo",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"


    }, headers = {"Content-Type" : "application/json","trainer_token": token })

print (response.text)



response = requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', json = {

    "pokemon_id": "12214"



    }, headers = {"Content-Type" : "application/json","trainer_token": token })

print (response.text)



    



