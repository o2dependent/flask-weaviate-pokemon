import weaviate

client = weaviate.Client(url="http://localhost:8080")  # Replace the URL with that of your Weaviate instance

def weaviate_img_search(img_str):
	search_object = {'image' : img_str, 'distance': 0.1}
	results = client.query.get('PokemonCards', ['image']).with_additional('distance').with_near_image(search_object, encode=False).with_limit(2).do()

	return  results['data']['Get']['PokemonCards']
