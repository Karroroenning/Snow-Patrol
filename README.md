# Snowpatrol


![Am I Responsive image](documentation/am_I_responsive.png)


Please view the live website here: [Snowpatrol](https://snowpatrol-6b2d334410bf.herokuapp.com/ "Snowpatrole Homepage").
<br>
My Repository can you see here: [Repository](https://github.com/Karroroenning/Snow-Patrol "Repository").

## Table of contents
+ [Business modal](#business-modal)
  + [Business overview](#business-overview)
+ [SEO](#seo)
  + [SEO Project planning](#seo-project-planning)
  + [Keywords](#keywords)
+ [UX](#ux)
  + [Site Purpose](#site-purpose)
  + [Site Goal](#site-goal)
* [User Stories](#user-stories)
  * [Site User](#as-a-site-user)
  * [Logged in Site User](#as-a-login-user)
  * [Admin](#as-a-admin)
* [Agile Methodology](#agile-methodology)
* [Design](#design)
  * [Wireframes](#wireframes)
  * [Color Scheme](#color-scheme)
  * [Imagery](#imagery)
* [Database diagram](#database-diagram)
* [Features](#features)
* [Future features](#future-features)
* [C.R.U.D.](#crud)
  * [Products](#products)
  * [Reviews](#reviews)
  * [Blog](#blog)
  * [Delete](#delete)
* [Testing](#testing)
  * [Manual Testing](#manual-testing)
  * [Browsers](#browsers)
  * [Validator Testing](#validator-testing)
  * [Defensive Validation](#defensive-validation)
* [Accessibility](#accessibility)
  * [Lighthouse](#lighthouse)
* [Fixed bugs](#fixed-bugs)
* [Technologies Used](#technologies-used)
* [Deployment](#deployment)
* [Credits](#credits)

## Business modal
Snowpatrol is a fictional B2C e-commerce store that is designed and implemented with Python and Django, HTML, CSS and some Javascript. 
However it has to be noted that this site is for educational use only.

### Business overview

#### Which page will the user first see when they visit the page.
- It will be the Home page

#### The first page will include
- The contents will be clear for the users. Simple to see what the site includes. Snowboarding is a winter sport that can be calm and cozy or more speed and wind. The majority of users who decide to snowboard are looking for more speed and adrenaline. Then we will try to emphasize that desire on our website. 
- The age groups for snowboarding in particular are variable from young children up to middle age. So our content should focus mostly on middle age and a little below.
- Our goal is to bring out action, so we will have a hero image that will show a lovely mix between nature and a bit of freestyle. So you get a better feel for what it's like to snowboard.

# SEO

## SEO Project planning

Once the business model was decided as a snowboard shop, I started working on how to market the site and what keywords to target.

I started searching on google and checked how many search results I got on each search and which keywords were most attractive.

## Keywords

### Snowboard
#### Short keyword

- Snowboard
- Snow
- Snowsports
- Mountain sports
- Snow nature
- Universal Snowboard
- Snowboarding gear

#### Long keyword

- Want to buy a snowboard in the right size
- What should I pack first time snowboarding

### Snowboard boots
#### Short keyword

- Snowshoes
- Snowboard shoes
- Warm snowshoes

#### Long keyword

- Most comfortable snowboard boots
- Good quality snowboard boots that last for off-piste

### Snowboard bindings
#### Short keyword

- Bindings
- Step in Bindings

#### Long keyword
- Buy snowboard bindings in sweden
- Easiest snowboard bindings to get in and out of 

### Sport gifts
#### Short keyword
- Snow adventure
- Snowboarding near me
- Snowboard store

#### Long keyword
- What to buy to someone who likes snowboarding


### Sitemap.xml
I generated a sitemap for the site so that once ready engines like google can search it effectively.

### Robots.txt
I generated a robots.txt file so that google could crawl the site. I have blocked off the accounts app as there is no benefit for google to crawl those pages.

### Logo
The logo of the site was made with an online app from LOGO(logo.com)

### Facebook Business Page

To view the facebook business page you can click on the link below:

[Facebook Business Page](https://www.facebook.com/profile.php?id=61552855474003)

In case the page becomes inactive or deactivated by Facebook I have taken screenshots to display here also:

<details><summary>Facebook page</summary>
<img src="documentation/facebook_page/facebook_1.png" >
<img src="documentation/facebook_page/facebook_2.png" >
<img src="documentation/facebook_page/facebook_3.png" >
</details>


# UX
### Site Purpose
The purpose of the website is to be able to give users an opportunity to explore what is available to use within the world of snowboarding. Whether you are a beginner or a professional, there is always an option that suits them. Even when you have bought what you need, there is always a reason to visit the website again, because there is a blog that the admin updates a few times a week to update users about all the upcoming news, various tips on good slopes and even tips on how to think about how to wax the board for next season.

### Site Goal
- An easy to navigate website with clear purpose.
- Provide users with products that meet their expectations.
- To provide tools that allow users to search for products.
- Allow users to view and read about the products that may help or interest them.
- Allow users to give their review on any product.
- Allow users to add products to a wishlist of theirs.
- To give users news or tips about what's happening in snowboarding.
- Allow users to checkout quickly and easily.
- To allow users to create a profile to view past orders and update profile information.


## User Stories


### As a site user: 

- Navigate around the site in a smooth and simple way. (must do)
- See a list of products and can choose the product you want. (must do)
- Search products to find a specific product. (must do)
- Click on a product to read and view the details. (must do)
- Register for an account to avail of the services offered to members. (must do)
- View product reviews so that I can read other users opinions. (Could do)
- Buy a product by using the website checkout system. (must do)
- I can sort products on criteria such as price and category so that I can have a method of ordering the products as I prefer. (Could do)
- I can view the contents of my shopping basket so that I can be able to make any adjustments. (must do)
- Sign up to newsletter so that I can keep updated on the latest news. (must do)
- User Signup Email Confirmation. (must do)
- Cart is displayed on the top right navigation panel, so that users can avoid spending too much. (must do)
- Read about the latest news. (Could do)

### As a login user:

- Delete my previous review. (Could do)
- Leave a review about a product. (Could do)
- Edit my previous reviews. (Could do)
- Save my data under my personal profile. (must do)
- I can view my order history. (must do)
- Manage my profile by updating my details. (must do)
- Logout of the website. (must do)
- Add products to my wish list (Could do)

### As a Admin:

- Create and publish a new product. (must do)
- Create a draft of a new product so it can be finalised later. (Could do)
- Create a new user, products, and categories. (must do)
- Delete user, products, categories and reviews. (must do)
- Approve user's reviews. (Could do)
- Create and publish a new blogpost from adminpanel. (Could do)


## Agile Methodology

The development of this project was managed and implemented using GitHub Projects Kanban Board. Available here:
<a href="https://github.com/users/Karroroenning/projects/7" target="_blank" rel="noopener" aria-label="Link to GitHub Projects">Snowpatrol - User Stories</a>

<br>

## Design
### Wireframes

- A low-fi wireframe was build before developing the website.
- This was done in Balsamiq Wireframes. 

<details><summary>Home Page</summary>
<img src="documentation/wireframes/index.png" >
</details>

<details><summary>Product Page</summary>
<img src="documentation/wireframes/products.png" >
</details>

<details><summary>Product Detail</summary>
<img src="documentation/wireframes/products_detail.png" >
</details>

<details><summary>Blog list</summary>
<img src="documentation/wireframes/blogpost.png" >
</details>

<details><summary>Blogpost</summary>
<img src="documentation/wireframes/blog_detail.png" >
</details>

<details><summary>Checkout</summary>
<img src="documentation/wireframes/checkout.png" >
</details>

<details><summary>Checkout success</summary>
<img src="documentation/wireframes/checkout_success.png" >
</details>

<details><summary>Product Management</summary>
<img src="documentation/wireframes/product_management.png" >
</details>

<details><summary>Profile</summary>
<img src="documentation/wireframes/profile.png" >
</details>

<details><summary>Shopping bag</summary>
<img src="documentation/wireframes/shopping_bag.png" >
</details>

<details><summary>Wishlist</summary>
<img src="documentation/wireframes/wishlist.png" >
</details>

<details><summary>Signup</summary>
<img src="documentation/wireframes/signup.png" >
</details>

<details><summary>Login</summary>
<img src="documentation/wireframes/login.png" >
</details>

<details><summary>Logout</summary>
<img src="documentation/wireframes/logout.png" >
</details>


### Color Scheme
<details><summary>Color Scheme</summary>
<img src="documentation/snowpatrol.png" >
</details>

I have kept the colors very simple. Black and white. Because there are already a lot of other colors from all the product images and blog post images. The fact that the basic colors are black and white means that the focus is more on the products. This is an e-commerce website and our goal is for the focus to fall on our goal, the products!

### Imagery:

- On the first page, I have a picture that I think is a good picture for a first impression that snowboarding is more than just going down a slope. It can also be sporty and peaceful in a beautiful nature.

<details><summary>Hero Image</summary>
<img src="media/pexels-jeffrey-brandjes-6835492.jpg" >
</details>

<br>


- Up in the left corner, we have our own designed logo. The logo should resemble a mountain and a bar-code. The mountain should symbolize slope and the bar-code is that it is an e-commerce website.
<details><summary>Logo</summary>
<img src="media/snowpatrol-low-resolution-logo-black-on-white-background.png" >
</details>

<br>
- All other images are of the products and blog post images that the admin can add from the admin panel.

## Database diagram
<details><summary>Database diagram</summary>
<img src="documentation/ERD.png" >
</details>
<br>

# Features

### Navbar and Footer
- A navbar with nav-items to navigate to various pages in the website.
- The logo at the top left which also takes us to the first page.
- The search box where you can search for a product you are looking for.
- My account button that takes one to their profile page, wishlist and log out.
- On the right we have our shopping cart so you can clearly see how much you spend.
- Footer with social media, adress, contact and subscribe.
<details><summary>Navbar</summary>
<img src="documentation/features/Navbar_footer/Navbar.png">
</details>
<details><summary>Footer</summary>
<img src="documentation/features/Navbar_footer/footer.png">
</details>

### Homepage
- We have the hero image with a short text about our blog and a button that will take us to the blogposts.
<details><summary>Hero Image</summary>
<img src="documentation/features/Home/hero_img_blog.png">
</details>

### Bloglist
- Blogposts lined up. 3 posts per row. 9 posts per side.
- Below the blog post images we have a title for the blog post and the date it was created.
- You can click on either the image or the title to get to the blog post page.
<details><summary>Bloglist</summary>
<img src="documentation/features/blog/bloglist.png">
</details>

### Blogpost
- Under the navbar, we have the title of the blogpost and when it was created. 
- Picture of the blogpost is to the right of the text.
- To the left of the picture we have the content about the blog post.
<details><summary>Blogpost</summary>
<img src="documentation/features/blog/blogpost.png">
</details>

### Product page
- Under the product heading we have links for the product categories. 
- On the right we have a dropdown menu to be able to sort the products.
- Products lined up. 4 posts per row.
- Below the image we have the name of the product, the price, the category and what rating it has. If Admin is logged in, there are also two links with Edit and Delete. 
- You can click on the image to get to the Product detail page.
- Down in the right corner we have a button that takes us back to the top of the page.
<details><summary>Product page</summary>
<img src="documentation/features/products/products.png">
</details>

### Product detail
- On the right we have the product image. When you press it, the image opens in a separate tab.
- On the left we have the product's name, price, category and rating. If Admin is logged in, there are also two links with Edit and Delete. 
- Underneath we have the product description, a dropdown menu so you can choose the size of the product, choose the quantity of how many you want. Then we have three buttons, one that takes us back to the product page and one to add the product to the bag. If you are logged in, you also have a button so you can add the product to your wishlist.
- At the bottom of the page we have a review section. Logged in users can leave a review about the product, update and delete their own review. If you are not logged in, you can only read reviews.
<details><summary>Product detail</summary>
<img src="documentation/features/products/product_detail.png">
</details>
<details><summary>Reviews</summary>
<img src="documentation/features/products/Reviews.png">
</details>

### Wishlist
- The wishlist is only availabe for logged in users. A logged in user can add or delete a product to this list.
- You can click on the product name to get to the product detail page.
<details><summary>Wishlist</summary>
<img src="documentation/features/wishlist/wishlist.png">
</details>

### Shopping Bag
- Products that you have added to your shopping bag end up here. 
- The picture of the product is on the left together with the product name and which size you have chosen. 
- On the right, we have how much the price is for a product, followed by how many products have been selected and the total amount for the product. 
- You can update the quantity of products or remove your product from your shopping bag by changing the number and pressing update or if you want to remove the product press the remove button.
- At the bottom of the page we have the total amount, shipping cost and grand total.
- We have two buttons below, one that takes us back to the product page and the other goes to our checkout page.
<details><summary>Shopping bag</summary>
<img src="documentation/features/shopping_bag/shopping_bag.png">
</details>
<details><summary>Shopping bag grand total</summary>
<img src="documentation/features/shopping_bag/shopping_bag_total.png">
</details>

### Checkout
- On the left side you enter your personal information including delivery information. If you are a logged in user, you can check a check box that you want to save your info to your profile page.
- On the right side we have our order summary and the total grand total.
- At the bottom of the page under delivery info, you enter your card details and if they are correct you can press the complete order button. If you want to change your shopping bag, press the adjust bag button to return to the checkout page.
<details><summary>Checkout</summary>
<img src="documentation/features/checkout/checkout.png">
</details>

### Checkout success
- On this page we have our order information.
- We also have a button that takes us to the blog page.
- After paying, the user also receives a confirmation email.
<details><summary>Checkout success</summary>
<img src="documentation/features/checkout/checkout_success.png">
</details>
<details><summary>Confirmation Email</summary>
<img src="documentation/features/checkout/email.png">
</details>

### My profile
- You have your own profile page if you are logged in.
- On the left side we have the user's delivery information which can be updated by pressing the button update information.
- On the right side we have the user's order history. The order number, date the order was placed, items and order total are displayed there.
- If you want to get more information about the order, you can click on the order number, which is a link to the order information.
<details><summary>Profile</summary>
<img src="documentation/features/profile/profile.png">
</details>
<details><summary>Order info</summary>
<img src="documentation/features/profile/order_info.png">
</details>

### Product Management
- If you are admin over the page, you can add new products for sale by going to product management.
- There you enter all the information that the admin wants to give the product.
- At the bottom, you can add a product image
- You have two buttons you can press, cancel or add product
<details><summary>Product management</summary>
<img src="documentation/features/product_management/product_management.png">
</details>


### Login
- Enter your username and password and then press the login button to log in to the website.
- Press the logout button and the user is logged out.
<details><summary>Login</summary>
<img src="documentation/features/Login_logout_signup/login.png">
</details>


### Logout
- Press the logout button and the user is logged out.
<details><summary>Logout</summary>
<img src="documentation/features/Login_logout_signup/logout.png">
</details>


### Sign-up
- Write in all fields to register.
- Press the signup button.
- A confirmation email is sent to your email address.
- You will receive an email with a link that you must click to verify your email address.
- You come to the website to confirm email.
- If you already have a login, you can press the link below to get to the login page.
<details><summary>Signup</summary>
<img src="documentation/features/Login_logout_signup/signup.png">
</details>
<details><summary>Verify email</summary>
<img src="documentation/features/Login_logout_signup/verify_email.png">
</details>
<details><summary>Email</summary>
<img src="documentation/features/Login_logout_signup/verify_email_mail.png">
</details>
<details><summary>Confirm email</summary>
<img src="documentation/features/Login_logout_signup/confirm_email.png">
</details>


## Future features

- Like the blogpost.
- Authenticated superuser can create a blog post without entering via the admin panel.
- See pictures of the product in the wishlist.

# CRUD

### Products
Products are what is the main focus of the e-commerce website. Admins can add, edit, and delete a product, add related image, and descriptions.

#### CRUD
- **Create:** If the user is an authenticated superuser, they can add a new product by clicking the my account icon in the top right corner and click on Product Management.
- **Read:** All users can view all the product and read about them in the product navbar.
- **Update:** Only admins can edit the products.
- **Delete:** Only admins can delete the products.

### Reviews
Registered users can leave a review about every product. 

#### CRUD
- **Create:** If the user is logged in, they can go to the product and leave a review about it.
- **Read:** All users, even those who are not logged in, can read all reviews written about the product.
- **Update:** Only the author of the review can edit the review via frontend.
- **Delete:** Only the author of the review can delete the review via frontend.

### Blog
Administrators (superusers) can add blog posts to the blog section by entering via the admin panel and creating a blog post. The reason for this is to give users the feeling that we are a whole family that likes the same things, snowboarding and to give insperation

#### CRUD
- **Create:** Admins can add new blog posts to the blog page.
- **Read:** All users can read the current blog posts listed in the blog section.
- **Update:** Admins can edit the existing blog posts via the admin panel.
- **Delete:** Admins can delete existing blog posts via the admin panel.

# Testing
## Manual Testing

#### Manual Testing

> If the intended outcome completes then this will be flagged as pass. If it does not then this is a fail.


<details>
<summary>Account Registration Tests </summary>
<br>

| Test |Result  |
|--|--|
|User can create an account | Pass |
|Verified User can log into account| Pass|
|User can log out of account|Pass|
|User is notified of logging in to account|Pass|
|User is notified of logging out of account|Pass|
|User receives email verification email|Pass|

</details>

---


<details>
<summary>Account Login Tests </summary>
<br>

| Test |Result  |
|--|--|
|Verified User can log into account| Pass|
|Non verified User is notified The username and/or password are not correct.|Pass|
|User can log out of account|Pass|
|User is notified of logging in to account|Pass|
|User is notified of logging out of account|Pass|


</details>

---

<details>
<summary>User Navigation Tests</summary>
<br>

| Test |Result  |
|--|--|
|User can navigate to product| Pass |
|User can access product details| Pass|
|User can add a product to cart|Pass|
|User can navigate back to products|Pass|
|User can add additional products to cart|Pass|
|User can add multiple quantities of a product |Pass|
|User can navigate to cart|Pass|
|Logged in User can navigate to the profile section of accounts|Pass|
|User can access their saved address information|Pass|
|User can access past orders|Pass|
|User can access the blog section of the page|Pass|
|User can access specific blogs|Pass|
|User can access the review section|pass|
|Logged in User can review any product|pass|
|Logged in User can edit or delete their reviews|pass|
|Logged in User can add to his/her wishlist|pass|
|All links on footer open to correct pages|Pass|
|All links on Heading Navigation open to correct option|Pass|
|User can use the search box|Pass|
|User entering a no results search returns error message|Pass|

</details>

---

<details>
<summary>Account Security Tests</summary>
<br>

| Test |Result  |
|--|--|
|Not logged in User cannot make review | Pass |
|Not logged in User cannot add products to wishlist|Pass|
|Not logged in User cannot access profile page| Pass|
|Not logged in User cannot access admin panel|Pass|
|Not logged in User cannot access products management|Pass|
|Not logged in user cannot access wishlist page|Pass|
|Logged in User cannot access admin panel|Pass|
|Logged in User cannot access products management|Pass|
|Logged in User cannot edit products|Pass|
|Logged in User can leave reviews about the products|Pass|
|Logged in User can add products to wishlist|Pass|

</details>

--- 

<details>
<summary>Profile Tests</summary>
<br>

| Test |Result|
|--|--|
|Not logged in User cannot access profile page | Pass |
|Logged in User can access profile page|Pass|
|Logged in User can see their details on the accounts home page|Pass|
|Logged in User can update their email|Pass|
|Logged in User can navigate to their shipping information|Pass|
|Logged in User can update street address 1 and 2|Pass|
|Logged in User can update town or city|Pass|
|Logged in User can update county|Pass|
|Logged in User can update postcode|Pass|
|Logged in User can update country|Pass|
|Pop-up modal prompts the user to confirm sign out before signing out|Pass|

</details>

---

<details>
<summary>Admin Tests</summary>
<br>

| Test |Result  |
|--|--|
|Super User can access add product page from my account dropdown|Pass|
|Super User can see the edit product button on the products page|Pass|
|Super User can see the delete button on the products page|Pass|
|Super User can write blogs from the admin panel and publish them|Pass|
|Super User can edit blog detail and update all fields successfully from the admin panel|Pass|
|Super User can delete blog from the from the admin panel|Pass|
|Super User can approve reviews from the admin panel|Pass|

</details>

---

<details>
<summary>Payment Tests</summary>
<br>

| Test |Result  |
|--|--|
|User can successfully make a payment & order| Pass|
|All users receive an email confirmation of order on deployed site|Pass|
|In development email confirmation is printed to terminal|Pass|
|In production email confirmation is sent to user|Pass|
|If payment is successful user will be redirected to order success page|Pass|
|If order fails due to incorrect information being submitted order will not be submitted|Pass|
|If there is an error when processing the order the site returns a 500 error without processing order|Pass|

</details>

---

<details>
<summary>Other Tests</summary>
<br>

| Test |Result  |
|--|--|
|User can Sign up for our newsletter|Pass|
|User can read about Privacy policy|Pass|

</details>

### Browsers
- I checked the site for compatibility on different browsers.
- I have checked the responsiveness on different window sizes.

## Validator Testing
#### HTML files pass through the W3C validator with no issues found.
<details><summary>- HTML</summary>
<img src="documentation/validator/html/w3c.png" >
</details>

#### CSS files pass through the Jigsaw validator with no issues found.
<details><summary>- CSS</summary>
<img src="documentation/validator/css/css_validator.png" >
</details>


#### Python files have been through the validator and have no issues.
<details><summary>- Bag context.py</summary>
<img src="documentation/validator/pep8/bag/contexts.py.png" >
</details>
<details><summary>- Bag urls.py</summary>
<img src="documentation/validator/pep8/bag/urls.py.png" >
</details>
<details><summary>- Bag views.py</summary>
<img src="documentation/validator/pep8/bag/views.py.png" >
</details>
<details><summary>- Blog admin.py</summary>
<img src="documentation/validator/pep8/blog/admin.py.png" >
</details>
<details><summary>- Blog forms.py</summary>
<img src="documentation/validator/pep8/blog/forms.py.png" >
</details>
<details><summary>- Blog models.py</summary>
<img src="documentation/validator/pep8/blog/models.py.png" >
</details>
<details><summary>- Blog urls.py</summary>
<img src="documentation/validator/pep8/blog/urls.py.png" >
</details>
<details><summary>- Blog views.py</summary>
<img src="documentation/validator/pep8/blog/views.py.png" >
</details>
<details><summary>- checkout admin.py</summary>
<img src="documentation/validator/pep8/checkout/admin.py.png" >
</details>
<details><summary>- checkout forms.py</summary>
<img src="documentation/validator/pep8/checkout/forms.py.png" >
</details>
<details><summary>- checkout models.py</summary>
<img src="documentation/validator/pep8/checkout/models.py.png" >
</details>
<details><summary>- checkout signals.py</summary>
<img src="documentation/validator/pep8/checkout/signals.py.png" >
</details>
<details><summary>- checkout urls.py</summary>
<img src="documentation/validator/pep8/checkout/urls.py.png" >
</details>
<details><summary>- checkout views.py</summary>
<img src="documentation/validator/pep8/checkout/views.py.png" >
</details>
<details><summary>- checkout webhook_handler.py</summary>
<img src="documentation/validator/pep8/checkout/webhook_handler.py.png" >
</details>
<details><summary>- checkout webhooks.py</summary>
<img src="documentation/validator/pep8/checkout/webhook.py.png" >
</details>
<details><summary>- home urls.py</summary>
<img src="documentation/validator/pep8/home/urls.py.png" >
</details>
<details><summary>- home views.py</summary>
<img src="documentation/validator/pep8/home/views.py.png" >
</details>
<details><summary>- products admin.py</summary>
<img src="documentation/validator/pep8/products/admin.py.png" >
</details>
<details><summary>- products forms.py</summary>
<img src="documentation/validator/pep8/products/forms.py.png" >
</details>
<details><summary>- products models.py</summary>
<img src="documentation/validator/pep8/products/models.py.png" >
</details>
<details><summary>- products urls.py</summary>
<img src="documentation/validator/pep8/products/urls.py.png" >
</details>
<details><summary>- products views.py</summary>
<img src="documentation/validator/pep8/products/views.py.png" >
</details>
<details><summary>- products widgets.py</summary>
<img src="documentation/validator/pep8/products/widgets.py.png" >
</details>
<details><summary>- profiles forms.py</summary>
<img src="documentation/validator/pep8/profiles/forms.py.png" >
</details>
<details><summary>- profiles models.py</summary>
<img src="documentation/validator/pep8/profiles/models.py.png" >
</details>
<details><summary>- profiles urls.py</summary>
<img src="documentation/validator/pep8/profiles/urls.py.png" >
</details>
<details><summary>- profiles views.py</summary>
<img src="documentation/validator/pep8/profiles/views.py.png" >
</details>
<details><summary>- wishlist models.py</summary>
<img src="documentation/validator/pep8/wishlist/models.py.png" >
</details>
<details><summary>- wishlist urls.py</summary>
<img src="documentation/validator/pep8/wishlist/urls.py.png" >
</details>
<details><summary>- wishlist views.py</summary>
<img src="documentation/validator/pep8/wishlist/views.py.png" >
</details>
<details><summary>- snowpatrol urls.py</summary>
<img src="documentation/validator/pep8/snowpatrol/urls.py.png" >
</details>
<details><summary>- snowpatrol views.py</summary>
<img src="documentation/validator/pep8/snowpatrol/views.py.png" >
</details>

#### Javascript file have been through the validator and it takes no arguments.
The function works without problems.
<details><summary>- checkout_stripe_elements.js</summary>
<img src="documentation/validator/jigsaw/checkout_stripe_elements.png" >
</details>
<details><summary>- profiles_countryfield.js</summary>
<img src="documentation/validator/jigsaw/profile_countryfield.png" >
</details>

## Defensive Validation

<details><summary>- When not logged in user try to access a page in logged in mode.</summary>
<img src="documentation/validator/defensive_validation/no_access_page.png" >
</details>


<details><summary>- When user try to access a page that doesn't exist.</summary>
<img src="documentation/validator/defensive_validation/404.png" >
</details>

<details><summary>- When logged in user try to access a superuser page.</summary>
<img src="documentation/validator/defensive_validation/no_access_page_super_user.png" >
</details>


## Accessibility

## Lighthouse

For the performance, accessibility, best practices, and SEO of the site for desktop I used the Chrome Lighthouse tool:

#### Desktop Results


<details><summary>- Index Page</summary>
<img src="documentation/validator/lighthouse/index.png" >
</details>
<details><summary>- Shopping Bag</summary>
<img src="documentation/validator/lighthouse/shopping_bag.png" >
</details>
<details><summary>- Products</summary>
<img src="documentation/validator/lighthouse/product.png" >
</details>
<details><summary>- Product detail</summary>
<img src="documentation/validator/lighthouse/product_detail.png" >
</details>
<details><summary>- Bloglist</summary>
<img src="documentation/validator/lighthouse/bloglist.png" >
</details>
<details><summary>- Blogpost detail</summary>
<img src="documentation/validator/lighthouse/blog_detail.png" >
</details>
<details><summary>- Checkout</summary>
<img src="documentation/validator/lighthouse/checkout.png" >
</details>
<details><summary>- Checkout Success</summary>
<img src="documentation/validator/lighthouse/checkout_success.png" >
</details>
<details><summary>- Profile</summary>
<img src="documentation/validator/lighthouse/profile.png" >
</details>
<details><summary>- Wishlist</summary>
<img src="documentation/validator/lighthouse/wishlist.png" >
</details>
<details><summary>- Product Management</summary>
<img src="documentation/validator/lighthouse/product_management.png" >
</details>

# Fixed bugs

### Bug 1

- When I was going to make a purchase, it didn't work. The checkout page was not updated and on my dashboard on the stripe.com page, the payment was incomplete. I had help from tutor support and got help from Joanne. She asked if I exported my keys, STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY in my terminal every time I started my server and I did but still got an error message. When she tested the same with herself, it worked.

#### Solution
 So we agreed to fix an env.py file with STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY instead. So she helped me to created my env.py and have set the stripe sk and pk to the os.environ values.

<details><summary> Export my keys in the terminal.</summary>
    <img src="documentation/bugs/first/terminal.png" >
    </details>
<details><summary> The checkout page error message.</summary>
    <img src="documentation/bugs/first/error_checkout.png" >
    </details>
<details><summary>My dashboard on stripe.com </summary>
    <img src="documentation/bugs/first/stipe_dashboard.png" >
    </details>
<details><summary>My env.py after Joanne helped me </summary>
    <img src="documentation/bugs/first/env.py.png" >
    </details>
<details><summary>The import in my settings.py </summary>
    <img src="documentation/bugs/first/import_in_settings.py.png" >
    </details>
<br>

### Bug 2

- I was trying to get all the products and categories from gitpod to heroku. I did not use fixtures. I added all products and categories from my admin panel. Everything was working great in gitpod when I was running runserver. I followed all the steps in Boutique Ado how to deploy to heroku and use AWS to store all media and static files. But when I open my site in heroku, only my static files work. My products showed 0. And when I went into Admin I had no categories or products like I had when I go into Admin via gitpod. I contacted tutor support for help. But that teacher seemed stressed and repeated everything I had already done but wanted me to do it again and check back at Boutique Ado. Redid everything again but couldn't get it to work. 

#### Solution
So I had to rethink and made my own fixtures with products and categories. After I did that, it worked without a problem.

<details><summary>- 42 products when I was running runserver in gitpop.</summary>
    <img src="documentation/bugs/second/42_products_gitpod.png" >
    <img src="documentation/bugs/second/42_products_gitpod_Admin.png" >
    </details>
<details><summary>- 0 products when I open the app in heroku.</summary>
    <img src="documentation/bugs/second/0_products_heroku.png" >
    <img src="documentation/bugs/second/0_products_heroku_Admin.png" >
    </details>
<br>

### Bug 3

- When I placed an order via gitpod, everything works without problems. My order cost, delivery cost and total cost are correct. When I tried to place an order on the website via heroku, it becomes a double order in my order history and the order cost shows 0. However, if I went into stripe, it was 1 order and the total cost is correct.

#### Solution
I had written tha same function twice. It should throw an error as I've defined the same function twice, but it didn't. So I fixed the second function and it worked after that.

<details><summary>- The problem and the function,</summary>
    <img src="documentation/bugs/third/delivery_cost-0.png" >
    <img src="documentation/bugs/third/dubbel_order_heroku_zero_cost.png" >
    <img src="documentation/bugs/third/order_total_0.png" >
    <img src="documentation/bugs/third/signals.png" >
    </details>
<details><summary>- The right function.</summary>
    <img src="documentation/bugs/third/right_signals.png" >
    </details>
<br>

### Bug 4

- I couldn't get some of my images and some css over to heroku. In gitpod everything looked fine, but when I opened the page in heroku two of my images didn't work and it looked like my whole base.css didn't work either. I stored static and media on aws, when I checked there all files and images were uploaded. All images worked except my logo image which was in my base.html and the other image was in my index.html. And all the other css that I had in all the different apps worked as they should except base.css.

#### Solution
My src attribute didn't have the {{ MEDIA_URL }} template tag - it just had 'media'.  And I forgot to do a hard refresh so all my css would work.

<details><summary>- My images or base.css didn't worked in heroku.</summary>
    <img src="documentation/bugs/fourth/button_css_wont_work.png" >
    <img src="documentation/bugs/fourth/some_pic_wont_work.png" >
    </details>
<details><summary>- My images and base.css worked in gitpod.</summary>
    <img src="documentation/bugs/fourth/button_css_wont_work_works_gitpod.png" >
    <img src="documentation/bugs/fourth/some_pic_wont_work_works_gitpod.png" >
    </details>
<details><summary>- What I missed.</summary>
    <img src="documentation/bugs/fourth/media_url.png" >
    </details>
<br>


# Technologies Used
### Main Languages Used
- HTML5
- CSS3
- Python
- Javascript
- Django
- SQL - Postgres

### Frameworks, Libraries & Programs Used
- [Bootstrap](https://getbootstrap.com/)
- Was used to style the website, add responsiveness and interactivity
- [Git](https://git-scm.com/)
- Git was used for version control by utilizing the Gitpod terminal to commit to Git and push to GitHub
- [GitHub](https://github.com/)
- GitHub is used to store the project's code after being pushed from Git
- [Heroku](https://id.heroku.com)
- Heroku was used to deploy the live project
- [PostgreSQL](https://www.postgresql.org/)
- Database used through Heroku.
- [Miro](https://miro.com/)
-  was used to create the database diagram
- [CI Python Linter](https://pep8ci.herokuapp.com/#)
- CI Python Linter was used to validate all the Python code
- [W3C - HTML](https://validator.w3.org/)
- W3C- HTML was used to validate all the HTML code
- [W3C - CSS](https://jigsaw.w3.org/css-validator/)
- W3C - CSS was used to validate the CSS code
- [Fontawesome](https://fontawesome.com/)
- Was used to add icons to the website
- [Google Chrome Dev Tools](https://developer.chrome.com/docs/devtools/)
- To check App responsiveness and debugging
- [Balsamiq](https://balsamiq.com/)
- To build the wireframes for the project
- [LOGO](https://logo.com/)
- To build the logo for the project
- [AWS](https://aws.amazon.com/)
- was used to host the static files and media
- [Chat GPT](https://chat.openai.com/)
- I have used ChatGPT to write my blog articles.<br>


# Deployment

### Deployment to Heroku

This application is deployed with Heroku.

<details>
  <summary>The steps for deploying through Heroku are as follows:</summary>
  <br>

1.  Visit Heroku and login
2.  Click on New and then choose New App.
3.  Choose a name for your app and then choose your region.
4.  Ideally select the region closest to you
5.  Then press 'Create app'.
  
</details>


<details>
  <summary>To attach The Database:</summary>
  <br>

1. Login or sign up to  [ElephantSQL](https://www.elephantsql.com/).
2. Press create a new instance.
3. Choose a name and plan. Then click on select region. 
4. Select the closest Data Center to you
5. Click on "Create Instance".
6. Go back to the start page and click on your new database.
7. Copy the URL for the database.
  
 </details>

<br>

- Go back to Heroku and click on the settings tab of your application.
    
- Click on "Reveal config vars".

- Add a new config var named DATABASE_URL and paste in the URL from  ElephantSQL  as the value.

- Go back to Gitpod or the IDE you are using and install two more requirements for the database:

- In Gitpod install dj-database_url and psycopg2 to connect to your external database
  
- Update your requirements.txt file by typing in  `pip3 freeze --local > requirements.txt`

- Add the DATABASE_URL to your env.py file or environment variables in gitpod.

- Go to settings.py and  `import dj_database_url`

- Comment out the default  `DATABASES`  setting.

- Add this under the commented out section:

``` DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL')) }

```
Run migrations for the new database.

1.  In the root directory of your project, create a file called "Procfile" and add  `web: gunicorn project_name.wsgi`  so Heroku will know what kind of application it is.
    
2.  In settings.py add ['app_name.heroku.com', 'localhost'] to  `ALLOWED_HOSTS`.
    
3.  Commit and push these changes to GitHub.
    
4.  In the Heroku settings tab of your project update the config vars to the following:

| Key | Value  |
| -- | -- |
|AWS_ACCESS_KEY_ID|From AWS in CSV Download|
|AWS_SECRET_ACCESS_KEY|From AWS in CSV Download|
|DATABASE_URL|From ElephantSQL dashboard|
|EMAIL_HOST_PASSWORD|App Password from Email Client|
|EMAIL_HOST_USER|Email address|
|SECRET_KEY|Randomly Generated Django Key|
|STRIPE_PUBLIC_KEY|Publishable key from Stripe Dashboard|
|STRIPE_SECRET_KEY|Secret key from Stripe Dashboard|
|STRIPE_WH_SECRET|Signing secret from Stripe Webhooks Endpoint|
|USE_AWS|True|

- If you deploy at the beginning of the project then add the key value of: `DISABLE_COLLCETSTATIC`  and set it to 1. When you have  staticfiles to push then remove this variable.

- Once the project is completed and you are no longer working on it set  `DEBUG`  =  `False`  in settings.py.

- Log in to Heroku and select the deploy tab on your Heroku App and connect your GitHub account.

- Search for your repository and connect it.

- Once you have selected the correct repository, scroll down and click "Deploy Branch".

- Watch the log as it deploys your project and ensure there are no errors.

- If everything is correct it should deploy successfully.

- Click on open app at the top of the page to view your deployed app.

<br>

Requirements.txt: This must be updated for deployment in Heroku. It stores data of libraries used for project
<details><summary>See Image</summary>
    <img src="documentation/requirements.png" >
    </details>

# Credits

### Content

- All the products content were taken from [BURTON](https://www.burton.com/gb/en/home)
- The product images were taken from [BURTON](https://www.burton.com/gb/en/home)
- The blogpost images were taken from [PEXELS](https://www.pexels.com/)
- The Snowpatrol logo and favicon are my own designed and build from [LOGO](https://logo.com/)
- To save time and also to try out some AI resources I have used ChatGPT to write my blog articles. [Chat GPT](https://chat.openai.com/)
<br>

### Resources

####  Code Institute
- The Code Institute 'Boutique Ado' walkthrough project assisted and guided in the setup and basic structure of this project.
- The Code Institute - Hello Django - Walkthrough
- The Code Institute - I think therefore I blog - Django blog project Walkthrough

#### Repositories
- I have taken help of various repositories for my readme and coding
<br>
[Pedro Cristo](https://github.com/PedroCristo/portfolio_project_5/tree/main)
<br>
[Pauline Rugwevera](https://github.com/pauline-rugwevera)
<br>
[Dee68](https://github.com/Dee68/pp5/tree/main)
<br>
[PPindel](https://github.com/PPindel/test-a-wheel/tree/0c046372aa5c8eb0e45a575fd59af916244c025e)

- I also sourced information and help from a variety of sources such as Slack Community Channels, W3Schools, and YouTube for Online Web Tutorials and resources.
- When I get stuck, I have received incredibly good help from tutor support. 
<br>
John, Joanne, Oisin and Roman

## Media

### Images

- The images on the homepage including blogpost images are taken from [pexels.com](https://www.pexels.com/)
- The product images were taken from [BURTON](https://www.burton.com/gb/en/home)
- The Snowpatrol logo and favicon are my own designed and build from [LOGO](https://logo.com/)

# Acknowledgement and support
 - I greatly appreciate the tutors at Code Institute for their patience and support!
 - The Code Institute Slack community for tips and guidance!
 - My mentor Maritna Terlevic who responded quickly when I needed help and was clear about what needed to be done. Great support!
 - My beloved husband who has taken care of everything in the home while I have been studying. Fed me, cleaned and took care of our newborn baby.

