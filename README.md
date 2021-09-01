<h1 align="center">MONSTERA</h1>
<h2 align="center">the future is green</h2>

![intro](./add picture devices)

Monstera is a project born from a passion. In the last year I discovered my big love for plants of every kind.
At the moment I share my house with over 50 plants, some bought and some grown from seeds (took from a shop or directly from the vegetables and fruit in my fridge). And almost every month the family grows a bit bigger.
I decided to create Monstera as an e-commerce shop, where users can bring home some of the most beautiful plants that exist, but also as a blog where to share with the visitors thought and tips about this beautiful green world.

Click [here](https://monstera-ms4.herokuapp.com/) to discover Monstera.

---

# Table of contents

1. [User Experience](#User-Experience)
    - [Project Goals](#Project-Goals)
    - [User Stories](#User-Stories)
        - [Website](#Website)
        - [Homepage](#Homepage)
        - [Shop](#Shop)
        - [Product View](#Product-View)
        - [Tips](#Tips)
        - [Login / Registration](#Login-/-Registration)
        - [Profile](#Profile)
        - [Cart - Checkout](#Cart-Checkout)
    - [Design](#Design)
        - [Color Use](#Color-Use)
        - [Fonts](#Fonts)
        - [Icons](#Icons)
        - [Images](#Images)
        - [Defensive Design](#Defensive-Design)
        - [Navigation](#Navigation)
        - [Data Modelling](#Data-Modelling)
        - [Use of Database](#Use-of-Database)
        - [Wireframes](#Wireframes)
2. [Features](#Features)
    - [Existing Features](#Existing-Features)
    - [Future Features](#Future-Features)
3. [Technologies Used](#Technologies-Used)
4. [Testing](#Testing)
5. [Deployment](#Deployment)
6. [Credits](#Credits)
    - [Content](#Content)
    - [Media](#Media)
    - [Code](#Code)
7. [Acknowledgements](#Acknowledgements)
8. [Disclaimer](#Disclaimer)

---

# User Experience

## Project Goals

This project is being submitted as the forth and last Milestone Project in partial fulfillment of the Full Stack Developement Program at Code Institute.
The aim of this Milestone was to build a full-stack site based on business logic used to control a centrally-owned dataset.
The website had to use authentification mechanisms and provide paid access to the site's data, in this case for the purchase of products.

The main technologies to be used are [HTML](https://en.wikipedia.org/wiki/HTML), [CSS](https://en.wikipedia.org/wiki/CSS), [JS](https://www.javascript.com/), [Python](https://www.python.org/), [Django](), [Postgres](), and [Stripe]() + additional libraries.

## User Stories

### Website

* As a website owner, I want to create a website where users will be able to shop for plants and order their favourites. 
* As a website owner, I want people to be able find fun facts and tips about how to take care of their plant.
* As a website owner, I want to make a profit from the sell of plants on my website.

* As a user, I want to be able to shop and order plants on the website. 
* As a user, I want to find information on how to take care of my plants.


### Homepage

* As a website owner, I want the user to be able to understand the purpose of the website and be able to access the different tabs. 
* As a website owner, I want the user to find means to contact us in case of any question or problem.
* As a website owner, I want the homepage to be attractive for the user.
* As a website owner, I want the user to find a response to all questions about ordering plants on Monstera.

* As a user I want to be able to easily navigate the website.
* As a user, I want to find everything I am looking for in just a few clicks.


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

## Design

### Color Use

The website color scheme is consistent in the entire website and uses 3 colors, the green #5B9A3F, the grey #CAC8CF and the white #FFFFFF. The green is been chosen to match the main product of the website, plants. The grey is been used mainly for the text and to create a contrast with the green but maintaining an elegant style. And the white is been used to highlight other colors and give an elegant and modern look to the whole website.

![color palette](./image)

### Fonts

The font that I used for the whole website is Lora with a fallback of serif. The font is been taken from [Google Fonts](https://fonts.google.com/).

I chose this this font because in my opinion it suits the website and the style really well. To distinguish between the different types of text (title, paragraph, button...) I used different styles of the same font, like normal, **bold** or *italic*.

![font](./image)

### Icons

The icons used in this website are all from [Font Awesome](https://fontawesome.com/) and are used to better communicate the action of a button or the content of a tab and generally beautify the website.

### Images

The images are all been taken from [Unsplash]() in order to be without copyright.
The shortcut icon instead is been taken from [Favicon.io](https://favicon.io/) and it represents a leaf of the Monstera Deliciosa plant.

### Defensive Design

To inprove the safety of the website and protect its users, some measures have been used to avoid the misuse of forms:

* Newsletter

* The login and register pages have been added whit the [Allauth]() library and it takes care that the requirements for the fields are respected.

* When registering, an email will be sent to the email address used for the registration and the user will have to verify its identity by clicking on the provided link before being able to login.

* When selecting 'logout', the website will ask again if the user really wants to logout.

* When checking out, some fields of the shipping details will be required.

* When checking out, the 'phone-number' field will accept just digits, while the 'full name' one, will accept just letters anad spaces.

* Defensive error pages have been also created for the codes 400, 403, 404 and 500.

### Navigation

The website is been created with the user in mind. The scope is to make it as userfriendly and as instuitive as possible.
Here below you can find the navigation scheme.

![font](./image)

### Data Modelling

Tables to do

### Use of Database

In the developement phase the database used was sqlite3 (Django's default). On deployment instead, PostgreSQL is been used in Heroku.

### Wireframes

Here below you find the wireframes created to develop this website:

(Table with wireframes)

