# **Auction App**

## Task Description

Your task is to develop an "auction web application" using the Django and Vue (think of Ebay). The web app should provide the following functionalities:

Users can create an account on the web app and login / logout. You should use a custom User model (as explained here) which inherits from Django's AbstractUser model, and make use of Django's authentication framework. The signup and login can be done using Django forms and templates. Vue only needs to be used once the user is authenticated.

Your custom user model should then also have a profile image, email, and date of birth of the user. The user should be able to edit all these fields in a "profile page". Changes to the profile page should be saved via Ajax (using Vue and the fetch API).

There should be a page where users can post a new item for auction. Items should contain a title, a description, starting price, a picture and the date/time the auction finishes.

Users of the site should then be able to bid for an item, before the end date/time of that item.

The site must contain a page listing all the items that are currently available, with the ability to “search” for items based on a given keyword. For instance, searching for “table” should return the list of items that have “table” as part of their title or description. The searching mechanism should be done using Ajax (so no page refreshes).

Users are able to send questions to the item owner about the condition of the item, and the owner is able to reply to those questions. These questions and answers should be visible to all users of the site.

At the end of the auction, the winner receives an email confirming that they should proceed to purchase the item. This feature should be implemented using cron jobs and Django's send_mail function. You should create a temporary Gmail account for your group and use that to send emails.

The top 10% of the mark (4 marks) will be given to projects that are making full use of static type checking. That means your Python code should be fully annotated with types, and the Vue frontend should use typescript.

**Outcome:** Once fully tested, your application should be deployed to the EECS OpenShift platform (to be discussed in week 8) — one deployed app per team. Make sure your submitted application has at least 5 test users and at least 10 items on auction. Each group should submit the code including a README file which should contain:

## Marking criteria

Criteria	+  Max. mark
- Using Django's AbstractUser model and authentication framework	2

- Using Vue router for frontend routing	2

- Using Ajax where required with Vue and fetch API	6

- Correct modelling of application data, including users, items, bids, questions and answers	3

- Account creation and login working	3

- Profile page included, with (editable) profile picture, email, city and date of birth	3

- Page with a list of items currently available included and working as expected	3

- Users are able to send questions about items to the seller	3

- README and requirements.txt files included with the requested information	2

- App deployed to Openshift with auto email sending	4

- Full use of static types both in Python and Vue	4

Total:	35
