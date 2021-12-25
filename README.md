# kobbyshop - Django Ecommerce App
A fully featured e-commerce application powered by Django.

<h2>Sections</h2>
<p>
  <ul>
    <li><a href="#desc">Project Description</a></li>
    <li><a href="#feat">Features</a></li>
    <li><a href="tech">Technology</a></li>
    <li><a href="#setup">Setup</a></li>
    <li><a href="#image">Screenshots</a></li>
    <li><a href="#status">Project Status</a></li>
    <li><a href="#contribute">Contributing</a></li>
    <li><a href="#contact">Author</a></li>
    <li><a href="#licence">Licence</a></li>
   </ul>
</p>

<h2 id="desc">Project Description</h2>
<p> This project is a fully featured django ecommerce application with some key functionalities in a modern day
ecommerce platform.
</p>

<h2 id="feat">Features</h2>
<ul>
  <li>Multi-language integration (2 languages at the moment)</li>
  <li>Product Recommendation</li>
  <li>Braintree Integration</li>
  <li>PDF Invoice</li>
</ul>

<h2 id="tech">Technology</h2>
<ul>
  <li>Python</li>
  <li>Django</li>
  <li>HTML5</li>
  <li>CSS</li>
  <li>Docker</li>
  <li>Celery</li>
  <li>Redis</li>
  <li>RabbitMQ</li>
</ul>

<h2 href=#setup>Setup</h2>
To run the application, please follow guidlines below
<p>
1. Requirements
 <ul>
  <li>You need a PC or Macbook</li>
  <li>You have Git installed</li>
  <li>You have Docker installed on your Machine</li>
  <li>A Text Editor or IDE(eg.Vscode, Sublime, Pycharm)</li>
</ul></p>
<p>2. Install python3 and Pipenv</p>

<p>3. Now you setup as indicated below:</p>


 ```
  # Clone this repository into the directory of your choice
  $ git clone https://github.com/KwabenaYeboah/kobbyshop.git
  # Move into project folder
  $ cd kobbyshop
  # Build the image and run the container
  $ docker-compose up --build
  # Migrate database models
  (kobbyshop-xxx) $ docker-compose exec web python manage.py migrate
  
  # Create superuser account
  (Final-Senior-Year-Project-XXXX) $ docker-compose exec web python manage.py createsuperuser
  # start server
  (Final-Senior-Year-Project-XXXX) $ docker-compose exec web python manage.py runserver
  
  # Copy the IP address provided once your server has completed building the site. (It will say something like >> Serving at 127.0.0.1....).
  
  # Open the address in the browser
  >>> http://127.0.0.1:XXXX/products/
  
  
  # Django Admin
  >>> http://127.0.0.1:XXXX/admin/
  ```
  
  <h2 id="image">Screenshots</h2>
  
  Product List
  :------------------:
  ![ProductList](https://github.com/KwabenaYeboah/kobbyshop/blob/master/screenshots/product_list.png)
  
   Product List By Category
  :--------------------------:
  ![ProductList By Category](https://github.com/KwabenaYeboah/kobbyshop/blob/master/screenshots/product_list_by_category.png)
  
   Product Detail
  :------------------:
  ![Product Detail](https://github.com/KwabenaYeboah/kobbyshop/blob/master/screenshots/product_detail.png)
  
   Shopping Cart
  :------------------:
  ![Shopping Cart](https://github.com/KwabenaYeboah/kobbyshop/blob/master/screenshots/shopping_cart.png)
  
   Checkout
  :------------------:
  ![Checkout](https://github.com/KwabenaYeboah/kobbyshop/blob/master/screenshots/checkout.png)
  
   Product Recommendation
  :------------------------:
  ![Product Recommendation](https://github.com/KwabenaYeboah/kobbyshop/blob/master/screenshots/product_recommendation.png)
  
   BrainTree Integration
  :------------------:
  ![Braintree Integration](https://github.com/KwabenaYeboah/kobbyshop/blob/master/screenshots/make_payment_with_braintree.png)
  
   Invoice
  :------------------:
  ![Invoice](https://github.com/KwabenaYeboah/kobbyshop/blob/master/screenshots/pdf_invoice.png)
  

<h2 id="status">Project Status</h2>
Project is: In Progress

<h2 id="contribute">Contributing</h2>
Pull requests and stars are always welcome

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

<h2 id="contact">Author</h2>

[KwabenaYeboah](https://github.com/KwabenaYeboah/)

<h2 id="licence">Licence</h2>

  **MIT** Licence
