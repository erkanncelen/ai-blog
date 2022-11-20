from transformers import pipeline
import requests
from dotenv import load_dotenv
import mysql.connector
import os

## function that gets the random quote
def get_random_quote():
	try:
		response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
		if response.status_code == 200:
			json_data = response.json()
			data = json_data['data']

			return data[0]['quoteText']
		else:
			print("API Error while getting quote")
	except:
		print("Something went wrong while getting the quote.")

## defining ai text generator
generator = pipeline('text-generation', model ='EleutherAI/gpt-neo-125M')

## instert new post to DB
def insert_record(context, content):
    try:
        load_dotenv()

        mydb = mysql.connector.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database = os.getenv('DB_NAME')
        )

        mycursor = mydb.cursor()

        sql = "INSERT INTO posts (context, content) VALUES (%s, %s)"
        val = (context, content)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted to DB.")
    except:
        print("Something went wrong while inserting record to DB.")

## retrieve latest 5 records from DB
def retreive_posts():
    try:
        load_dotenv()

        mydb = mysql.connector.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database = os.getenv('DB_NAME')
        )

        mycursor = mydb.cursor()

        sql = "SELECT * FROM posts ORDER BY created_at DESC LIMIT 5"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        return result

    except:
        print("Something went wrong while retreiving records from DB.")

## rendering single line HTML string for github pages index.html
def render_html(result):
    try:
        context1= result[0][1]
        context2= result[1][1]
        context3= result[2][1]
        context4= result[3][1]
        context5= result[4][1]

        content1= result[0][2]
        content2= result[1][2]
        content3= result[2][2]
        content4= result[3][2]
        content5= result[4][2]

        date1= str(result[0][3].date()) + " " + str(result[0][3].time())
        date2= str(result[1][3].date()) + " " + str(result[1][3].time())
        date3= str(result[2][3].date()) + " " + str(result[2][3].time())
        date4= str(result[3][3].date()) + " " + str(result[3][3].time())
        date5= str(result[4][3].date()) + " " + str(result[4][3].time())

        htmltext = f'<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd"><html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en"><head><title>Bruno Florentin</title><meta http-equiv="content-type" content="text/html; charset=iso-8859-1" /><link rel="stylesheet" href="css/1.css" type="text/css" media="screen,projection" /></head><body><div id="container">  <div id="header">    <h1><a>Bruno <strong>Florentin</strong></a></h1>    <h2>Some of my thoughts</h2>  </div>  <div id="sidebar">    <h1>About Me</h1>    <p>Hi there! I am Bruno Florentin. I love philosophy and a good cup of coffee.      I share some of my intriguing thoughts in this blog. Hope you enjoy reading them!</p>  </div>  <div id="content">    <h1><a id="intro">{context1}</a></h1>    <p>{content1}</p>    <div class="article_menu"> <b>{date1}</b> </div>        <h1><a id="css">{context2}</a></h1>    <p>{content2}</p>    <div class="article_menu"> <b>{date2}</b> </div>    <h1><a id="css">{context3}</a></h1>    <p>{content3}</p>    <div class="article_menu"> <b>{date3}</b> </div>    <h1><a id="css">{context4}</a></h1>    <p>{content4}</p>    <div class="article_menu"> <b>{date4}</b> </div>    <h1><a id="css">{context5}</a></h1>    <p>{content5}</p>    <div class="article_menu"> <b>{date5}</b> </div>  </div>  <div id="footer">    <p> This is the personal blog of Bruno Florentin. </p>  </div></div></html>'

        f = open("docs/index.html", "w")
        f.write(htmltext)
        f.close()
    except:
        print("Something went wrong while rendering HTML.")
