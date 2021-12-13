
from flask import request
from flask_admin import Admin,expose,BaseView
from src import app, db, utils
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from src.models import Room, TypeRoom, RentalVoucher


class StatsView(BaseView):
    @expose('/')
    def index(self):
        # kw = request.args.get('kw')
        # from_date = request.args.get('from_date')
        # to_date = request.args.get('to_date')
        # stats = utils.product_stats(kw=kw, from_date=from_date, to_date=to_date)
        return self.render('admin/stats.html')


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
    column_exclude_list = ['rentalVoucher']
    column_filters = ['quantity_bed', 'price']
    column_searchable_list = ['quantity_bed', 'price']
    column_labels = {
        'id': 'Mã phòng',
        'quantity_bed': 'Số giường',
        'price': 'Giá',
        'status': 'Trạng thái',
        'typeRoom': 'Loại phòng',
        'rentalVoucher': 'Phiếu thuê phòng'
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

admin = Admin(app=app, name='Quản lí', template_mode='bootstrap4', index_view=MyAdminIndexView())
admin.add_view(RoomView(Room, db.session, name='Phòng'))
admin.add_view(TypeRoomView(TypeRoom, db.session, name='Loại phòng'))
admin.add_view(StatsView(name='Thống kê'))


