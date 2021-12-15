import imghdr

from flask import request
from flask_admin import Admin, expose, BaseView
from flask_admin.form import FileUploadField
from wtforms import ValidationError

from src import app, db, utils
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from src.models import Room, TypeRoom, RentalVoucher


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')


class Home_page(BaseView):
    @expose('/')
    def index(self):
        return self.render('index.html')


class RoomView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    column_exclude_list = ['rentalVoucher']
    column_filters = ['quantity_bed', 'price']
    column_searchable_list = ['quantity_bed', 'price']
    column_labels = {
        'id': 'Mã phòng',
        'quantity_bed': 'Số giường',
        'price': 'Giá',
        'status': 'Trạng thái',
        'typeRoom': 'Loại phòng',
        'rentalVoucher': 'Phiếu thuê phòng',
        'image': 'Hình ảnh'
    }
    form_excluded_columns = ['receiptDetails', 'rentalVoucher']


class TypeRoomView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    column_filters = ['id','type_room_name']
    column_searchable_list = ['id','type_room_name']
    column_labels = {
        'id': 'Mã thuê phòng',
        'type_room_name': 'Tên loại phòng'
    }


class StatsView(BaseView):
    @expose('/')
    def index(self):
        type_rooms_list = utils.get_all_type_rooms()
        used_type_room_counter = utils.get_used_quantity_type_room_in_month()
        return self.render('admin/stats.html',
                           type_rooms_list=type_rooms_list,
                           used_type_room_counter=used_type_room_counter)


admin = Admin(app=app, name='Admin page', template_mode='bootstrap4', index_view=MyAdminIndexView())
admin.add_view(Home_page(name='Website'))
admin.add_view(RoomView(Room, db.session, name='Phòng'))
admin.add_view(TypeRoomView(TypeRoom, db.session, name='Loại phòng'))
admin.add_view(StatsView(name='Thống kê'))


