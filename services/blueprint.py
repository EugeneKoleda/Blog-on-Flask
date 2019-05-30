from flask import Blueprint, render_template, request, redirect, url_for


services = Blueprint('services', __name__, template_folder='templates')


@services.route('/')
def index():
    return render_template('services/index.html')

