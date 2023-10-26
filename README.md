# Snowpatrol


![Am I Responsive image]()

Snowpatrol is a fictional B2C e-commerce store that is designed and implemented with Python and Django, HTML, CSS and some Javascript. 
 However it has to be noted that this site is for educational use only

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


### Product page


### Product detail


### Review


### Bloglist


### Blogpost


### Wishlist


### Shopping Bag


### Checkout


### Checkout success


### My profile


### Footer


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
<details><summary>- Bag Total</summary>
<img src="" >
</details>

<details><summary>- Bag</summary>
<img src="" >
</details>

<details><summary>- Checkout Buttons</summary>
<img src="" >
</details>

<details><summary>- Product image</summary>
<img src="" >
</details>

<details><summary>- Product info</summary>
<img src="" >
</details>

<details><summary>- Quantity form</summary>
<img src="" >
</details>

<details><summary>- Blogpost detail</summary>
<img src="" >
</details>

<details><summary>- Blogpost</summary>
<img src="" >
</details>

<details><summary>- Checkout Success</summary>
<img src="" >
</details>

<details><summary>- Checkout</summary>
<img src="" >
</details>

<details><summary>- Index</summary>
<img src="" >
</details>

<details><summary>- Add product</summary>
<img src="" >
</details>

<details><summary>- Edit product</summary>
<img src="" >
</details>

<details><summary>- Product detail</summary>
<img src="" >
</details>

<details><summary>- Products</summary>
<img src="" >
</details>

<details><summary>- Profile</summary>
<img src="" >
</details>

<details><summary>- Base</summary>
<img src="" >
</details>

<details><summary>- Footer</summary>
<img src="" >
</details>

<details><summary>- Main nav</summary>
<img src="" >
</details>

<details><summary>- Mobile top header</summary>
<img src="" >
</details>

#### CSS files pass through the Jigsaw validator with no issues found.
<details><summary>- base.css</summary>
<img src="" >
</details>

<details><summary>- blog.css</summary>
<img src="" >
</details>

<details><summary>- checkout.css</summary>
<img src="" >
</details>

<details><summary>- home.css</summary>
<img src="" >
</details>

<details><summary>- profile.css</summary>
<img src="" >
</details>


#### Python files have been through the validator and have no issues.
<details><summary>- Bag context.py</summary>
<img src="" >
</details>
<details><summary>- Bag views.py</summary>
<img src="" >
</details>
<details><summary>- Blog admin.py</summary>
<img src="" >
</details>
<details><summary>- Blog forms.py</summary>
<img src="" >
</details>
<details><summary>- Blog models.py</summary>
<img src="" >
</details>
<details><summary>- Blog urls.py</summary>
<img src="" >
</details>
<details><summary>- Blog views.py</summary>
<img src="" >
</details>
<details><summary>- Blog .py</summary>
<img src="" >
</details>
<details><summary>- checkout admin.py</summary>
<img src="" >
</details>
<details><summary>- checkout forms.py</summary>
<img src="" >
</details>
<details><summary>- checkout models.py</summary>
<img src="" >
</details>
<details><summary>- checkout signals.py</summary>
<img src="" >
</details>
<details><summary>- checkout urls.py</summary>
<img src="" >
</details>
<details><summary>- checkout views.py</summary>
<img src="" >
</details>
<details><summary>- checkout webhook_handler.py</summary>
<img src="" >
</details>
<details><summary>- checkout webhooks.py</summary>
<img src="" >
</details>
<details><summary>- home urls.py</summary>
<img src="" >
</details>
<details><summary>- home views.py</summary>
<img src="" >
</details>
<details><summary>- products admin.py</summary>
<img src="" >
</details>
<details><summary>- products forms.py</summary>
<img src="" >
</details>
<details><summary>- products models.py</summary>
<img src="" >
</details>
<details><summary>- products urls.py</summary>
<img src="" >
</details>
<details><summary>- products views.py</summary>
<img src="" >
</details>
<details><summary>- products widgets.py</summary>
<img src="" >
</details>
<details><summary>- profiles forms.py</summary>
<img src="" >
</details>
<details><summary>- profiles models.py</summary>
<img src="" >
</details>
<details><summary>- profiles urls.py</summary>
<img src="" >
</details>
<details><summary>- profiles views.py</summary>
<img src="" >
</details>
<details><summary>- wishlist admin.py</summary>
<img src="" >
</details>
<details><summary>- wishlist models.py</summary>
<img src="" >
</details>
<details><summary>- wishlist urls.py</summary>
<img src="" >
</details>
<details><summary>- wishlist views.py</summary>
<img src="" >
</details>

#### Javascript file have been through the validator and it takes no arguments.
The function works without problems and I see that I have undefined variable and unused variables. I tried to fix a google maps from Code institute lessons. But did not go through JsHint. So the code I have now is from Google's own tutorial. Tried to fix the code so I didn't need what is circled in the picture, but unfortunately didn't succeed.
<details><summary>- checkout stripe_elements.js</summary>
<img src="" >
</details>
<details><summary>- profiles countryfield.js</summary>
<img src="" >
</details>

## Defensive Validation

<details><summary>- When I am not logged in and try to access a page in logged in mode.</summary>
<img src="" >
</details>

If a non-logged-in guest tries to access the add recipes, edit page, delete page, and contact page, they are prompted to log in. If at login they are identified as a logged in user, they are taken to the pages. Otherwise they are taken to the page screenshot above.

## Accessibility

## Lighthouse

For the performance, accessibility, best practices, and SEO of the site for mobile and desktop I used the Chrome Lighthouse tool:

#### Desktop Results


<details><summary>- Index Page</summary>
<img src="" >
</details>
<details><summary>- Shopping Bag</summary>
<img src="" >
</details>
<details><summary>- Products</summary>
<img src="" >
</details>
<details><summary>- Product detail</summary>
<img src="" >
</details>
<details><summary>- Blogpost</summary>
<img src="" >
</details>
<details><summary>- Blogpost detail</summary>
<img src="" >
</details>
<details><summary>- Checkout</summary>
<img src="" >
</details>
<details><summary>- Checkout Success</summary>
<img src="" >
</details>
<details><summary>- Add product</summary>
<img src="" >
</details>
<details><summary>- Profile</summary>
<img src="" >
</details>
<details><summary>- Wishlist</summary>
<img src="" >
</details>


- Desktop performed well on all major pages of the site.
- The 83-point score for Best Practices is due to the scripts beyond my control (e.g. Mailchimp)

#### Mobile Results

<details><summary>- Index Page</summary>
<img src="" >
</details>
<details><summary>- Shopping Bag</summary>
<img src="" >
</details>
<details><summary>- Products</summary>
<img src="" >
</details>
<details><summary>- Product detail</summary>
<img src="" >
</details>
<details><summary>- Blogpost</summary>
<img src="" >
</details>
<details><summary>- Blogpost detail</summary>
<img src="" >
</details>
<details><summary>- Checkout</summary>
<img src="" >
</details>
<details><summary>- Checkout Success</summary>
<img src="" >
</details>
<details><summary>- Add product</summary>
<img src="" >
</details>
<details><summary>- Profile</summary>
<img src="" >
</details>
<details><summary>- Wishlist</summary>
<img src="" >
</details>


- Mobile performed well on all major pages of the site.
- The 83-point score for Best Practices is due to the scripts beyond my control (e.g. Mailchimp)


## Fixed bugs

#### Bug 1
- 
- - <details><summary>I was missing the L in HTML.</summary>
    <img src="" >
    </details>
<br>

#### Bug 2

- 
- 
- - <details><summary>- </summary>
    <img src="" >
    </details>
- - <details><summary>- </summary>
    <img src="" >
    </details>
- - <details><summary>- </summary>
    <img src="" >
    </details>
<br>

#### Bug 3

- 
- - <details><summary>- </summary>
    <img src="" >
    </details>
- - <details><summary>- </summary>
    <img src="" >
    </details>
<br>


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
    <img src="" >
    </details>

## Deployment

### Creating Database using ElephantSQL

1. To generate a managed PostgreSQL database, please proceed to [ElephantSQL](https://customer.elephantsql.com/) and either sign up or sign in to your account. Once you've logged in, click on the 'Create New Instance' button.
- - <details><summary>See Image</summary>
    <img src="" >
    </details>

2. Name your database and select the 'Tiny Turtle' payment plan. Then, click on 'Select Region'

3. Select your preferred region and create the database instance.

4.  After creating the instance, navigate to the instances page and click on the name of the database you selected earlier. Then, in the details section on the following page, copy the PostgreSQL URL.

- - <details><summary>See Image</summary>
    <img src="" >
    </details>

### Deploying the website in Heroko

#### Before deploying in Heroku following files were created:

1. env.py : stores confidential data eg. API keys, passwords etc.
- - <details><summary>See Image</summary>
    <img src="" >
    </details>

2. Procfile : Very important for deployment and must be added with capital P
- - <details><summary>See Image</summary>
    <img src="" >
    </details>

3. Requirements.txt: This must be updated for deployment in Heroku. It stores data of libraries used for project
- - <details><summary>See Image</summary>
    <img src="" >
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


## Images

- The images on the homepage including recipes images are taken from [pexels.com](https://www.pexels.com/)
