## Welcome to the Polish Cook Book

The demo.ipynb is the main file to be opened and run.

The package creates a pdf file with desired recipe selected based on the prompt.

The scripts are created with a mixture of APIs, Webpage scraping and additional data files.

***
It is requested that if the demo.ipynb doesn't function at the first attempt then please try attempting again, because it is made of different APIs and Webpages. APIs get updates more or less and sometimes some APIs are found offline or doesn't function after some days or doesn't function sometimes and does function sometimes. Webpages also get updates or are changed which results in change of html of the page. 
***

The package contains the following:


4 APIs
-themealDB (To spawn random polish dish names)
-OpenAi Api-7 (To generate any recipe based on a very simple prompt or command)
-real-time-image-search (To search for dish or food image)
-bing_image_search (To search for dish or food image)


2 Website Scraped
-www.trafalgar.com (To obtain interesting facts about Poland and it's cuisine)
-www.edition.cnn (To obtain Polish dish with their actual usable names)


2 Data File - 1 csv & 1 json 
-veggies.csv (The file contains the available vegetables according to months in Belgium)
-dish_data.json (The file contains several dish names which are categorized according to the course)



### Inside the WhatToCook directory:

"random_recipe.py" script generates a random recipe and creates a pdf with the photo and directions everytime it is run.
This script is not hardcoded to any dish which is why it not known which dish will be generated when. It is completely random and 
a random choice from 15+ dishes is obtained.


"course_recipe.py" script allows the user to enter a course name such as: breakfast, lunch, dinner or snack. Then the script will create a pdf which will contain the recipe of a polish dish based on the selected course.


"seasonal_recipe.py" script detects the present time and uses the file veggies.csv to find which vegetables are available in the month. Then it creates a recipe made from those vegetables.


"seasonal_course_recipe.py" script allows the user to enter a course name such as: breakfast, lunch, dinner or snack and then detects the month with available vegetables. Then the script will create a pdf which will contain the recipe of a polish dish based on the selected course made with the available vegetables in Belgium of that month.


## Conclusion

Thank you for considering our Python package! We hope it proves to be a valuable tool for your projects. If you have any questions, encounter any issues, or have suggestions for improvements, please don't hesitate to reach out. We appreciate your interest and feedback.

Happy coding!







