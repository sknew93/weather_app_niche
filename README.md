# tonightWeather_FLASK
An extremely niche app that will tell you tonight's temperature.

<br>
We have the app.py file that calls the pages into view.
Once called, the page has a text box and a button into which users are expected to type in their cooridantes in the following style "38.2527 N, 85.7585 W".

Hitting the submit button takes that inputted string and passes it to a function, "getAPIData".
Here, we strip the input text to remove any spaces on either side of the text.
Next, the String is formatted using split and strip to extract the directional data and the numeric data, seperately.

The pole data is passed to a function "ifPositiveOrNegative" that returns;
    - "", if a positive direction
    - "-", if a negative direction
The numeric data is combined with their corresponding signs and stored as "final_link"

This is then combined and added to the url, ""https://api.weather.gov/points/{final_link} and a get request is made.
We're looking to extract the link that will give us the forecasted temperature data from the response of the above request.

Once extracted, a get request is made to this link, and the various forcasts are stored under the 'periods' key which inturn is stored under the "properties" key.

We look through the  list of forecasts and pick the one that says "Tonight" (corresponsing to Wednesday night, on the day of the interview.)

One of the three cheeky responses are chosen based on the value of the forecasted temperature and then displayed on the page.

<br>
Author: Swaroop Sk
<br>

