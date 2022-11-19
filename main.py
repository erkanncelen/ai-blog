from transformers import pipeline
import requests

## function that gets the random quote
def get_random_quote():
	try:
		## making the get request
		response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
		if response.status_code == 200:
			## extracting the core data
			json_data = response.json()
			data = json_data['data']

			## getting the quote from the data
			return data[0]['quoteText']
		else:
			print("Error while getting quote")
	except:
		print("Something went wrong! Try Again!")


quote = get_random_quote()

generator = pipeline('text-generation', model ='EleutherAI/gpt-neo-125M')

context = quote.partition('.')[0]
output = generator(context, max_length=300, do_sample=True, temperature=0.9)
content = output[0]['generated_text'].rsplit('.', 1)[0]+"."
print(context+'\n'+'\n'+content)