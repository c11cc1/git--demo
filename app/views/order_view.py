from flask import render_template

def render_orders_page(orders_data):
    return render_template('orders.html', orders=orders_data)
