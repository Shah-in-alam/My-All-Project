import json
from reportlab.lib.pagesizes import A3
from reportlab.pdfgen import canvas
from bs4 import BeautifulSoup
import requests
import random
import re



"""

Obtaining course name form the respected user
parameters
    course = input string
    my_file = json file
    my_data = json daya
    dish_list = list
    dish = string

"""

course = input("Course name: ")
my_file = open("dish_data.json")
my_data = json.load(my_file)
dish_list = []

for i in my_data[course]:
    dish_list.append(i)

random_item = random.choice(dish_list)
dish = random_item





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












def course_recipe(dish):
    """
        Generates a recipe of a given dish name
        Parameters
            data = json data
            dish = string
        Return
            The recipe of given dish
    """

    url = "https://chatgpt-api7.p.rapidapi.com/ask"

    payload = {"query": f"What is the recipe of {dish}?"}
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "88394a3fe4msh0b7307bfb3702e3p1fb268jsn4d3e16051fdd",
        "X-RapidAPI-Host": "chatgpt-api7.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)

    data = json.loads(response.text)

    return f"Dish Name: {dish}" + "\n" + data['response']


content = course_recipe(dish)



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


photo_url = dish_image(dish)


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
            "X-RapidAPI-Host": "real-time-image-search.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        data = json.loads(response.text)

        photo_again = data['value'][0]['thumbnailUrl']
        download_image(photo_again, "food.jpg")


download_image(photo_url, "food.jpg")














def create_pdf(title, image_path, text, output_file):
    # Creates a new PDF document
    c = canvas.Canvas(output_file, pagesize=A3)

    # Setting up the title
    c.setFont('Helvetica-Bold', 16)
    c.drawCentredString(400, 1100, title)

    # Adding the image to the PDF
    c.drawImage(image_path, 100, 500, width=500, height=500)

    # Adding the text to the PDF
    c.setFont('Helvetica', 10)
    text_lines = text.split('\n')
    line_height = 15
    text_y = 450
    for line in text_lines:
        c.drawString(30, text_y, line)
        text_y -= line_height

    # Addition of some text
    c.setFont('Helvetica', 12)
    text2 = f"{fact}"
    text2_y = text_y - line_height  # Calculating the y-coordinate for the additional text
    c.drawString(30, text2_y, text2)


    # Save and close the PDF
    c.save()

    print(f"PDF created successfully: {output_file}")



given_title = f"Polish Dish for {course}" # A title for the pdf
image_path = "food.jpg" # The image of the food
given_text = content # The whole recipe of the food
output_file = "course recipe.pdf" # The output pdf file name

thecoursedish = create_pdf(given_title, image_path, given_text, output_file)

