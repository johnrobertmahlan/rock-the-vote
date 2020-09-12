# Know Your Vote

Voting is both a right and a privilege. So it is important to be well informed before casting your ballot. The goal of this app is to help you with that. Simply enter your address and:

* Find out who your local representatives are
* See which elected seats are being contested in upcoming elections
* Learn more about polling locations, early voting sites, and ballot dropoff locations

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

The electionId that is used in `views.py` varies from election to election. The electionId for the 2020 general election in the United States is 7000. Unfortunately, data on polling locations is not currently available for this election (as of September 12, 2020), so I have generated some toy data in my `views.py` for the purposes of illustration.

## Future Enhancements
Coming soon!