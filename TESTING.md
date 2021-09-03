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


2. The user will be able to find all the answers he/she needs in the homepage of Monstera.
The navar is hosting the main tabs (with dropdowns). Moreover in the second section of the website there is another way to easily access the shop category they prefer. In the footer, instead there will be contacts, FAQs and newsletter application.


### Shop

* As a website owner I want to provide the user with a good range of products and make it easy to distinguish between the categories.
* As a website owner, I want the user to be able to filter the products in order to easily identify what he/she is looking for.

* As a user I want to easily browse through the products to find something I like.

3. The shop tab is really easy and intuitive to use. For example, in the shop all section, under the heading there is a sort dropdown so that the page can match the users desires. The search bar instead, will identify the query and search for it both in the name and in the species. So if the user doesn't know the name we gave to that plant he/she can just search the species.


### Product View

* As a website owner, I want to provide information on the plant and how to care for it so the user can decide if is the right plant for them.
* As a website owner, I want the user to clearly see the price.
* As a website owner, I want to give the possibility to the user to add the plant to their cart.

* As a user, I want to understand if it is the right plant for me by reading something about it.
* As a user, I want to know how much am I going to pay for the plant(s) I picked.
* As a user, I want to be able to add plants to my cart.

4. In the product view page the user will find a picture and a description of the plant, including tips for the care. They can also decide how many to buy (they will see the price grow with the quantity) and put them in the cart.

### Tips

* As a website owner, I want the user to find, beside plants, also information and fun facts about them.
* As a website owner, I want the user to be able to comment on my articles to give his/her opinion or to ask  more information.

* As a user, I want to buy a new plant but I also want to see how the website advise me to behave with it to make it thrive.
* As a user, I want to be able to comment and share my opinion or ask for more tips about my plant(s).

5. The Tips blog is a great way for the users to find out more about plants and to get in contact with fellow plant lovers. There will be advices on how to treat your new plant, how to decide when is the moment to water them and many more. But the fun part will always be get to comment those things with other Monstera's users.


### Login / Registration

* As a website owner, I want users to give to the user a personalized experience by giving the possibility to create an account.

* As a user, if I like the website, I want to have a personal account in it.

6. The user can easily create an account in the accounts tab. If they decide to visit the website again, they will be able to login.

### Profile

* As a website owner, I want to give the possibility to the user to create a profile so they can store their information and review past order.
* As a website owner, I want the users that create an account to access extra features to thank them for their loyalty.

* As a user, I want to create an account with the company so I will not have to insert my information for every order
* As a user, I want to create an account on the website to always have a place where to review past orders.
* As a user, I would like my loyalty to be appreciated by giving me access to extra contents and/or discounts.

7. The Profile page hosts mainly 2 things: a way to store the shipping details and the possibility to review past orders. Only authenticated users can access to this page so this will be a push factor.

### Cart - Checkout

* As a website owner, I want the user to be able to finalize their order. In order to do so I will provide an overview of the cart (with possibility to add and remove articles). 
* As a website owner, once the user is ready for the checkout, I want them to be able to fill in their information and payment method.
* As a website owner, I will provide the user with an overview about what they just bought and the order number for an easy tracking.

* As a user, I want to see clearly what I am about to order and how much will the total be.
* As a user, I want to be able to fill in / retrieve my details and order.
* As a user, I will need an order number to track my package.

8. In the cart view users will be able to review whatthey are about to buy. Also, in the same page they will be asked to fill up their shipping details (for the logged in user it will be already pre-compiled) and credit card details. (If they change idea on what they want, moreover, they will be able to change the quantity or delete some products).

Once all these fields are filled, the user will able to click "pay". If the payment will be successfull they will be redirected to a page with the information of their purchase (which article, the order number and the place it will be delivered at)

# Testing defensive design

Defensive design is been put in place. Many form fields are required or require a specific type of input (letters or numbbers). The user will have to respect these rules in order to finalize his/her purchase.
Also, error hander pages have been put in place to protect the privacy of our (authenticated) users.

# Bugs

1. It was the first time for me creating a model so I had to do quite a bit of reasearch about it. I wanted to create a newsletter and I heard Mailchimp was a good service to use for this. I followed their tutorials but I couldn't make the app work so I decided to cancel it for the moment and retry later. The bug was in the fact that I erased the app but not the migrations and when I tried to recreate it I had an error in the admin. Luckily I discussed this with my mentor and he helped me solve this bug.

2. Another bug I had when I started the project was the allauth templates not working. I was trying to edit the template of the login page but my changes didn't seem to have effect. I had to contact a tutor and she was as confused as me. We chatted for 2 days before realizing that the page was just placed in the wrong folder. Once we solved that and place the file in the right folder, it all worked.

3. A bug that I didn't manage to solve is the fact that each category in the shop has its name on top but the "Shop all" one displays the name of all categories. I tried to implement a loop to give it a different title but unfortunately it didn't work.