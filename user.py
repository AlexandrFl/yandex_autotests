# import requests
import data
import requests 
import json


# def create_new_user (firstName, email, phone, comment, address):
#     new_user =  {"firstname":firstName,  
#                 "email":email,
#                 "phone":phone,
#                 "comment":comment, 
#                 "address":address}
#     return new_user

body = {
    "firstName": "Григорий",
    "email": "fff@mail.ru",
    "phone": "+74441237887",
    "comment": "Ребёнок спит, не шумите",
    "address": "г. Москва, ул. Хохотушкина, д. 16"
    }   

def getToken(body) :
    responce = requests.post(data.URL + data.Create_User,
                             json=body,
                             headers=data.headers)
    authToken = responce.json()
    return authToken["authToken"]

