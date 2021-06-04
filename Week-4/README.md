# Happy Hour - Week 4

#### *Theme:* 
Using APIs

#### *Challenge:* 
~ None ~
## Problems

#### Problem 1

Using a programming language of your choice, print out a random cat fact retrieved from the **_Cat Fact API_**

`https://cat-fact.herokuapp.com/facts`

- OR -

Using a programming language of your choice, print out a random activity from the **_Bored API_**

`http://www.boredapi.com/api/activity/`

#### Problem 2

This one is a surprise! Keep it appropriate, but POST a **message** to the following API:

`https://prod-52.westus.logic.azure.com:443/workflows/de771845ff134d969ae0d83a25c1a43f/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=zGpNhuMy61qzsSaZiKx5cNdErvXkR0Psr1Q1hUqkeHU`

Headers must look as such:
```json
{
    "ApiKey": "Phil Collins",
    "Content-Type": "application/json"
}
```

And the body should look as such:
```json
{
    "message": "<Write a Message>"
}
```


#### Problem 3

Following [this documentation](https://www.openbrewerydb.org/documentation/03-search), take user input to search for a specific brewery, printing out the name and city/state of all the results.

*Challenge:* Format the ouputs into a table format

#### Problem 4

Building off of problem three, after all the breweries print out, let the user pick the brewery they were searching for. Then, using [this api](https://www.openbrewerydb.org/documentation/02-getbrewery) print out more information about that specific brewery.

*Note: I know this call is entirely unnecessary, it was just added for more practice* 

#### Problem 5

In problem 4, the API response should have the lattitude and longitude of a brewery. Using [this api](https://www.7timer.info/bin/astro.php) in the format shown below, print out the weather at your brewery of choice!

`https://www.7timer.info/bin/astro.php?output=json&lon=113.2&lat=23.1`

*Hint: Use the Url `https://www.7timer.info/bin/astro.php?output=json&` and append the lon and lat*

#### Problem 6

Using the API above, create a 5x5 2D-Array of the temperatures in locations a predefined 'step' away in each direction.

Ex. You pick lat=50, lon=50 with a step of 20. 

`array[2][2]` will be the temperature of (50,50), 
`array[2][3]` will be temperature of (50, 70)
`array[0][1]` will be temperature at (10, 30)

*Reminder:* Latitude is in the range (-90, 90) and longitude is in the range (-180, 180)

*Challenge:* Do an 'n'-sized array with the same logic


