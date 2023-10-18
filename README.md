# Snowpatrol


![Am I Responsive image]()

Please view the live website here: [Snowpatrol](https://snowpatrol-6b2d334410bf.herokuapp.com/ "Snowpatrole Homepage").

## Table of contents
+ [UX](#ux)
  + [Site Purpose](#site-purpose)
  + [Site Goal](#site-goal)
  * [Future Goals](#future-goals)
* [User Stories](#user-stories)
  * [Site User](#as-a-site-user)
  * [Admin](#as-a-admin)
* [Design](#design)
  * [Wireframes](#wireframes)
  * [Color Scheme](#color-scheme)
  * [Typeography](#typography)
  * [Imagery](#imagery)
* [Features](#features)
  * [Homepage](#homepage)
  * [Add Recipes](#add-recipes)
  * [Recipes Home](#recipes-home)
  * [Recipes Detail](#recipes-detail)
  * [Edit ecipes](#edit-recipes)
  * [Delete ecipes](#delete-recipes)
  * [Contact](#contact-page)
  * [Sign-In](#sign-in)
  * [Sign-Out](#sign-out)
  * [Sign-Up](#sign-up)
* [C.R.U.D.](#crud)
  * [Create](#create)
  * [Read](#read)
  * [Update](#update)
  * [Delete](#delete)
* [Manual Testing](#manual-testing)
* [Admin Panel](#admin-panel)
* [Validator Testing](#validator-testing)
* [Defensive Validation](#defensive-validation)
* [Accessibility](#accessibility)
* [Fixed bugs](#fixed-bugs)
* [Technologies Used](#technologies-used)
* [Deployment](#deployment)
* [Credits](#credits)

## UX
### Site Purpose


### Site Goal


### Future Goals


## User Stories


### As a site user: 

### As a login user:

### As a Admin:


## Agile Methodology

The development of this project was managed and implemented using GitHub Projects Kanban Board. Available here:
<a href="https://github.com/users/Karroroenning/projects/7" target="_blank" rel="noopener" aria-label="Link to GitHub Projects">Snowpatrol - User Stories</a>

<br>

## Design
### Wireframes

- A low-fi wireframe was build before developing the website.
- This was done in Balsamiq Wireframes. 

<details><summary>Home Page</summary>
<img src="" >
</details>

<details><summary>Product Page</summary>
<img src="" >
</details>

<details><summary>Product Detail</summary>
<img src="" >
</details>

<details><summary>Blog list</summary>
<img src="" >
<img src="" >
</details>

<details><summary>Blogpost</summary>
<img src="" >
</details>

<details><summary>Signup</summary>
<img src="" >
</details>

<details><summary>Login</summary>
<img src="" >
</details>

<details><summary>Logout</summary>
<img src="" >
</details>


### Color Scheme
<img src="" >

I want the colors to give a calming and modern feeling. I have chosen to have a light background so that there will be a good contrast between the important thing that should be seen the most and the background. It must not flow together because it can be perceived as disturbing to the eye. 

### Typography:

All fonts were obtained from the Google Fonts library. I have chosen the same font throughout the web page. A simple typeface that does very well with the rest.

Font: Lato

### Imagery:

- For the first page, I want an image that shows what the page has to offer. 
<details><summary>Hero Image</summary>
<img src="" >
</details>

<br>


- For the placeholder image
<details><summary>Placeholder image</summary>
<img src="" >
</details>

<br>
- All other images


## Features
### Homepage


### Add Recipes

### Recipes Sites


### Recipes detail


### Edit Recipes


### Delete Recipes


### Contact Page


### Sign-in


### Sign-out


### Sign-up

## Products
products are what is the main focus of the e-commerce website. Admins can add, edit, and delete the service, select the customized options, add related image, and descriptions.

### CRUD
- **Create:** If the user is an authenticated superuser, they can add a new service by clicking the profile icon in the top right corner and selecting Add service
- **Read:** All users can view the current services in the services section
- **Update:** Only admins can edit the existing service
- **Delete:** Only admins can delete the existing service

## Reviews
Registered users can review every order made. The option "Review me!" is added to the order history accessible via the profile page.

### CRUD
- **Create:** After the order is paid, the registered user can add a review
- **Read:** All users can view the current reviews in the customer ratings section
- **Update:** Only the author of the review can edit the review via frontend
- **Delete:** Only the author of the review can delete the review via frontend

## Blog
Admins (superusers) can add blog posts in the blog sections. The reason for this is to convince potential buyers that we are reliable in what we do and that we know our stuff (all posts are related to the services we provide).

### CRUD
- **Create:** Admins can add new blog posts to the blog page
- **Read:** All users can read the current blog posts listed in the blog section
- **Update:** Admins can edit the existing blog posts on the blog page
- **Delete:** Admins can delete existing blog posts on the blog page


## Manual Testing

### Not logged in:

### Homepage
I have manually tested every link on the homepage to ensure that it redirects to the appropriate url. 

# Testing
## Manual Testing
 | Feature | Test  | Expected Result | Actual Result |
| -------------| ----- | ----- | :----: |
| PACK AND STASH  | Selecting logo on homepage |  directs user back to homepage |  Pass |
| Search | Using the search box | Entering a search returns expected result  |  Pass |
| Search no results | No search | Entering a no results search returns error message and shows all products  |  Pass |
| Navigation Links  | Selecting navigation links |  directs user to relevant pages |  Pass |
| All products  | Selecting all products |  directs user to all products |  Pass |
| Back to top | Back to top arrow | Select the arrow box on the products page brings the user back to the top of the page  |  Pass |
| Sort By  | Selecting the filter Sort |  successfully sort by price, name and category options |  Pass |
| Shop Now button  | Selecting Shop Now button |  directs user to all  products page |  Pass |
| About Us | Selecting About Us |  directs user to About Us page |  Pass |
| Sign up for our newsletter | selecting Sign up for our newsletter |  directs user Sign up for our newsletter page |  Pass |
| Privacy policy | Selecting privacy policy |  directs user to privacy policy|  Pass |
| facebook icon | Selecting  facebook icon |  directs user to facebook page |  Pass |
| Special offers | Selecting all specials |  directs user to all special offers |  Pass |
| Blog | Selecting blog |  directs user to blog page |  Pass |
| Blog detail | Selecting Blog detail |  directs user to blog detail |  Pass |
| Leave a Comment when signed in | Submitting comment|  successfully submit and display comment |  Pass |
| Add blog | Adding a new blog | successfully add new blog to blog page  |  Pass |
| As Admin edit blog | editing blog|  successfully edited the blog |  Pass |
| As Admin Delete Comment | Deleting comment|  successfully remove comment |  Pass |
| Contact | Selecting Contact | directs user to contact page  |  Pass |
| Contact form submission | submitting contact form | successfully sends submit form and can seen be in admin |  Pass |
| My account | Selecting my account as admin | displays dropdown menu unique to admin apart from profile and logout  |  Pass |
| Add product | Adding a new product| successfully add new product to products page  |  Pass |
| Add Product | no image is selected | default image is used |  Pass |
| As Admin edit product | editing product |  successfully edited the product |  Pass |
| As Admin Delete product | Deleting product|  successfully remove product |  Pass |
| Register | Register for an account | selecting Register in my account directs user signup page |  Pass |
| Register | Registering as a new user | Registering as a new user form works |  Pass |
| Login | Login to an account | selecting Login in my account directs user to Login page |  Pass |
| Login | Login to an account | login-in as a new user form works |  Pass |
| Login as admin| Login to as admin gives access to blog/product management | login-in as a new user form works |  Pass |
| Logout | message shown | Logging out message shown |  Pass |


### Browsers
- I checked the site for compatibility on different browsers.
- I have checked the responsiveness on different window sizes.

## Validator Testing
#### HTML files pass through the W3C validator with no issues found.
<details><summary>- Add recipes</summary>
<img src="documentation/html-validations/html_validator_add_recipes.png" >
</details>

<details><summary>- Contact Us</summary>
<img src="documentation/html-validations/html_validator_contact.png" >
</details>

<details><summary>- Edit</summary>
<img src="documentation/html-validations/html_validator_edit.png" >
</details>

<details><summary>- Home</summary>
<img src="documentation/html-validations/html_validator_home.png" >
</details>

<details><summary>- Login</summary>
<img src="documentation/html-validations/html_validator_login.png" >
</details>

<details><summary>- Logout</summary>
<img src="documentation/html-validations/html_validator_logout.png" >
</details>

<details><summary>- Recipes</summary>
<img src="documentation/html-validations/html_validator_recipes.png" >
</details>

<details><summary>- Recipes detail</summary>
<img src="documentation/html-validations/html_validator_recipes_detail.png" >
</details>

<details><summary>- Register</summary>
<img src="documentation/html-validations/html_validator_register.png" >
</details>

#### CSS files pass through the Jigsaw validator with no issues found.
<details><summary>- CSS</summary>
<img src="documentation/css-validator/css_validator.png" >
</details>

#### Python files have been through the validator and have no issues.
<details><summary>- contact_admin</summary>
<img src="documentation/python-validator/contact_admin.png" >
</details>
<details><summary>- contact_admin</summary>
<img src="documentation/python-validator/contact_apps.png" >
</details>
<details><summary>- contact_forms</summary>
<img src="documentation/python-validator/contact_forms.png" >
</details>
<details><summary>- contact_models</summary>
<img src="documentation/python-validator/contact_models.png" >
</details>
<details><summary>- contact_urls</summary>
<img src="documentation/python-validator/contact_urls.png" >
</details>
<details><summary>- contact_views</summary>
<img src="documentation/python-validator/contact_views.png" >
</details>
<details><summary>- home_apps</summary>
<img src="documentation/python-validator/home_apps.png" >
</details>
<details><summary>- home_urls</summary>
<img src="documentation/python-validator/home_urls.png" >
</details>
<details><summary>- home_views</summary>
<img src="documentation/python-validator/home_views.png" >
</details>
<details><summary>- nonalco4me_urls</summary>
<img src="documentation/python-validator/nonalco4me_urls.png" >
</details>
<details><summary>- nonalco4me_wsg</summary>
<img src="documentation/python-validator/nonalco4me_wsgi.png" >
</details>
<details><summary>- nonalco4me_wsgi</summary>
<img src="documentation/python-validator/recipes_admin.png" >
</details>
<details><summary>- recipes_forms</summary>
<img src="documentation/python-validator/recipes_forms.png" >
</details>
<details><summary>- recipes_models</summary>
<img src="documentation/python-validator/recipes_models.png" >
</details>
<details><summary>- recipes_urls</summary>
<img src="documentation/python-validator/recipes_urls.png" >
</details>
<details><summary>- recipes_views</summary>
<img src="documentation/python-validator/recipes_views.png" >
</details>

#### Javascript file have been through the validator and it takes no arguments.
The function works without problems and I see that I have undefined variable and unused variables. I tried to fix a google maps from Code institute lessons. But did not go through JsHint. So the code I have now is from Google's own tutorial. Tried to fix the code so I didn't need what is circled in the picture, but unfortunately didn't succeed.
<details><summary>- maps.js</summary>
<img src="documentation/javascript-validator/jshint.png" >
</details>

## Defensive Validation

<details><summary>- When I am not logged in and try to access a page in logged in mode.</summary>
<img src="documentation/testing/login_Page.png" >
</details>

If a non-logged-in guest tries to access the add recipes, edit page, delete page, and contact page, they are prompted to log in. If at login they are identified as a logged in user, they are taken to the pages. Otherwise they are taken to the page screenshot above.

## Accessibility

<details><summary>- Lighthouse</summary>
<img src="documentation/lighthouse/lighthouse.png" >
</details>

## Fixed bugs
- When I was clicking on a recipe to see details, I got an error that my recipes_detail.html does not exist. 
- - <details><summary>I was missing the L in HTML.</summary>
    <img src="documentation/bugs/missing_html.png" >
    </details>
<br>

- I was trying to fix my comments. But when I was running a makemigration, I got (You are trying to add a non-nullable field 'email') I got different all the time. I also tried received 'name'. I couldn't have fixed it without Joshua's help on tutor support. Because I needed to restore my database.

- I had a url path that didn't work when I pressed the add recipes button. So I got an error message. But it turned out that I had placed my url paths in the wrong order.
- - <details><summary>- The button that didn't work.</summary>
    <img src="documentation/bugs/the_button.png" >
    </details>
- - <details><summary>- Url path when it didn't work.</summary>
    <img src="documentation/bugs/my_url.png" >
    </details>
- - <details><summary>- The Url path after, then the button worked.</summary>
    <img src="documentation/bugs/tutor_urls.png" >
    </details>
<br>

- In my recipe detail, I wanted an edit and delete buttons. But I never got the buttons to appear. But that was because I had creator in my html file and author in my models.py.
- - <details><summary>- The button that didn't work.</summary>
    <img src="documentation/bugs/edit_button.png" >
    </details>
- - <details><summary>- Url path when it didn't work.</summary>
    <img src="documentation/bugs/edit_button_creator.png" >
    </details>
<br>

- I didn't get my google maps to show up after I deployed to heroku. But my very kind classmate Starhigh helped me solve the problem. I would just add the secret key as a variable in configvars.

## Technologies Used
### Main Languages Used
- HTML5
- CSS3
- Python
- Javascript
- Django
- SQL - Postgres

### Frameworks, Libraries & Programs Used
- Google Fonts - for the font families:
- Font Awesome - to add icons to the social links in the footer element.
- GitHub - to store my repository for submission.
- Balsamiq - were used to create mockups of the project prior to starting.
- Am I Responsive? - to ensure the project looked good across all devices.
- Favicon - to provide the code & image for the icon in the tab bar.
- Django
- Bootstrap

### Modules used for the development of this project:
<details><summary>- Requirements.</summary>
    <img src="documentation/images/requirements.png" >
    </details>

## Deployment

### Creating Database using ElephantSQL

1. To generate a managed PostgreSQL database, please proceed to [ElephantSQL](https://customer.elephantsql.com/) and either sign up or sign in to your account. Once you've logged in, click on the 'Create New Instance' button.
- - <details><summary>See Image</summary>
    <img src="documentation/deployment/elephantSQL.png" >
    </details>

2. Name your database and select the 'Tiny Turtle' payment plan. Then, click on 'Select Region'

3. Select your preferred region and create the database instance.

4.  After creating the instance, navigate to the instances page and click on the name of the database you selected earlier. Then, in the details section on the following page, copy the PostgreSQL URL.

- - <details><summary>See Image</summary>
    <img src="documentation/deployment/elephantSQL_url.png" >
    </details>

### Deploying the website in Heroko

#### Before deploying in Heroku following files were created:

1. env.py : stores confidential data eg. API keys, passwords etc.
- - <details><summary>See Image</summary>
    <img src="documentation/deployment/env.py.png" >
    </details>

2. Procfile : Very important for deployment and must be added with capital P
- - <details><summary>See Image</summary>
    <img src="documentation/deployment/procfile.png" >
    </details>

3. Requirements.txt: This must be updated for deployment in Heroku. It stores data of libraries used for project
- - <details><summary>See Image</summary>
    <img src="documentation/deployment/requirements.png" >
    </details>

- The website was deployed to Heroko using following steps:

#### Login or create an account at Heroku

- Make an account in Heroko and login

#### Creating an app

- Create new app in the top right of the screen and add an app name.
- Select region
- Then click "create app".

<details>
<summary>Create App</summary>
<img src="documentation/deployment/app_name.png" alt="Heroko create app screenshot">
</details>

#### Open settings Tab

##### Click on config var

- Store CLOUDINARY_URL file from in key and add the values
- Store DATABASE_URL file from in key and add the values
- Store SECRET_KEY file from in key and add the values
- Store PORT in key and value

NOTE: For initial deployment DISABLE_COLLECTSTATIC was also added

<details>
<summary>Config var</summary>
<img src="documentation/deployment/configvars.png" alt="Config var screenshot">
</details>

##### Add Buildpacks

- Add python buildpack

<details>
<summary>Buildpacks</summary>
<img src="documentation/deployment/buildpacks.png" alt="Buildpacks screenshot">
</details>

#### Open Deploy Tab

##### Choose deployment method and Connect to Github

- Connect GITHUB
- Login if prompted
- Choose repositories you want to connect
- Click "Connect"

<details>
<summary>Deployment method</summary>
<img src="documentation/deployment/github_connect.png" alt="Github connect">
</details>

##### Automatic and Manual deploy

- Choose a method to deploy
- After Deploy is clicked it will install various file

<details>
<summary> Deploy methods</summary>
<img src="documentation/deployment/deploy.png" alt="deploy method screenshot">
</details>

##### Final Deployment

- A view button will display
- Once clicked the website will open

<details>
    <summary> Deploy</summary>
    <img src="documentation/deployment/deployment_view.png" alt="view screenshot">
</details>

The live link for "NonAlco4Me" can be found [HERE](https://non-alco-4me-427be0bd27b2.herokuapp.com/)

## Credits

### Content
- I have received very good help from Think Therefore I Blog from code institute which got me started on my project.
- Checked out [Django Blog Webinar](https://youtu.be/YH--VobIA8c) which helped me understand more about edit and delete buttons.
- Big shoutout to my classmate [Starhigh](https://github.com/gStarhigh) who sat for 4 hours trying to help me get my commenting feature up and running. Unfortunately I needed to restore my database. Which we didn't think of.
- A thank you to Joshua from tutor support who helped me reset my database. When I couldn't makemigrate.
- Code Institute (especially the Django blog) which helped me to understand how it all comes together.
- Rebecca from tutor support helped me to understand my urls path and why it didn't worked.
- Thanks to my mentor Martina for taking the time and giving me good inputs about my project. And sent very good suggestions for different repos that I could get inspiration from.
- I struggled a lot with my google maps, but couldn't get it to work the way I wanted. So I searched on google and found a great youtube video that helped me. [How to add a map to your website with JavaScript](https://www.youtube.com/watch?v=B4p3A00uXAs&t=53s)
- Have looked at [The paper lounge](https://github.com/cornishcoder1/the_paper_lounge) functions and received a lot of inspiration and a lot of understanding of how everything is connected.
- I had a hard time getting started with my readme. So I've looked at three fantastic readme's that I've copied a bit from.
- - [Humanitas](https://github.com/Sinha5714/humanitas_django_pp4/blob/main/README.md)
- - [Hillbox](https://github.com/736B796E6574/CI-PP4/blob/main/README.md)
- - [The paper lounge](https://github.com/cornishcoder1/the_paper_lounge/blob/main/README.md)

## Images

- The images on the homepage including recipes images are taken from [pexels.com](https://www.pexels.com/)