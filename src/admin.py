from flask import request
from flask_admin import Admin,expose,BaseView
from src import app, db, utils
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView


class MyAdminIndexView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/index.html')


class StatsView(BaseView):
    @expose('/')
    def index(self):
        type_rooms_list = utils.get_all_type_rooms()
        used_type_room_counter = utils.get_used_quantity_type_room_in_month()
        return self.render('admin/stats.html',
                           type_rooms_list=type_rooms_list,
                           used_type_room_counter=used_type_room_counter)


admin = Admin(app=app, name='Admin page', template_mode='bootstrap4', index_view=MyAdminIndexView())
admin.add_view(StatsView(name='Thống kê'))
