import configuration
import requests
import data


#Function to create a new user
def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

#Function to create a new user kit
def post_new_user_kit(kit_body, auth_token):
    new_kit_headers = data.headers.copy()
    new_kit_headers["Authorization"] = "Bearer " + auth_token
    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kit_body,
                         headers=new_kit_headers)