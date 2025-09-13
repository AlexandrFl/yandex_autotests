import requests 
import data
import user

kit_1 = {
       "name": "a",
       "card": {
           "id": 1,
           "name": "Под ситуацию"
       },
       "productsList": "",
       "id": 7,
       "productsCount": 0
   }

kit_2 = {
       "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC",
       "card": {
           "id": 1,
           "name": "Под ситуацию"
       },
       "productsList": "",
       "id": 7,
       "productsCount": 0
   }

kit_3 = {
       "name": "",
       "card": {
           "id": 1,
           "name": "Под ситуацию"
       },
       "productsList": "",
       "id": 7,
       "productsCount": 0
   }

kit_4 = {
       "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD",
       "card": {
           "id": 1,
           "name": "Под ситуацию"
       },
       "productsList": "",
       "id": 7,
       "productsCount": 0
   }

kit_5 = {
       "name": "QWErty",
       "card": {
           "id": 1,
           "name": "Под ситуацию"
       },
       "productsList": "",
       "id": 7,
       "productsCount": 0
   }

kit_6 = {
       "name": "Мария",
       "card": {
           "id": 1,
           "name": "Под ситуацию"
       },
       "productsList": "",
       "id": 7,
       "productsCount": 0
   }

kit_7 = {
       "name": "№%@,",
       "card": {
           "id": 1,
           "name": "Под ситуацию"
       },
       "productsList": "",
       "id": 7,
       "productsCount": 0
   }

kit_8 = {
       "name": " Человек и КО ",
       "card": {
           "id": 1,
           "name": "Под ситуацию"
       },
       "productsList": "",
       "id": 7,
       "productsCount": 0
   }

kit_9 = {
       "name": "123",
       "card": {
           "id": 1,
           "name": "Под ситуацию"
       },
       "productsList": "",
       "id": 7,
       "productsCount": 0
   }

kit_10 = {}

kit_11 = {
       "name": 123,
       "card": {
           "id": 1,
           "name": "Под ситуацию"
       },
       "productsList": "",
       "id": 7,
       "productsCount": 0
   }

def createKits(kit):
    token = user.getToken(user.body)
    new_header = {
    "Content-Type": "application/json",
    "Authorization" : "Bearer" + " "  + token
    }
    responce = requests.post(data.URL + data.Create_kits,
                             json=kit,
                             headers=new_header)
    return responce