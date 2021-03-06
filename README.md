<h1 align="center">MONSTERA</h1>
<h2 align="center">the future is green</h2>

![Monstera](./media-readme/home-readme.png)

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

The main technologies to be used are [HTML](https://en.wikipedia.org/wiki/HTML), [CSS](https://en.wikipedia.org/wiki/CSS), [JS](https://www.javascript.com/), [Python](https://www.python.org/), [Django](https://www.djangoproject.com/), [Postgres](https://www.postgresql.org/), and [Stripe](https://stripe.com/en-ie) + additional libraries.

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

![Colors](./media-readme/color-scheme.png)

### Fonts

The font that I used for the whole website is Lora with a fallback of serif. The font is been taken from [Google Fonts](https://fonts.google.com/).

I chose this this font because in my opinion it suits the website and the style really well. To distinguish between the different types of text (title, paragraph, button...) I used different styles of the same font, like normal, **bold** or *italic*.

![font](./media-readme/lora.png)

### Icons

The icons used in this website are all from [Font Awesome](https://fontawesome.com/) and are used to better communicate the action of a button or the content of a tab and generally beautify the website.

### Images

The images are all been taken from [Unsplash](https://unsplash.com/s/photos/plants) in order to be without copyright.
The shortcut icon instead is been taken from [Favicon.io](https://favicon.io/) and it represents a leaf of the Monstera Deliciosa plant.

### Defensive Design

To inprove the safety of the website and protect its users, some measures have been used to avoid the misuse of forms:

* Newsletter

* The login and register pages have been added whit the [Allauth](https://django-allauth.readthedocs.io/en/latest/installation.html) library and it takes care that the requirements for the fields are respected.

* When registering, an email will be sent to the email address used for the registration and the user will have to verify its identity by clicking on the provided link before being able to login.

* When selecting 'logout', the website will ask again if the user really wants to logout.

* When checking out, some fields of the shipping details will be required.

* When checking out, the 'phone-number' field will accept just digits, while the 'full name' one, will accept just letters anad spaces.

* Defensive error pages have been also created for the codes 400, 403, 404 and 500.

### Data Modelling

### 1. Profile app 
#### UserProfile model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 User | user | OneToOneField |  User, on_delete=models.CASCADE
 Full Name | default_full_name | CharField | max_length=50, null=True, blank=True
 Phone number | default_phone_number | CharField | max_length=20, null=True, blank=True
 Street address 1 | default_street_address1 | CharField | max_length=80, null=True, blank=True
 Street address 2 | default_street_address2 | CharField | max_length=80, null=True, blank=True
Town/City | default_town_or_city | Charfield | max_length=40, null=True, blank=True
County | default_county | CharField | max_length=80, null=True, blank=True
Postcode | profile_postcode | CharField | max_length=20, null=True, blank=True
Country | profile_country | CountryField | blank_label='Country', null=True, blank=True
 

#### 2. Products app 
#### Category model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 name | name | CharField | max_length=254
 Friendly name | friendly_name | CharField | max_length=254, null=True, blank=True

 #### Product model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Category| category| ForeignKey | Category, null=True, blank=True, on_delete=models.SET_NULL
 Sku number | sku | CharField | max_length=40, null=True, blank=True
 Name| name | CharField | max_length=250
 Species | species | CharField |  max_length=250
 Description| description | TextField | null=True, blank=True
 Price | price | DecimalField | max_digits=5, decimal_places=2, null=False, default=0
 Image | image | ImageField | null=True, blank=True

#### 3. Checkout app 
#### Order model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Order number | order_number | CharField | max_length=32, null=False, editable=False
 User profile | user_profile | ForeignKey | UserProfile, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders'
 Full name | full_name | CharField | max_length=50, null=False, blank=False
 Email| email| EmailField | max_length=254, null=False, blank=False
 Phone number | phone_number | Charfield | max_length=20, null=True, blank=True
 Street address 1 | street_address1 | CharField | max_length=80, null=True, blank=True
 Street address 2 | street_address2 | CharField | max_length=80, null=True, blank=True
 Town/City | town_or_city | CharField | max_length=40, null=True, blank=True
 Postcode | postcode| CharField | max_length=20, null=True, blank=True
 County | county | ChartField | max-length=80, null=True, blank=True
 Country| country | CountryField | blank_label='Country *', null=False, blank=False
 
 | **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Date | date | DateTimeField | auto_now_add=True
 Delivery cost | delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0
 Order total | order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
 Grand total | frand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0
 Original cart | original_cart | TextField | null=False, blank=False, default=''
 Stipe pid | stripe_pid | CharField | max_length=254, null=False, blank=False, default=''

 #### OrderLineItem model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Order  | order | ForeignKey | Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems'
 Product | product | ForeignKey | Product, null=False, blank=False, on_delete=models.CASCADE
 Quantity | quantity | IntegerField | null=False, blank=False
 Lineitem total | lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False

#### 4. Newsletter app 
#### Subscribe model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
 Email | email| EmailField | max_length=255
 Timestamp | timestamp | DateTimeField | auto_now_add=True

 #### 5. Blog app
 #### Article model

| **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
title | title | CharField | max_length=200, unique=True
slug | slug | SlugField | max_length=200, unique=True
author | author | ForeignKey | User, on_delete=models.CASCADE, related_name='blog_articles'
updated_on | updated_on  | DateTimeField | auto_now=True
content | content | TextField
created_on | created_on  | DateTimeField | auto_now_add=True
status | status | IntegerField |choices=STATUS, default=0


 #### Comment model

 | **Name** | **Database Key** | **Field Type** | **Validation** |
--- | --- | --- | --- 
article | article | ForeignKey(Article, on_delete=models.CASCADE,related_name='comments'
name | name | CharField | max_length=80
email | email | EmailField | 
body | body |TextField | 
created_on | created_on | DateTimeField | auto_now_add=True
active | BooleanField | default=False

### Use of Database

In the developement phase the database used was sqlite3 (Django's default). On deployment instead, PostgreSQL is been used in Heroku.

### Wireframes

Here below you find the wireframes created to develop this website:



* [Mobile](./media-readme/wireframes/monstera-mobile.pdf)
* [Desktop](./media-readme/wireframes/monstera-desktop.pdf)

<div align="right">
    <a href="#top">??? Back to top!</a>
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

Immediately under the navbar there is a banner informing the guests that, if they will spend more then ???80, they will recieve a free gift of a baby plant.

![Navbar](./media-readme/navbar.png)

* Footer

In the footer there will be a smaller version of the logo that will also redirect to the home when clicked.
It also contains:
- The contacts (address, phone number and email address).
- The payments, to inform the guests about what card are we accepting.
- The newsletter tab (the guest that will insert their email address, will automatically receive a welcome email).
Underneath it also includes the links to [Facebook](https://www.facebook.com/), [Instagram](https://www.instagram.com/) and [YouTube](https://www.youtube.com/).
Lastly a separe part of the footer will display the website owner name, the year and the copyright. Besides, a little info icon can be clicked to access the FAQs page.

![Footer](./media-readme/footer.png)

* Homepage

The homepage is divided in 3 areas:
- The first one is purely to create the wow effect and attract the user.
- The second is a little shop menu where the user can easily pick the plant category he/she wants to browse.
- The third one is a carousel of fun fact about plants.

![Homepage](./media-readme/home.png)

* Shop

This section is divided into 5 categories (Shop All, Big leaves, To hang, Succulents and Cacti). On the page of any category there will be a picture of the plant and near it the Name, species and price. In the website owner view, it will also be visible an edit and a delete button.

![Shop](./media-readme/products.png)


* Product details

After clicking on a plant, the user will access the product view where will find the same information from the shop view plu more details about the plant and how to take care of it. Moreover there will be also the possiblity to select how many plants of the same kind the user want to purchase (the price will grow in real time with the change of quantity to help the user)and a button to move the plants to the cart.

![Product details](./media-readme/product_detail.png)


* Tips

Tips is a blog everyone can view. There is first an overview of the articles and, when clicking on one of them the user will access a second page. The second page will have the entire text of the article selected plus a section below where to view past comments and add new ones. The comments that will be submitted will have to be approved by the website moderator before appearing underneath the article.

![Tips](./media-readme/tips.png)

* Account

In this tab a not authenticated user will have the possibility to login (a tab for users that forgot their password is included in this tab) or register. The authenticated user instead, will be able to access his/her profile page. The profile page is divided in 2 zones. In one the user can save his/her delivery information to avoid writing it for every order. In the second part the user can view and access the 'confirmation' page of past orders and review all the information.

![Account](./media-readme/profile.png)


* Add products

This page will only be visible to an authenticated superuser. In this view, the superuser can add new products to the shop.

![Add](./media-readme/add.png)


* Cart

In the cart the user will find all the plants he previously added, the quantities and the total price. Users that spend over ???100 euros will not have to pay for delivery, while the ones that will not reach this sum will pay a 10% of their cart. Moreover at Monstera at the moment there is a promotion: for every ???80 spent, we will send to the user also a free baby plant. The user will be informed of this by the banner under the navbar or by the fact that if the cart contains already ???80 euros of products, a new line will be added with the gift.

![Cart](./media-readme/cart.png)


* Checkout

Once the user have decided what to buy, in the checkout page they will be able to fill in their details (or retrieve them from they profile if they previously set them) and inser their credit card details. Also in this page it will be provided a little overview of the purchase. These information will also be sent by mail to the user.

![Checkout](./media-readme/checkout.png)

* Confirmation

If the users inserted all the necessary information and proceeded with the purchase, they will then be recirected to the confirmation page where they will find information regarding their order (like the order number, the products the delivery info and the total price). On the top it will be also attched the little info logo to review the FAQs.

![Order success](./media-readme/checkout-success.png)

* FAQ

This page contains a few answers to the most common questions about order, delivery and refunds.

![Faq](./media-readme/faq.png)


## Future feature

* Newsletter: In the future I would like to create a way so that the users will receive every month a freebie in their email. It can be another gift to receive with the next order, a digital content or a dicount. This means that a field for promotional codes will have to be added to the checkout tab.

* Tips (blog): I would like in future to improve the blog by adding images and restyling the content of the article. Also I would like to make it only accessible for authenticated users. Moreover I would like to add a tempate to add, edit and delete articles and moderate comments directly from the frontend.

* I would also like to add paginstion to my shop

* I would like to allow reviews in the product details page.

* Adding login with social media.

<div align="right">
    <a href="#top">??? Back to top!</a>
</div>


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
* [Postrges](https://www.postgresql.org/) - For the database
* [AWS](https://aws.amazon.com/) - For static and media
* [Boto](http://boto.cloudhackers.com/en/latest/) - Used for compatibility in AWS.
* [Gunicorn](https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/gunicorn/) - Used with Heroku for deployment
* [Spycopg2](https://www.psycopg.org/) - Link between Postgres and Django
* [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Used to add forms
* [Stripe](https://stripe.com/en-ie) It is used so that the users can access
* [Mailchimp](https://mailchimp.com/) Is used for the newsletter

<div align="right">
    <a href="#top">??? Back to top!</a>
</div>

# Testing

This chapter is displayed in a different file. Click [here](./TESTING.md) to go to Testing.

<div align="right">
    <a href="#top">??? Back to top!</a>
</div>

# Deployment

Please consult the requirements.txt file for the necessary installs.

**How to clone this project:**

1. Log in to github and go to the [Monstera](https://github.com/FraL96/Monstera-MS4) repository.
2. Click on the big Code button , near the green one.
3. Copy the URL.
4. Open Gitbash from your computer and write 'git clone', paste the copied link and execute.
5. Type "git clone", paste the URL and press "enter".

**How to run this code locally:**

1. In the terminal: Install all your requirements with pip3 install -r requirements.txt.
2. Create a gitignore file to ignore all passwords.
3. Create an env.py file and add to it the following code (make sure env.py is part of gitignore):

     ```
    Import os
    os.environ("SECRET_KEY", "Added by developer")
    os.environ("STRIPE_PUBLIC_KEY", "Added by developer")
    os.environ("STRIPE_SECRET_KEY", "Added by developer")
    os.environ("STRIPE_WH_SECRET", "Added by developer")
    os.environ("MAILCHIMP_API_KEY", "Added by developer")
    os.environ("MAILCHIMP_DATA_CENTER", "Added by developer")
    os.environ("MAILCHIMP_EMAIL_LIST_ID", "Added by developer")

4. Execute 'make migrations' and 'migrate'
5. Add the file db.json with all the products.
6. Create a superuser to access the admin in the backend.
7. type 'python3 manage.py runserver to open the website preview.
8. Check if the data is been added correctly (you can access it by just typing ' /admin' after the urls link.).

**How to deploy to Heroku:**

1. Execute 'pip3 freeze -- local > requirements.txt.' to be sure all the files we need are in there.
2. Go tu heroku and select 'new' by clicking on the button on the right and then 'Create new app'. Fill up all the fields that heroku asks you to, automate the GitHub's deploy (Select Connect To Github - search your repository - select it - Enable automatic deploys) and stop when you are back in the overview of the project.
3. Back in your IDE, create a Procfile file with inside 'web: gunicorn <name app>.wsgi:application' and then add - commit - push.
4. In heroku, go to 'Resources' and add the free veraion of Postges.
5. Then, go in settings and, after clicking reveal vars, add all these.

    | KEY            | VALUE         |
    |----------------|---------------|
    | AWS_ACCESS_KEY_ID | `<aws access key>`  |
    | AWS_SECRET_ACCESS_KEY | `<aws secret access key>`  |
    | DATABASE_URL| `<postgres database url>`  |
    | EMAIL_HOST_PASS | `<email password>` |
    | EMAIL_HOST_USER| `<email address>`  |
    | MAILCHIMP_API_KEY| `<api key>`  |
    | MAILCHIMP_DATA_CENTER| `<datacenter id>`  |
    | MAILCHIMP_EMAIL_LIST_ID| `<emailist id>`  |
    | SECRET_KEY | `<your secret key>`  |
    | STRIPE_PUBLIC_KEY| `<your stripe public key>`  |
    | STRIPE_SECRET_KEY| `<your stripe secret key>`  |
    | STRIPE_WH_SECRET| `<your stripe wh key>`  |
    | USE_AWS | `True`  |


6. Copy and paste the Postgres URL as 'DATABASE_URL' in the settings.py of Monstera. This is just a temporary precedure and this piece of code will be changed in a few steps more.

    ```
    DATABASES = {
        'default': dj_database_url.parse("<DATABASE_URL here>")
         }
    ```
7. Remember to migrate here and to create a superuser if you didn't yet.

8. At this point you can reset the database to the old line.

9. Add the heroku app URL to the ALLOWED HOSTS

10. Add - Commit -Push

<div align="right">
    <a href="#top">??? Back to top!</a>
</div>

# Credits

## Content

* The text for the FAQ and the blog posts are from [PLNTS.com](https://plnts.com/).
* The plants information are my own knowledge
* The text from the carousel is from [Burnett's country garden](https://burnettscg.com/5-fun-facts-about-house-plants/).
* The comments of the blog are invented by me.

## Media

* The images (without Copyright) are all from [unsplash.com](https://unsplash.com/s/photos/plants).
* The logo is been created by me with [Canva](https://www.canva.com/).
* The little logo is from [thenounproject.com](https://thenounproject.com/term/monstera/3538859/).
* The icons are from [font awesome](https://fontawesome.com/).
* The tab icon is from [favicon.com](https://favicon.io/).
* The color scheme is been chosen on [hexcolortool.com](https://www.hexcolortool.com/#88c46e)

## Code

* For position elements I consulted [W3School](https://www.w3schools.com/).
* Many graphic elements are from [Bootstrap](https://getbootstrap.com/).
* I used [Django central](https://djangocentral.com/creating-comments-system-with-django/) to create the blog and its comment section.
* I used [Mailchimp](https://mailchimp.com/) for the newsletter.
* I used [StackOverflow](https://stackoverflow.com/) to create the price that changes in real time with the cange of quantity.
* I used the videos from [Code Institute](https://learn.codeinstitute.net/ci_program/diplomainsoftwaredevelopment) - Boutique Ado to see how to start designing the website.
* I used [Stripe Docs](https://stripe.com/docs) to add the credit card bar in checkout.

<div align="right">
    <a href="#top">??? Back to top!</a>
</div>

# Acknowlegment

I want to truly thank this amazing group of people that inspired and sustained me into completing this project.

* My mentor [Precious Ijege](https://www.linkedin.com/in/precious-ijege-908a00168/) that gave me great advices and helped me solve all the questions and doubts I had.
* The extraorinary tutors Jo, Shirley, Igor and Micheal that gided me into identifying and solving bugs in my code.
* My better half, [Cathal Moore](https://www.facebook.com/cathal.moore.39), always there to give me strenght and never complaining when I ramble about coding stuff 24/7.
* My parents, [Gabriele e Monica Lupu](https://www.facebook.com/lupu.emonica) and grandparents, my biggest sustainers from day one.
* [Declan](https://www.linkedin.com/in/declan-moore-83728b80/) and Ann Moore, my second family and the people that first introduced me to IT. Without them I would not be the same person I am today.

# Disclaimer

This website is for educational purposes only. For any concerns about images or content, please contact me at : francesca_lupu@live.it

<div align="right">
    <a href="#top">??? Back to top!</a>
</div>




