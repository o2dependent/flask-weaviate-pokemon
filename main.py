from flask import Flask, render_template, request, jsonify
import weaviate
from search_image import weaviate_img_search

# auth_config = weaviate.auth.AuthApiKey(api_key="bGIkcpYcw0K5Uki8tHVD6di4MGOU0jTIQBCU")  # Replace w/ your API Key for the Weaviate instance

# client = weaviate.Client(url="https://pokemon-test-l6ze2gae.weaviate.network", auth_client_secret=auth_config)  # Replace the URL with that of your Weaviate instance
client = weaviate.Client(url="http://localhost:8080")  # Replace the URL with that of your Weaviate instance

app = Flask(__name__)

@app.route("/")
def hello_world():
	data = client.query.get('PokemonCards', ['image']).do()
	images = data['data']['Get']['PokemonCards']
	for i in range(len(images)):
		image = images[i]
		images[i] = f"data:image/jpeg;base64,{image['image']}"
	# return f"<p>{images}</p>"
	return render_template('index.html', value=images)

@app.route('/search')
def search_page():
	return render_template('search.html')

@app.route('/search/image', methods=['POST'])
def search_image():
	if 'image' in request.json:
		image = request.json['image']
		results = weaviate_img_search(image)
		return jsonify({
			"images": results
		})
	else:
		return jsonify({'error': 'No image provided'})