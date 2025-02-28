from flask import render_template

def render_suppliers_page(suppliers_data):
    return render_template('supplier.html', suppliers=suppliers_data)
