
import os

from flask import Blueprint, render_template, redirect, \
    url_for, session, request, jsonify

from App.models import Area, Facility, House, db, HouseImage
from utils import status_code
from utils.functions import is_login
from utils.setting import UPLOAD_DIR

house_bluprint = Blueprint('house', __name__)


@house_bluprint.route('/myhouse/', methods=['GET'])
def my_house():
    return render_template('myhouse.html')


@house_bluprint.route('/myhouses/', methods=['GET'])
@is_login
def user_my_house():
    houses = House.query.filter(House.user_id == session['user_id']).all()
    houses_info = [house.to_dict() for house in houses]
    return jsonify(code=status_code.OK, houses=houses_info)


@house_bluprint.route('/newhouse/', methods=['GET'])
def new_house():
    return render_template('newhouse.html')


@house_bluprint.route('/area_facility/', methods=['GET'])
def area_facility():
    areas = Area.query.all()
    facilitys = Facility.query.all()

    areas_list = [area.to_dict() for area in areas]
    facilitys_list = [facility.to_dict() for facility in facilitys]
    return jsonify(code=status_code.OK,
                   areas=areas_list,
                   facilitys=facilitys_list)


@house_bluprint.route('/newhouse/', methods=['POST'])
def user_new_house():
    data = request.form.to_dict()
    facility_ids = request.form.getlist('facility')

    house = House()
    house.user_id = session['user_id']
    house.title = data.get('title')
    house.price = data.get('price')
    house.area_id = data.get('area_id')
    house.address = data.get('address')
    house.room_count = data.get('room_count')
    house.house_id = data.get('acreage')
    house.unit = data.get('unit')
    house.capacity = data.get('capacity')
    house.beds = data.get('beds')
    house.deposit = data.get('deposit')
    house.min_days = data.get('min_days')
    house.max_days = data.get('max_days')

    facility_list = Facility.query.filter(Facility.id.in_(facility_ids)).all()
    house.facilities = facility_list
    try:
        house.add_update()
    except:
        db.session.rollback()
    return jsonify(code=status_code.OK, house_id=house.id)


@house_bluprint.route('/house_images/', methods=['POST'])
def house_images():
    house_id = request.form.get('house_id')
    house_image = request.files.get('house_image')

    save_url = os.path.join(UPLOAD_DIR, house_image.filename)
    house_image.save(save_url)


    # 保存房屋图片信息
    image_url = os.path.join('upload', house_image.filename)

    # 保存房屋的首图
    house = House.query.get(house_id)
    if not house.index_image_url:
        house.index_image_url = image_url
        house.add_update()


    h_image = HouseImage()
    h_image.house_id = house_id
    h_image.url = image_url
    try:
        h_image.add_update()
    except:
        db.session.rollback()
        return jsonify(status_code.DATABASE_ERROR)
    return jsonify(code=status_code.OK, image_url=image_url)


@house_bluprint.route('/detail/', methods=['GET'])
def detail():
    return render_template('detail.html')


@house_bluprint.route('/detail/<int:id>/', methods=['GET'])
def house_detail(id):
    house = House.query.get(id)
    house_info = house.to_full_dict()

    return jsonify(code=status_code.OK,
                   house_info=house_info)


@house_bluprint.route('/booking/', methods=['GET'])
def booking():
    return render_template('booking.html')
