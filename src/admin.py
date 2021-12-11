from flask import request
from flask_admin import Admin,expose,BaseView
from src import app, db, utils
from flask_admin.contrib.sqla import ModelView
from flask_admin import AdminIndexView


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


admin = Admin(app=app, name='Admin page', template_mode='bootstrap4', index_view=MyAdminIndexView())
admin.add_view(StatsView(name='Thống kê'))
