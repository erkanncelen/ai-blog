from utils import get_random_quote, generator, insert_record, retreive_posts, render_html

quote = get_random_quote()
context = quote.partition('.')[0] + "."
output = generator(context, max_length=300, do_sample=True, temperature=0.9)
content = output[0]['generated_text'].rsplit('.', 1)[0]+"."
print(context+'\n'+'\n'+content)

insert_record(context, content)
result = retreive_posts()
render_html(result)