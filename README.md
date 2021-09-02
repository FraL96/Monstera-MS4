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

<div align="right">
    <a href="#top">↥ Back to top!</a>
</div>

# Features

## Existing Features

* Navigation bar

The Navigation bar is the main way for the users to enter the pages.
Clicking on the logo, the user will be redirected home. On smaller devices, the logo will be a Monstera Deliciosa leaf.
The search bar in the center will help the user search plants (the queries are extended to both the name and the species of the plant).
On the right side, instead, there are the main four tabs:
- Shop: by clicking it a dropdown will display the categories of the plant and the user will be able to choose his/her favourite.
- Tips: a blog accessible for authenticated users. In Tips there will be articles about how to take care of the plants. There is also a comment section under the blog so that the users can interact with the website.
- Account: no click of this tab a dropdown menu will appear and the user will be able to decide if to Login or Register. After authentification, the user will be able to also access its profile tab.
- Cart: this tab will allow the user to access the cart and checkout. However, even without clicking it this tab have some functions. When the user will add product in its cart, the total amount under the cart will grow. Also from the same point a toast notification will show up in different moments to inform or warn the guest, In the toast there will be also a little preview of what's in the cart. 

Immediately under the navbar there is a banner informing the guests that, if they will spend more then €80, they will recieve a free gift of a baby plant.

<img src="readme/images/navbar.png" alt="Navbar" width="500px">
<img src="readme/images/minimenu.png" alt="Hamburger menu" width="500px">
<img src="readme/images/toast.png" alt="Hamburger menu" width="500px">

* Footer

In the footer there will be a smaller version of the logo that will also redirect to the home when clicked.
It also contains:
- The contacts (address, phone number and email address).
- The payments, to inform the guests about what card are we accepting.
- The newsletter tab
Underneath it also includes the links to [Facebook](https://www.facebook.com/), [Instagram](https://www.instagram.com/) and [YouTube](https://www.youtube.com/).
Lastly a separe part of the footer will display the website owner name, the year and the copyright. Besides, a little info icon can be clicked to access the FAQs page.

<img src="readme/images/footer.png" alt="Footer" width="500px">

* Homepage

The homepage is divided in 3 areas:
- The first one is purely to create the wow effect and attract the user.
- The second is a little shop menu where the user can easily pick the plant category he/she wants to browse.
- The third one is a carousel of fun fact about plants.

<img src="readme/images/home.png" alt="Homepage" width="500px">

* Shop

This section is divided into 5 categories (Shop All, Big leaves, To hang, Succulents and Cacti). On the vew of any category there will be a picture of the plant and near it the Name, Species and price. In the website owner view, it will also be visible an edit and a delete button.

<img src="readme/images/shop.png" alt="All recipes" width="500px">

* Product details

The recipe view displays the title with a picture and a few information about the recipe, like servings, difficulty level and ingredients.
Underneath the preparation of the recipe is displayed step by step.

<img src="readme/images/recipe-view.png" alt="Recipe View" width="500px">

* Casale del Giglio

In this page, there is a little explaination about the wine company. Moreover there is also a button linked to the website of the company.

<img src="readme/images/wine.png" alt="Casale del Giglio" width="500px">

* Profile

This page is accessible only after having registered or logged in. In this section the user will be able to add new recipes by clicking on the button.
He/she will also be able to review the added recipes, edit or delete them.

<img src="readme/images/profile.png" alt="Profile" width="500px">

* Add/Edit recipe

In the add page, a logged in user will have the possibility to fill up the form and add a new recipe to the website.
The edit form will be really similar but the fields will already contain the information of the recipe that the user would like to modify. Once modified, the user will have the possibility to save the changes or cancel them and go back to the previous version of the recipe.

<img src="readme/images/add.png" alt="Add recipe" width="500px">

* Log In / Registration

In the registration page, the user will be able to create a username and a password to access the profile page. The error handlers underneath the fields will help the user to create a valid username and password.
A flash message will show up if the user is already existent.
In the log in page, the registered user will be able to log in by filling up his/her username and password.
A flash message will appear if the username or password are incorrect.

<img src="readme/images/login-form.png" alt="Login" width="500px">

<img src="readme/images/register-form.png" alt="Register" width="500px">

## Future Features

In the future I would like to add to Italian Inside:
- The possibility for users to upload their picture of the recipe once they prepared it at home.
- The possibility for users to comment under the recipes and add their opinions or advices for other users.
- The user will recive an email after they register with a welcoming message and their log in credentials.
- Add videos of the preparation of the recipes
- To give the possibility to the user to create a "favorites" list
- Create real pages on social medias and advertise the website by teaching a few words in italian or sharing fun facts.
- Add a map that shows from where in the world are people using Italian Inside in order to show from where people are preparing and sharing their italian recipes.

