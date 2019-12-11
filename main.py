from sanic import Sanic
from sanic import response

import json

def load_postcodes():
    with open('postcodes.json', 'r') as f:
        data = json.loads(f.read())
    f.close()
    return data

postcodes = load_postcodes()

def load_profile_data():
    with open('profile_data.json', 'r') as f:
        data = json.loads(f.read())
    f.close()
    return data

profile_data = load_profile_data()

app = Sanic()

@app.route("/", methods=['GET'])
async def get_html(request):
    with open('site/index.html', 'r') as f:
        html = f.read()
        f.close()
    return response.html(html)

@app.route("/", methods=["POST"])
async def get_deputy(request):
    return response.json(json.loads('{"first_name":"Gregor","last_name":"Gysi","degree":"Dr.","picture_url":"https://www.abgeordnetenwatch.de/sites/abgeordnetenwatch.de/files/dr_gregor_gysi_13.jpg","party":"DIE LINKE"}'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
