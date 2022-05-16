<h1 align="center">GolfShop</h1>

![Portfolio website](readme_img/AmIResponsive.png)

<span id="golfShop"></span>

The GolfShop is an online golf shop website that allows users to buy golf clubs and accessories.

Superusers can log in and add, edit and delete items in the shop.

I got inspraion from the application in the walk through that we did in this module, Botique Ado.

I used the walk through videos to help code the project.

**[View the live project here.](https://golfshopp5.herokuapp.com/)**

---

## Index 

- <a href="#ux">1. User experience (UX)</a>
  - <a href="#ux-goals">1.1. Project goals</a>
  - <a href="#ux-stories">1.2 User stories</a>
  - <a href="#ux-design">1.3 Design</a>
  - <a href="#ux-architecture">1.4 Information architecture</a>
  - <a href="#ux-mockup">1.5 Mockup designs</a>
- <a href="#features">2. Features</a>
  - <a href="#features-existing">2.1 Existing features</a>
  - <a href="#features-future">2.2 Features left to implement in the future</a>
- <a href="#technologies">3. Technologies used</a>
- <a href="#testing">4. Testing</a>
- <a href="#deployment">5. Deployment</a>
- <a href="#credits">6. Credits</a>
- <a href="#Acknowledge">7. Acknowledge</a>
- <a href="#Acknowledge">8. Disclaimer</a>

---

<span id="ux"></span>

<h1>1. User experience (UX)</h1>

<span id="ux-goals"></span>

### 1.1 Project goals 

- Making a full-stack site that allows users to manage a common dataset about a particular domain. 
- Making a full-stack site that uses HTML, CSS, JavaScript, Python+Flask and PostGresDB.
- Creating a website that serves as a platform where people shop online, create an account and add items to the site. 
- Creating a website that is simple to understand and easy to navigate.

<span id="ux-stories"></span>

### 1.2 User stories 

**First-time visitor goals:**
1. As a first time visitor, I want to be able to visit the website on every device, so that I can look at the website on desktop, mobile and tablet. 
2. As a first time visitor, I want to be able to navigate easily through the website, so I can find everything easily. 
3. As a first time visitor, I want to be able to add and remove items from my shopping basket.
4. As a first time visitor, I want to be able to search golf clubs by categories, so I can easily find the equipment I want. 
5. As a first time visitor, I want to register an account on the website, so I can buy golf accessories. 

**Site member goals:** 

All the goals of first-time visitors also apply for site members. There are additional user stories to the site members because they have more access to the website. See the additional user stories below. 
1. As a site member, I want to login to my profile.  
2. As a site member, I want to search for golf equipment.
3. As a site member, I want to buy the equipment. 
4. As a site member, I want to logout to my profile. 


**Admin goals:**

All the goals of the first time visitors and site members also apply for the admin. The admin has additional user stories to manage the categories of the golf accessories. 
1. As an admin, I want to be able to add, edit and delete an item to the website.
2. As an admin, I want to be able to approve a message before it is displayed in the website. 

<span id="ux-design"></span>

### 1.3 Design 

- #### Colour scheme 
I kept this website very neutral so that it doesnt take away from the golf images.  White for the header mild color scheme from colorwwall.com.   

![Colour scheme](readme_img/color.png)


- #### Fonts
The **Merriweather** are used throughout the whole website. Sans serif and cursive are the fallbacks in case the main font isn’t being imported to the site correctly.  

- #### Icons
In the project, for the golf club and user, I used the icons provided by [Font Awesome](https://fontawesome.com/).  

- #### Images
I collected the images from multiple sites including https://www.halpennygolf.com/. 

- #### Interactive design 

    - The website is basic and simple to use for the user.  Users can navigate the site easily and clearly find what they are looking for. 

<span id="ux-architecture"></span>

### 1.4 Information architecture
 I have crated a model for the categories and products and was able to add them using fitures using json files.  I have used allauth for my login and logout. 
 I have order models for the checkout and 

### 1.5 Mockup designs
Mockup designs are made with [Balsamic.](https://balsamiq.com/)

Click on the links below to view.
|    Mobile   |    Tablet / Desktop   | 
|    :----:    |     :----:   |   
|[golfShop](https://github.com/colmhaugh/GolfShop/blob/main/readme/balsamic/Golf%20for%20Android.bmpr)|[golfShop](https://github.com/colmhaugh/GolfShop/blob/main/readme/balsamic/Golfe%20for%20LargerScreens.bmpr) | 

<span id="features"></span>

<h1>2. Features</h1>

<span id="features-existing"></span>

### 2.1 Existing features 

#### 1. Design 
- A basic, uncluttered layout with consistency.
- Simple navigation throughout the website by using the navigation bar. 
- Displaying nice images, description and proces of the products.

#### 2. General 
- The home page has a header where the user can login, log out or create an account. 
- Users can search for a club on using the search bar. 
- Users can select select from a tab what club or accessory they want to see. 
- Users can navigate to a facebook shop page to help SEO. 

#### 3. Product
- Logged in super user can add, edit or delete an item. 
- Users can arrange the items by price, category or name. 
- Users can select a product and add it to the bag. 

#### 4. Shopping Bag 
- Users can add or remove items from their shopping bag. 
- Users can buy the app from the website.

#### 5. Signup, login and logout 
- Like in the walkthrough, I have used allAuth for to handle the login and logout. 
- People can create a new account on the web application. 
- People can login with their existing accounts. 
- People can easily log out.


<span id="features-future"></span>

### 2.2 Features left to implement in the future 
- Extra style to be added.
- Facebook page to be updated.

<span id="technologies"></span>

<h1>3. Technologies used</h1>

#### Languages used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - HTML5 provides the structure and the content for my project. 
- [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
    - CSS3 provides the style of the HTML5 elements.
- [jQuery](https://jquery.com/)
    - jQuery used as the JavaScript functionality.
- [Python](https://www.python.org/)
    - Python provides the backend of the project.
- [Django](https://www.djangoproject.com/)
    - Python-based framework that follows the model–template–views architectural pattern.


#### Frameworks, libraries & Other
- [Gitpod](https://www.gitpod.io/) 
    - The GitPod is used to develop the project.
- [Git](https://git-scm.com/)
    - The Git was used for version control to commit to Git and push to GitHub.
- [GitHub](https://github.com/)
    - The GitHub is used to host the project.
- [Balsamic](https://balsamiq.com/)
    - Balsamic is used to create the mockup designs for the project.
- [PostgreSQL](https://www.postgresql.org/)
    - PostgreSQL is the open Source Relational Database that was used for the project.
- [Heroku](https://dashboard.heroku.com/)
    - Heroki is the cloud platform to deploying the app.
- [AllAuth](https://django-allauth.readthedocs.io/en/latest/)
    - Django-allauth was used for registeration, login and log out.
- [AWS Amazon](https://aws.amazon.com/)
    - AWS Amazon is used to store static and media files.
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
    - Boto3 is used for compatibility in AWS.
- [Gunicorn](https://pypi.org/project/gunicorn/)
    - Gunicorn is used to enable deployment to Heroku.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - Django Crispy Forms is used to style the Django forms
- [Stripe](https://stripe.com/en-nl)
    - Stripe is used for the secure payments.
- [SQlite3](https://www.sqlite.org/index.html)
    - SQlite3 is used as the development database.
- [PostgreSQL](https://www.postgresql.org/)
    - PostgreSQL is used as the production database.

#### Testing tools used 
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/open) is used to detect problems and test responsiveness.
- [Autoprefixer](https://autoprefixer.github.io/)
    - Autoprefixer is used to parse the CSS and to add vendor prefixes to CSS rules. 
- [W3C Markup Validation Service](https://validator.w3.org/)
    - The W3C Markup Validation Service is used to check whether there were any errors in the HTML5 code. 
- [W3C CSS validator](https://jigsaw.w3.org/css-validator/)
    - The W3C CSS validator is used to check whether there were any errors in the CSS3 code.
- [JShint](https://jshint.com/)
    - JShint is a JavaScript validator that is used to check whether there were any errors in the JavaScript code. 
- [PEP8](http://pep8online.com/)
    - The PEP8 validator is used to check whether there were any errors in the Python code.

<span id="testing"></span>

<h1>4. Testing</h1>

## 1. Code validators
 - **[HTML Validator](https://validator.w3.org/):** Some errors due to django.
    - With testing the HTML code, I had some syntax issues on all pages I build with django templating.
    - I tested the HTML code by running my server locally and used view page source. This code I passed through the validator.
    - Some doctype errors that can be ingored as seen on slack chat.

- **[CSS Validator](https://jigsaw.w3.org/css-validator/):** No errors found.

- **[Python validator | PEP8](http://pep8online.com/):** No errors found

---

<span id="responsiveness"></span>

## 2. Responsiveness 
- Responsiveness of the project is tested with [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools).
- The project is tested on the following devices: 
    - Desktop, Mobile & Tablet.  
    - On ChromeDevTools used some of their devices for further testing.

---

## 4. Testing user stories 

1. As a user i want to click on a golf accessory so that I can see the the details of the product. 
    - The user can click on a product and a detail page will open with the details required.
2. As a user i want to view a paginated list of products so that I can select what product I want to view. 
    - The user will see see a set ammount of products depending on the screen size. 
3. As a user i want to add and remove items from my shopping basket.
    - A user add and remove products from basket. 
4. As a user i want to be able to search for a product.
    - A logged in user can enter text into the search bar and find a product they want.  
5. As an Administrator, i want to add, remove and edit a product so that other users can view my products.
    - I added products as an admin. 
6. As a user i want to be able to register an account.
    - I created and deleted test user accounts.  All this was handled by allAuth.
7. As a user i want to be able to list the products in different orders so that i can view the list order by price or category.
    - I added order functionality and tested in the app.


<h1>5. Deployment</h1>

#### Requirements 
- Python3 
- Github account 
- Heroku account

#### Clone the project 
To make a local clone, follow the following steps. 
1. Log in to GitHub and go to the repository. 
2. Click on the green button with the text **“Code”.**
3. Click on **“Open with GitHub Desktop”** and follow the prompts in the GitHub Desktop Application or follow the instructions from **[this link](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop)** to see how to clone the repository in other ways. 


#### Heroku Deployment  
1. Set up local workspace for Heroku 
    - In terminal window of your IDE type: **pip3 freeze -- local > requirements.txt.** (The file is needed for Heroku to know which filed to install.)
    - In termial window of your IDE type: **python app.py > Procfile** (The file is needed for Heroku to know which file is needed as entry point.)
2. Set up Heroku: create a Heroku account and create a new app and select your region. 
3. Deployment method 'Github'
    - Click on the **Connect to GitHub** section in the deploy tab in Heroku. 
        - Search your repository to connect with it.
        - When your repository appears click on **connect** to connect your repository with the Heroku. 
    - Go to the settings app in Heroku and go to **Config Vars**. Click on **Reveal Config Vars**.
        - Enter the variables contained in your env.py file. it is about: **CLOUDINARY_URL, DATABASE_URL, SECRET_KEY**
4. Push the requirements.txt and Procfile to repository. 
     ```
    $ git add requirements.txt
    $ git commit -m "Add requirements.txt"

    $ git add Procfile 
    $ git commit -m "Add Procfile"
    ```
5. Automatic deployment: Go to the deploy tab in Heroku and scroll down to **Aotmatic deployments**. Click on **Enable Automatic Deploys**. By **Manual deploy** click on **Deploy Branch**.

Heroku will receive the code from Github and host the app using the required packages. 
Click on **Open app** in the right corner of your Heroku account. The app wil open and the live link is available from the address bar. 


<span id="credits"></span>

<h1>6. Credits</h1>

This project is based on the Botique Ado walkthrough project and also using project example Idea 2.  A lot of the code that I used in the walkthrough project I also used on this project.

#### Products
- I got the product images, price and details from various online golf shops, mainly [halpennygolf](https://www.halpennygolf.com/). 

#### Code
- Code Institute walkthrough project I think therefore I blog.

<span id="Acknowledge"></span>

<h1>7. Acknowledge</h1>

Thanks to the following people and organizations who helped or inspired me for the project:  
- The support from Kasia and my class mates.
- The support and guidance of my mentor Precious Ijege. 
- The lessons and knowledge of [Code Institute.](https://codeinstitute.net/)
- The advice about bugs from Slack community.

Thanks for visiting

<a href="#golfShop">Back to top!</a>