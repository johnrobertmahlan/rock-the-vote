# Know Your Vote

Voting is both a right and a privilege. So it is important to be well informed before casting your ballot. The goal of this app is to help you with that. Simply enter your address and:

* Find out who your local representatives are
* See which elected seats are being contested in upcoming elections
* Learn more about polling locations, early voting sites, and ballot dropoff locations

## History of the App
Know Your Vote was initially built as my Hack Week project when I was a student in General Assembly's Software Engineering Immersive Remote Flex Program. Since graduating, I have been tinkering with the app, focusing primarily on improving the front end design and implementing basic error handling and custom form validation.

## Get Started with the App
Know Your Vote is deployed to Heroku [here](https://do-you-know-your-vote.herokuapp.com/).

## Technologies
Know Your Vote was built with the following languages and technologies:

* HTML, CSS, Python
* Django
* Django Requests [Library](https://requests.readthedocs.io/en/master/)
* Google Civic Information [API](https://developers.google.com/civic-information)
* [Materialize](https://materializecss.com/)
* Google [Fonts](https://fonts.google.com/)

## Essential Information about the App
Because Know Your Vote relies on Google's Civic Information API, some data is not always available. A support forum with information about the availability of data for upcoming elections can be found [here](https://developers.google.com/civic-information/docs/ci_forum).

The electionId that is used in `views.py` varies from election to election. The electionId for the 2020 general election in the United States is 7000. Because this election is now over, election data is no longer available. Data concerning elected representatives remains available, however.

## Future Enhancements
In addition to continuing to improve the front end of this app and as well as its custom form validations, I would like for this app to eventually include a number of more advanced features. These include:

1. Continue to improve the front end.
2. Consuming the GoogleMaps API to provide users with *directions* to polling locations.
3. Consuming additional APIs to provide more information about candidates as well as ballot measures or referenda.
4. The ability to determine whether one is a registered voter. (This is very much an icebox feature, but future work on the app may include this.)