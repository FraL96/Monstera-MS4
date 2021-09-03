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
- Tips: a blog wher user will find articles about how to take care of the plants. There is also a comment section under the blog so that the users can interact with the website.
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
- The newsletter tab (the guest that will insert their email address, will automatically receive a welcome email).
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

This section is divided into 5 categories (Shop All, Big leaves, To hang, Succulents and Cacti). On the page of any category there will be a picture of the plant and near it the Name, species and price. In the website owner view, it will also be visible an edit and a delete button.

<img src="readme/images/shop.png" alt="All recipes" width="500px">

* Product details

After clicking on a plant, the user will access the product view where will find the same information from the shop view plu more details about the plant and how to take care of it. Moreover there will be also the possiblity to select how many plants of the same kind the user want to purchase (the price will grow in real time with the change of quantity to help the user)and a button to move the plants to the cart.

* Tips

Tips is a blog everyone can view. There is first an overview of the articles and, when clicking on one of them the user will access a second page. The second page will have the entire text of the article selected plus a section below where to view past comments and add new ones. The comments that will be submitted will have to be approved by the website moderator before appearing underneath the article.

* Account

In this tab a not authenticated user will have the possibility to login (a tab for users that forgot their password is included in this tab) or register. The authenticated user instead, will be able to access his/her profile page. The profile page is divided in 2 zones. In one the user can save his/her delivery information to avoid writing it for every order. In the second part the user can view and access the 'confirmation' page of past orders and review all the information.

* Add products

This page will only be visible to an authenticated superuser. In this view, the superuser can add new products to the shop.

* Cart

In the cart the user will find all the plants he previously added, the quantities and the total price. Users that spend over €100 euros will not have to pay for delivery, while the ones that will not reach this sum will pay a 10% of their cart. Moreover at Monstera at the moment there is a promotion: for every €80 spent, we will send to the user also a free baby plant. The user will be informed of this by the banner under the navbar or by the fact that if the cart contains already €80 euros of products, a new line will be added with the gift.

* Checkout

Once the user have decided what to buy, in the checkout page they will be able to fill in their details (or retrieve them from they profile if they previously set them) and inser their credit card details. Also in this page it will be provided a little overview of the purchase. These information will also be sent by mail to the user.

* Confirmation

If the users inserted all the necessary information and proceeded with the purchase, they will then be recirected to the confirmation page where they will find information regarding their order (like the order number, the products the delivery info and the total price). On the top it will be also attched the little info logo to review the FAQs.

* FAQ

This page contains a few answers to the most common questions about order, delivery and refunds.

## Future feature

* Newsletter: In the future I would like to create a way so that the users will receive every month a freebie in their email. It can be another gift to receive with the next order, a digital content or a dicount. This means that a field for promotional codes will have to be added to the checkout tab.

* Tips (blog): I would like in future to improve the blog by adding images and restyling the content of the article. Also I would like to make it only accessible for authenticated users. Moreover I would like to add a tempate to add, edit and delete articles and moderate comments directly from the frontend.

* I would also like to add paginstion to my shop

* I would like to allow reviews in the product details page.

* Adding login with social media.


# Technologies Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5) - Used to create the structure of the website.
* [CSS3](https://en.wikipedia.org/wiki/CSS) - Used to style the website.
* [Django]() - Used as the main framework
* [JQuery](https://jquery.com/) - Used to add interactive features to the website.
* [Python3](https://www.python.org/) - Used to create the backend of the website.
* [Heroku](https://dashboard.heroku.com/apps) - Used to deploy my website.
* [Balsamiq](https://balsamiq.com/) - Used to design the Wireframes.
* [Bootsrap]() - Used to add functionality and beautify the website.
* [Gitpod](https://www.gitpod.io/) - Used to design and host the project.
* [GitHub](https://github.com/) - Used to hold the repository.
* [Google fonts](https://fonts.google.com/) - Used to add fonts to the website.
* [AmIResponsive](http://ami.responsivedesign.is/#) - Used for the READ ME cover picture.
* [Fontawesome](https://fontawesome.com/v4.7.0/) - used for the icons.
* [PEP8](https://www.python.org/dev/peps/pep-0008/) - Used to maintain a proper style in the Python code.
* [Chrome DevTools](https://developer.chrome.com/docs/devtools/) - Used to test responsiveness and identify bugs.
* [Autoprefixer](https://autoprefixer.github.io/) - Used to parse my CSS code.
* [W3C Markup Validation Service](https://validator.w3.org/) - Used to identify errors in the HTML code.
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - Used to identify errors in the CSS code.
* [Google Lighthouse](https://developers.google.com/web/tools/lighthouse) - Used to verify performance.
* [Postrges]() -
* [AWS]() - 
* [Boto]() - Used for compatibility in AWS.
* [Gunicorn]() - Used with Heroku for deployment
* [Spycopg2]() - Link between Postgres and Django
* [Django Crispy Forms]() - Used to add forms
* [Stripe]() It is used so that the users can access
* [Mailchimp]() Is used for the newsletter




