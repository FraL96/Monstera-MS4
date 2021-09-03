<h1 align="center">4. Testing</h1>

This file is the forth chapter of the full README file. Click here to go to [README.md](./README.md)

# Table of contents

1. [Code Validators](#Code-Validators)
2. [Responsiveness/Browsers Compatibility](#Responsiveness/Browsers-Compatibility)
3. [Testing User Stories](#Testing-User-Stories)
4. [Testing Defensive Design](#Testing-Defensive-Design)
5. [Bugs](#Bugs)

------

# Code Validators

### [W3C HTML Validator]():

In all the files, the validator interprets the django syntax as error. Apart that, no errors are found in the actual "plain code".

<img src="readme/images/w3c-valid.png" alt="Validator HTML" width="500px">

### [W3C CSS Validator](https://jigsaw.w3.org/css-validator/):

In the CSS file, only one error was found. However in this situation I used "clip" to solge a bug where the scrollbar use to go under the navbar. For this reason I decide to keep it.

<img src="readme/images/css-validation.png" alt="CSS validation" width="500px">

## [PEP8](http://pep8online.com/)

The PEP8 validator revealed some errors. However they where all about whitespaces (missing or too many).
I considered that wasn't a critical error so I decided to keep it for now. 

<img src="readme/images/pep8.png" alt="PEP8" width="500px">

### [JS Hint](https://jshint.com/)

JS Hint revealed no errors in the js files.

------

#  Responsiveness / Browser compatibility

The website display perfectly on the 5 browsers I tried it on.
Also all the pages display great on the devices we tried it on.
(For the browsers have been used real ones, while for the devices the results are taken from a devices emulator.)

<img>

# Testing User Stories

### Website

* As a website owner, I want to create a website where users will be able to shop for plants and order their favourites. 
* As a website owner, I want people to be able find fun facts and tips about how to take care of their plant.
* As a website owner, I want to make a profit from the sell of plants on my website.

* As a user, I want to be able to shop and order plants on the website. 
* As a user, I want to find information on how to take care of my plants.


1. On Monstera users will be able to buy plants and also learn how to take care of them, both from the website owner and from other users. Being an e-commerce website, moreover, it will create a profit foe the website owner.


### Homepage

* As a website owner, I want the user to be able to understand the purpose of the website and be able to access the different tabs. 
* As a website owner, I want the user to find means to contact us in case of any question or problem.
* As a website owner, I want the homepage to be attractive for the user.
* As a website owner, I want the user to find a response to all questions about ordering plants on Monstera.

* As a user I want to be able to easily navigate the website.
* As a user, I want to find everything I am looking for in just a few clicks.


2.


### Shop

* As a website owner I want to provide the user with a good range of products and make it easy to distinguish between the categories.
* As a website owner, I want the user to be able to filter the products in order to easily identify what he/she is looking for.

* As a user I want to easily browse through the products to find something I like.


### Product View

* As a website owner, I want to provide information on the plant and how to care for it so the user can decide if is the right plant for them.
* As a website owner, I want the user to clearly see the price.
* As a website owner, I want to give the possibility to the user to add the plant to their cart.

* As a user, I want to understand if it is the right plant for me by reading something about it.
* As a user, I want to know how much am I going to pay for the plant(s) I picked.
* As a user, I want to be able to add plants to my cart.

### Tips

* As a website owner, I want the user to find, beside plants, also information and fun facts about them.
* As a website owner, I want the user to be able to comment on my articles to give his/her opinion or to ask  more information.

* As a user, I want to buy a new plant but I also want to see how the website advise me to behave with it to make it thrive.
* As a user, I want to be able to comment and share my opinion or ask for more tips about my plant(s).


### Login / Registration

* As a website owner, I want users to give to the user a personalized experience by giving the possibility to create an account.

* As a user, if I like the website, I want to have a personal account in it.

### Profile

* As a website owner, I want to give the possibility to the user to create a profile so they can store their information and review past order.
* As a website owner, I want the users that create an account to access extra features to thank them for their loyalty.

* As a user, I want to create an account with the company so I will not have to insert my information for every order
* As a user, I want to create an account on the website to always have a place where to review past orders.
* As a user, I would like my loyalty to be appreciated by giving me access to extra contents and/or discounts.

### Cart - Checkout

* As a website owner, I want the user to be able to finalize their order. In order to do so I will provide an overview of the cart (with possibility to add and remove articles). 
* As a website owner, once the user is ready for the checkout, I want them to be able to fill in their information and payment method.
* As a website owner, I will provide the user with an overview about what they just bought and the order number for an easy tracking.

* As a user, I want to see clearly what I am about to order and how much will the total be.
* As a user, I want to be able to fill in / retrieve my details and order.
* As a user, I will need an order number to track my package.


