
from flask import request
from flask_admin import Admin,expose,BaseView
from src import app, db, utils
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView
from src.models import Room, TypeRoom


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
    # column_exclude_list = ['image']
    # column_filters = ['name', 'price']
    # column_searchable_list = ['name']
    column_labels = {
        'id': 'Mã phòng',
        'quantity_bed':'Số giường',
        'price': 'Giá',
        'status': 'Trạng thái',
        'type_room_id': 'Loại phòng',
        'Typeroom': 'Loại giường'
    }
    form_excluded_columns = ['rental_voucher']
admin = Admin(app=app, name='Admin page', template_mode='bootstrap4', index_view=MyAdminIndexView())
admin.add_view(RoomView(Room, db.session, name='Phòng'))
admin.add_view(ModelView(TypeRoom, db.session, name='Loại phòng'))
admin.add_view(StatsView(name='Thống kê'))


