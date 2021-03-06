import re
import logging
import json


def load_postcodes():
    with open('data/postcodes.json', 'r') as f:
        data = json.loads(f.read())
    f.close()
    return data


postcodes = load_postcodes()


def load_profile_data():
    with open('data/profile_data.json', 'r') as f:
        data = json.loads(f.read())
    f.close()
    return data


profile_data = load_profile_data()


def validate_input(request):
    regex = re.compile(r'^postcode=\d{5}$')
    try:
        logging.debug('Type: ' + str(type(request)))
        string = request.decode()
        if bool(regex.match(string)):
            logging.debug('Cut my strings: ' + string[-5:])
            return string[-5:]
        else:
            raise ValueError
    except Exception as e:
        logging.warning('User Input could not be validated: ' + str(e))
        return False


def get_uuid(validated_input):
    logging.debug("Validated Input: " + validated_input)
    try:
        uuid = postcodes[str(int(validated_input))]["uuid"]
        logging.debug('UUID: ' + uuid)
        return uuid
    except Exception as e:
        logging.warning('Could not find postcode: ' + str(e))
        return False


def get_profile(uuid):
    try:
        profile = profile_data[uuid]
        logging.debug('Profile: ' + json.dumps(profile))
        return profile
    except Exception as e:
        logging.warning('Could not find profile for UUID: ' + str(uuid) + ' Error was: ' + str(e))
        return False
