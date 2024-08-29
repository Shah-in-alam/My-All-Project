import pandas as pd
from datetime import datetime
import json
from reportlab.lib.pagesizes import A3
from reportlab.pdfgen import canvas
from bs4 import BeautifulSoup
import requests
import random
import re

"""
Calculates the current month and shows the available vegetables
Parameters
    current_month = Present Month
    df = data frame of a csv file
    veggies = list
    vegs = a whole column
    i = vegetable names
    course = string
"""



current_month = datetime.now().strftime('%B')
df = pd.read_csv("veggies.csv")
veggies = []
vegs = df[df['Month'] == f'{current_month}']
for i in vegs['Vegetables']:
    print(i)
course = input("Course name: ")



def fun_fact():

    """
    Show a random fact about Poland
    Parameters
        titles = list
        facts = list
        sentence = string
        result = string
    Return
        A random fact
    """

    weburl = "https://www.trafalgar.com/real-word/facts-poland/"
    r = requests.get(weburl)
    soup = BeautifulSoup(r.text, features="lxml")

    titles = soup.find_all("h2")
    facts = []

    for i in titles:
        facts.append(i.text)

    fun_facts = facts[:11]

    sentence = random.choice(fun_facts)

    result = re.sub(r'\d+', '', sentence)

    return f"Did You Know?{result}"

fact = fun_fact()










def combined_recipe(course,i):
    """
        Generates a recipe of a given dish name
        Parameters
            data = json data
            i = string
            course = string
        Return
            The recipe of given vegetables and course
        """

    url = "https://chatgpt-api7.p.rapidapi.com/ask"

    payload = {"query": f"Generate a {course} recipe made with {i} starting with the recipe name"}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "88394a3fe4msh0b7307bfb3702e3p1fb268jsn4d3e16051fdd",
        "X-RapidAPI-Host": "chatgpt-api7.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    data = json.loads(response.text)





    return data['response']


content = combined_recipe(course,i)

name = content.split("\n")
real_name = name[0]


def dish_image(dish):
    """
        Gets the url of an image
        Parameters
            data = json data
            photo = string
            dish = string
        Return
            url of image
    """

    url = "https://real-time-image-search.p.rapidapi.com/search"

    querystring = {"query": f"{dish}"}

    headers = {
        "X-RapidAPI-Key": "88394a3fe4msh0b7307bfb3702e3p1fb268jsn4d3e16051fdd",
        "X-RapidAPI-Host": "real-time-image-search.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = json.loads(response.text)

    photo = data['data'][0]['url']
    return photo


photo_url = dish_image(real_name)


def download_image(image_url, file_name):
    """
        Downloads an image
        Return
            None
        else block:
            data = json data
            photo_again = url of an image
        """

    response = requests.get(image_url)
    if response.status_code == 200:
        with open(file_name, 'wb') as file:
            file.write(response.content)
        print("Image downloaded successfully!")
    else:
        url = "https://bing-image-search1.p.rapidapi.com/images/search"

        querystring = {"q": f"bigos"}

        headers = {
            "X-RapidAPI-Key": "88394a3fe4msh0b7307bfb3702e3p1fb268jsn4d3e16051fdd",
            "X-RapidAPI-Host": "bing-image-search1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        data = json.loads(response.text)

        photo_again = data['value'][0]['thumbnailUrl']
        download_image(photo_again, "food.jpg")


download_image(photo_url, "food.jpg")










def create_pdf(title, image_path, text, output_file):
    # Creates a new PDF document
    c = canvas.Canvas(output_file, pagesize=A3)

    # Seting up the title
    c.setFont('Helvetica-Bold', 16)
    c.drawCentredString(400, 1100, title)

    # Addition of the image to the PDF
    c.drawImage(image_path, 100, 500, width=500, height=500)

    # Adding the text to the PDF
    c.setFont('Helvetica', 10)
    text_lines = text.split('\n')
    line_height = 15
    text_y = 450
    for line in text_lines:
        c.drawString(30, text_y, line)
        text_y -= line_height

    # Some more text addition
    c.setFont('Helvetica', 12)
    text2 = f"{fact}"
    text2_y = text_y - line_height  # Calculate the y-coordinate for the additional text
    c.drawString(30, text2_y, text2)

    # Save and close the PDF
    c.save()

    print(f"PDF created successfully: {output_file}")



"""
Parameters
    course = string
    current_month = string
"""

given_title = f"Polish Dish for {course} made with Vegetables available in {current_month}" # A title for the pdf
image_path = "food.jpg" # The image of the food
given_text = content # The whole recipe of the food
output_file = "course specific seasonal recipe.pdf" # The output pdf file name

thecoursedish = create_pdf(given_title, image_path, given_text, output_file)
