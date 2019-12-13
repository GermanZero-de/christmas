import logging
import json

import christmas.data as data

from sanic import Sanic
from sanic import response
from sanic.exceptions import NotFound, ServerError, abort

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
    logging.debug(request.body)
    valid_input = data.validate_input(request.body)
    if valid_input:
        uuid = data.get_uuid(valid_input)
    else:
        uuid = False
    logging.debug("UUID: " + str(uuid))
    if uuid:
        profile = data.get_profile(uuid)
        return response.json(profile)
    else:
        return response.text("No Content", status=204)
