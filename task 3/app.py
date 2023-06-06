from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(_name_)

@app.route('/')
def index():
    product_link = "https://yoshops.com/products/hrx-by-hrithik-roshan-men-orange-printed-cotton-t-shirt-with-yoshops-free-gift-hear-phone-pouch"

    # Fetch reviews from Yoshops.com
    response = requests.get(product_link)
    soup = BeautifulSoup(response.text, 'html.parser')

    reviews = []

    # Extract the reviews from the HTML
    review_elements = soup.select('.review-item')
    for element in review_elements:
        rating = element.select_one('.review-rating').text.strip()
        review = element.select_one('.review-text').text.strip()
        reviews.append({'rating': rating, 'review': review})

    return render_template('index.html', reviews=reviews)

if _name_ == '_main_':
    app.run()