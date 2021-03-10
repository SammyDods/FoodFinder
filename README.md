Food Finder
=================
Deltahacks 2021 Entry
_____________________
## Inspiration
We wanted to gather real time data for foodbanks and organize it in an accesible digital way for folks who need it.

## What it does
Food Finder allows Foodbanks to input how much food is available at certain sites so people can 
easily find food when they need it, all from the accessability of a phone or pc.

## How I built it
I used Python Flask for the backend, HTML and CSS for the frontend, Google API to connect with google sheets and Glitch for editing and 
hosting on the cloud.

## Challenges I ran into
Origonally I was only supposed to some frontend work but my group of four had to go do homework, leaving me in a situation where
I could either leave it as an empty front end husk or learn how to do backend overnight. I didn't have too much faith in the
beginning but I figured things out along the way and got the project to work.

I couldn't figure out how to use the .env file to store secrets in time for the submission period so I thought to myself that no one would look through 
*my* github and look for *my* secrets. Well, I thought wrong, during the judging period I got an email from google stating that my credentials had been 
harvested by a third party for bitcoin mining. Needless to say I learned my lesson and learned how to access the enviromnent variables after the hackathon
concluded.

## Accomplishments that I'm proud of
I'm extrmely proud of the fact that I learned how to do some backend programming as I've had basically zero experience doing that.
Learning flask was pretty awesome and It's cool to know that I have it in my toolbelt now.

## What I learned
I learned how to use Google API with the gspread python module. I then learned how to use Flask to make the page dynamic and then'
Jinja to push that content into the HTML.

## What's next for Food Finder
Currently there's no way to remove food postings except through excel, I would also like to add a button that takes the address and launches google maps.
