# Typing Test

This project is a locally-hosted typing test based on Python, JavaScript, and HTML. The test is used in the following way:
* The user selects a preferred LENGTH and GENRE and for their typing test
* An excerpt of these criteria is pulled from an array of JSON libraries to create the template
* The user copies the template excerpt with as much speed and accuracy as they can
* A results table tracks user's results (in error count and completion time) for as many tests as they complete in one session

<img src="https://user-images.githubusercontent.com/69176399/185642510-c533d87c-b36b-47ba-81bc-74e303ff271e.png" width=950 align=center>

#### Building a keyboard

The inspiration for this project was a mechanical keyboard that I built for my PC setup this summer. I wanted a keyboard that was satisfying to type on, nice to look at, and that took up less space than my 100% membrane keyboard. I decided on 75% keyboard case with linear switches, and modded it with tape and foam for better acoustics. I also lubed the switches and stabilizers with 205g0 lube for smoother and quieter typing.

![LubeMap](https://user-images.githubusercontent.com/69176399/185642697-6730c05b-75ed-4998-b477-5b932384fd94.png)

During my research into keyboard parts, I found that enthusiasts strongly distinguish between the experience of mechanical and membrane keyboards. The [switch and click keyboard blog](https://switchandclick.com/how-to-type-faster/), asserts that mechanical keyboards can reduce the number of missed key registers and improve typing speed. Even prior to this, I noticed a difference in the way I typed on my membrane keyboard and (laptop) butterfly keys.
I wanted to create a simple, locally-hosted typing test that would allow me to compare the typing speed and number of mistakes made on each type of keyboard.

#### Server-browser interaction

* Typing test is accessed on the browser and connected to the server on a local port
* HTML scripts set up static elements such as drop-down menus, text boxes, tables, and raw text
* Python server code generates templates based on user's preferences, and analyzes the time taken and number of mistakes
* JavaScript handles the server's response and updates HTML for the page to reflect

<img src="https://github.com/brizbird14/Typing-Test/blob/main/servercomm_anim.gif?raw=true" width=600 align=center>

#### What I learned
* Basic communication between frontend browser and backend server
* Creating webpage elements in HTML and managing dynamic elements in JavaScript
* Passing, storing, and accessing information as JSON dictionaries

#### Future improvements
* Calculating mean WPM or characters per minute for each test
* Highlighting errors in red
* Error analysis that accounts for offset of a few letters
* More varied template options (currently only one for each (length, genre) pair)
