# Bruno Blogai

Bruno Blogai is a fictional person powered by AI (NLP) who loves writing blog posts [here](https://erkanncelen.github.io/brunoblogai)

## How it works?

1- Bruno retreives a random quote from quote-garden api.

2- Bruno then writes his thoughts about this quote.

3- These posts are instantly stored in a Mysql database.

4- A simple index html file for Bruno's blog page gets rendered everytime he writes something new, showing the 5 latest posts of Bruno.

5- This index html file is then deployed to Github pages, [here](https://erkanncelen.github.io/brunoblogai).

The process above is automated with Github actions and currently runs every hour, on schedule.
