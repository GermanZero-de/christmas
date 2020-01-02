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


def get_uuids(validated_input):
    logging.debug("Validated Input: " + validated_input)
    try:
        uuids = postcodes[str(int(validated_input))]["uuids"]
        logging.debug('UUID: ' + str(uuids))
        return uuids
    except Exception as e:
        logging.warning('Could not find postcode: ' + str(e))
        return False


def get_profiles(uuids):
    try:
        profiles = [profile_data[uuid] for uuid in uuids]
        logging.debug('Profile: ' + str(profiles))
        return profiles
    except Exception as e:
        logging.warning('Could not find profile for UUID: ' + str(uuids) + ' Error was: ' + str(e))
        return False
