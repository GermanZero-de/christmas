import json
import logging

from os import environ

import christmas.data as data

LOG_LEVEL = logging.getLevelName(environ.get('LOG_LEVEL', 'ERROR'))


def test_all_valid_zipcodes():
    with open('data/zipcodes.de.json', 'r') as f:
        zipcodes = json.loads(f.read())
        f.close()
    missing_zipcodes = []
    for zip in zipcodes:
        if not data.get_profile(data.get_uuid(str(int(zip["zipcode"])))):
            missing_zipcodes.append(zip)
    zipcode_errors = {"error_count": len(missing_zipcodes),
                      "missing_zipcodes": missing_zipcodes}
    print(json.dumps(zipcode_errors))


if __name__ == "__main__":
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s christmas.%(module)s.%(funcName)s +%(lineno)s: '
                                  '%(levelname)-8s [%(process)d] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(LOG_LEVEL)
    test_all_valid_zipcodes()
