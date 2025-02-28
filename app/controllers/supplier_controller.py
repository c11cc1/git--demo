from flask import Blueprint
# from models.supplier import Supplier
from views.supplier_view import render_suppliers_page

supplier_blueprint = Blueprint('supplier', __name__)

@supplier_blueprint.route('/')
def show_suppliers():
    suppliers_data = Supplier.get_suppliers()
    return render_suppliers_page(suppliers_data)
