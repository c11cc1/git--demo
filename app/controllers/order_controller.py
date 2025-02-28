from flask import Blueprint
# from models.order import Order
from views.order_view import render_orders_page

order_blueprint = Blueprint('order', __name__)

@order_blueprint.route('/')
def show_orders():
    orders_data = Order.get_orders()
    return render_orders_page(orders_data)
