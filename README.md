# Typing Test

This project is a locally-hosted typing test based on Python, JavaScript, and HTML. The test is used in the following way:
* The user selects a preferred LENGTH and GENRE and for their typing test
* An excerpt of those qualities is pulled from an array of JSON libraries to create the test
* The user copies the template excerpt with as much speed and accuracy as they can
* A results table tracks user's results (in error count and completion time) for as many tests as they complete in one session

![SpeedtestPic](https://user-images.githubusercontent.com/69176399/182047583-e2d1ee4e-63bb-49f1-b40c-ceeb8e3f63e1.png)

#### Building a keyboard

The inspiration for this project was a mechanical keyboard that I decided to build for my PC setup this summer. I wanted a keyboard that was satisfying to type on, nice to look at, and that took up less space than my 100% membrane keyboard. I decided on 75% keyboard case, as well as linear switches which tend to have a more consistent and quiet typing experience than their clicky and tactile counterparts. I also lubed the switches and stabilizers with 205g0 lube for smoother and quieter typing.

![LubeMap](https://user-images.githubusercontent.com/69176399/182047587-47d13eeb-5214-4273-939f-6026ec1fc742.png)

During my research into keyboard parts, I found that enthusiasts strongly distinguish between the quality and experience of mechanical and membrane keyboards especially. The [switch and click keyboard blog](https://switchandclick.com/how-to-type-faster/), asserts that mechanical keyboards reduce the number of missed key registers and that, when customized, mechanical keyboards can improve typing speed. Before building my mechanical keyboard, I also noticed a difference in the way I typed on my membrane keyboard and the butterfly keyboard on my Mac laptop.
I wanted to create a simple, locally-hosted typing test that would allow me to compare the typing speed and number of mistakes made on each type of keyboard.

#### Server-browser interaction

The server starts a websocket server and HTTP server on a (hardcoded) local port, which is then accessed on the browser. Once the connection is established, the server communicates the HTML and JavaScript scripts to the browser, setting up the static and dynamic elements of the page, respectively. 
Each time the user interacts with the buttons on the browser page, a message with the information submitted by that button is sent to the server as a JSON message. The server then processes the information and returns a JSON message so that the browser can update accordingly.
For my typing test, browser elements coded in HTML include the drop-down menus, text boxes, tables, and raw text. The Python server code processes the text selection using criteria from the drop-down menus, as well as analyzing the time taken and mistakes made for each test submission. JavaScript handles the server’s response, updating the HTML code accordingly by accessing the elements to be changed by their tags.

#### What I learned
* Basic communication between frontend browser and backend server
* Creating webpage elements in HTML and managing dynamic elements in JavaScript
* Passing, storing, and accessing information as JSON dictionaries

#### Future improvements
* Calculating mean WPM or characters per minute for each test
* Highlighting errors in red
* Error analysis that accounts for offset of a few letters
* More varied template options (currently only one for each length, genre pair)
