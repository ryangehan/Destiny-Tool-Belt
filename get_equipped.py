import requests

id = "4611686018447695967"  # " + id + "
# id = "4611686018441392470"  #dj
idtype = "1"  # " + idtype + "
headers = {"X-API-Key": "b9d611e224fd4da3bf2b87e1b9942f15"}
defURL = 'https://www.bungie.net'


def get_characters():
    chardict = {}
    url = defURL + "/Platform/Destiny2/" + idtype + "/Profile/" + id + "?components=200"
    response = requests.request("GET", url, headers=headers).json()
    for character in response['Response']['characters']['data']:
        destiny_class = str(response['Response']['characters']['data'][character]['classType'])
        if destiny_class == '2':
            chardict['warlock'] = character
        elif destiny_class == '1':
            chardict['hunter'] = character
        elif destiny_class == '0':
            chardict['titan'] = character
        else:
            print('you have less than three classes bozo')
    return chardict


def get_item_name(itemID):
    url = defURL + "/Platform/Destiny2/Manifest/DestinyInventoryItemDefinition/" + str(itemID) + "/"
    response = requests.request("GET", url, headers=headers).json()
    return response['Response']['displayProperties']['name']


def get_equipped(charID):
    equipped = {'weapons': {}, 'armor': {}}
    url = defURL + "/Platform/Destiny2/" + idtype + "/Profile/" + id + "/Character/" + charID + "/?components=205"
    response = requests.request("GET", url, headers=headers).json()
    items = response['Response']['equipment']['data']['items']
    equipped['weapons']['kinetic'] = get_item_name(items[0]['itemHash'])
    equipped['weapons']['special'] = get_item_name(items[1]['itemHash'])
    equipped['weapons']['heavy'] = get_item_name(items[2]['itemHash'])
    equipped['armor']['head'] = get_item_name(items[3]['itemHash'])
    equipped['armor']['arms'] = get_item_name(items[4]['itemHash'])
    equipped['armor']['chest'] = get_item_name(items[5]['itemHash'])
    equipped['armor']['legs'] = get_item_name(items[6]['itemHash'])
    equipped['armor']['class'] = get_item_name(items[7]['itemHash'])
    return equipped


characters = get_characters()
equipped_items = get_equipped(characters['warlock'])
print(equipped_items)