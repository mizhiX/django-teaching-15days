
from flask import Blueprint, render_template, redirect, \
    url_for, session, request, jsonify

from App.models import Area, Facility
from utils import status_code

house_bluprint = Blueprint('house', __name__)


@house_bluprint.route('/myhouse/')
def my_house():
    return render_template('myhouse.html')


@house_bluprint.route('/newhouse/')
def new_house():
    return render_template('newhouse.html')


@house_bluprint.route('/area_facility/')
def area_facility():
    areas = Area.query.all()
    facilitys = Facility.query.all()

    areas_list = [area.to_dict() for area in areas]
    facilitys_list = [facility.to_dict() for facility in facilitys]
    return jsonify(code=status_code.OK,
                   areas=areas_list,
                   facilitys=facilitys_list)

