import logging
import json

from os import environ
from sanic import Sanic
from sanic import response
from sanic.exceptions import NotFound, ServerError, abort

from christmas import server

LOG_LEVEL = logging.getLevelName(environ.get('LOG_LEVEL', 'WARNING'))

app = Sanic()

@app.exception(NotFound)
async def ignore_404s(request, exception):
    logging.info("This URL could not be found: {}".format(request.url))
    return response.text("Not Found", status=404)

@app.exception(ServerError)
async def catch_500s(request, exception):
    logging.error("This created an error: {}".format(str(request)))
    return text("There was an error", status=500)

@app.route("/", methods=['GET'])
async def get_html(request):
    with open('site/index.html', 'r') as f:
        html = f.read()
        f.close()
    return response.html(html)

@app.route("/", methods=["POST"])
async def request_deputy(request):
    if server.validate_input(request.json):
        uuid = server.get_uuid(str(request.json))
    if uuid:
        profile = server.get_profile(uuid)
        return response.json(profile)
    else:
        return response.text(
                "This postcode could not be found: {}".format(str(request.json)),
                status=204)

if __name__ == "__main__":
    logger = logging.getLogger()
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s christmas.%(module)s.%(funcName)s +%(lineno)s: '
                                  '%(levelname)-8s [%(process)d] %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(LOG_LEVEL)
    app.run(host="0.0.0.0", port=8000, access_log=False)
