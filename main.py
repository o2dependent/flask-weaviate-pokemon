from flask import Flask
import requests
import weaviate

# auth_config = weaviate.auth.AuthApiKey(api_key="bGIkcpYcw0K5Uki8tHVD6di4MGOU0jTIQBCU")  # Replace w/ your API Key for the Weaviate instance

# client = weaviate.Client(url="https://pokemon-test-l6ze2gae.weaviate.network", auth_client_secret=auth_config)  # Replace the URL with that of your Weaviate instance
client = weaviate.Client(url="http://localhost:8080")  # Replace the URL with that of your Weaviate instance

app = Flask(__name__)

@app.route("/")
def hello_world():
	data = client.query.get('PokemonCards', ['image']).do()
	all_images = data['data']['Get']['PokemonCards']
	images_html = ''
	for image in all_images:
		images_html += f"<img src='data:image/jpeg;base64,{image['image']}' />"
	return f"<p>{images_html}</p>"
