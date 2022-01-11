import imghdr

from flask import request
from flask_admin import Admin, expose, BaseView
from flask_admin.form import FileUploadField
from wtforms import ValidationError

from src import app, db, utils
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from src.models import Room, TypeRoom, RentalVoucher, User, ChangePolicyNumber, UserRole
from flask_login import logout_user, current_user


class AuthenticatedModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')


class RoomView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    column_exclude_list = ['rentalVoucher', 'image']
    column_filters = ['quantity_bed', 'price']
    column_searchable_list = ['quantity_bed', 'price']
    column_labels = {
        'id': 'Mã phòng',
        'quantity_bed': 'Số giường',
        'price': 'Giá',
        'status': 'Trạng thái',
        'typeRoom': 'Loại phòng',
        'rental_voucher': 'Phiếu thuê phòng',
        'image': 'Hình ảnh',
        'descriptions': 'Mô tả'
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


class UserView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    column_exclude_list = ['avatar']
    column_filters = ['id', 'username']
    column_searchable_list = ['id', 'username']
    column_labels = {
        'id': 'Mã',
        'user': 'Tên người dùng',
        'password': 'Mật khẩu',
        'joined_date': 'Ngày tạo',
        'user_role': 'Quyền',
    }
    form_excluded_columns = ['comments']


class ChangePolicyNumberView(ModelView):
    column_display_pk = True
    can_view_details = True
    can_export = True
    edit_modal = True
    details_modal = True
    column_exclude_list = ['']
    column_filters = ['id']
    column_searchable_list = ['id']
    column_labels = {
        'id': 'Mã',
        'foreign_visitor_number': 'Hệ số khách nước ngoài',
        'domestic_visitor_number': 'Hệ số khách trong nước',
        'quantity_types_visitors': 'Số lượng các loại khách đến',
        'quantity_types_rooms': 'Số lượng các loại phòng',
        'max_visitors_in_a_room': 'Số lượng khách tối đa',
        'number_price' : 'Giá',
        'amount_extra' : 'Số tiền thêm'
    }


class StatsView(BaseView):
    @expose('/')
    def index(self):
        type_rooms_list = utils.get_all_type_rooms()
        used_type_room_counter = utils.get_used_quantity_type_room_in_month()
        return self.render('admin/stats.html',
                           type_rooms_list=type_rooms_list,
                           used_type_room_counter=used_type_room_counter)


admin = Admin(app=app, name='Lotus hotel', template_mode='bootstrap4', index_view=MyAdminIndexView())
admin.add_view(UserView(User, db.session, name='Người dùng'))
admin.add_view(RoomView(Room, db.session, name='Phòng'))
admin.add_view(TypeRoomView(TypeRoom, db.session, name='Loại phòng'))
admin.add_view(ChangePolicyNumberView(ChangePolicyNumber, db.session, name='Hệ số người dùng'))
admin.add_view(StatsView(name='Thống kê'))


