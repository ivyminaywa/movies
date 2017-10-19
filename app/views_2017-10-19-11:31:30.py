# coding: utf-8 
# AUTOGENERATED BY gen_script.sh from 
# Copyright (C) Nyimbi Odero, Kamiisa, Onkololeessa 19, 11:18:24 WD EAT 2017
 
 
import calendar
from flask import redirect, flash, url_for, Markup
from flask import render_template
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.views import ModelView, BaseView, MasterDetailView, MultipleView, RestCRUDView, CompactCRUDMixin
from flask_appbuilder import ModelView, CompactCRUDMixin, aggregate_count, action, expose, BaseView, has_access
from flask_appbuilder.charts.views import ChartView, TimeChartView, GroupByChartView
from flask_appbuilder.models.group import aggregate_count
from flask_appbuilder.widgets import ListThumbnail, ListWidget
from flask_appbuilder.widgets import FormVerticalWidget, FormInlineWidget, FormHorizontalWidget, ShowBlockWidget
from flask_appbuilder.models.sqla.filters import FilterStartsWith, FilterEqualFunction as FA
from app import appbuilder, db
 
 
from .models import *
 
 
 
# Basic Lists 
hide_list = ['created_by', 'changed_by', 'created_on', 'changed_on'] 
 
 
#To pretty Print from PersonMixin 
def pretty_month_year(value):
    return calendar.month_name[value.month] + ' ' + str(value.year)
 
 
def pretty_year(value):
    return str(value.year)
 
 
def fill_gender():
  try:
      db.session.add(Gender(name='Male'))
      db.session.add(Gender(name='Female'))
      db.session.commit()
  except:
      db.session.rollback()
class AgeRatingView(ModelView):#MasterDetailView, MultipleView    datamodel=SQLAInterface(AgeRating, db.session)    #add_title =    #list_title =    #edit_title =    #show_title =    #add_widget = (FormVerticalWidget|FormInlineWidget)    #show_widget = ShowBlockWidget    #list_widget = (ListThumbnail|ListWidget)    #base_order = ("name", "asc")    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns    add_exclude_columns = edit_exclude_columns = audit_exclude_columns    #add_columns = person_list_columns + ref_columns + contact_columns    #edit_columns = person_list_columns + ref_columns + contact_columns    #list_columns = person_list_columns + ref_columns + contact_columns    #list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)    #related_views =[]    #show_fieldsets = person_show_fieldset + contact_fieldset    #edit_fieldsets = add_fieldsets = \ 
			# ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset    #description_columns = {"name":"your models name column","address":"the address column"}    #show_template = "appbuilder/general/model/show_cascade.html"    #edit_template = "appbuilder/general/model/edit_cascade.html"

    @action("muldelete", "Delete", Markup("<p>Delete all Really?</p><p>Ok then...</p>"), "fa-rocket")
    def muldelete(self, items):
        self.datamodel.delete_all(items)
        self.update_redirect()
        return redirect(self.get_redirect())


class CusDvdView(ModelView):#MasterDetailView, MultipleView    datamodel=SQLAInterface(CusDvd, db.session)    #add_title =    #list_title =    #edit_title =    #show_title =    #add_widget = (FormVerticalWidget|FormInlineWidget)    #show_widget = ShowBlockWidget    #list_widget = (ListThumbnail|ListWidget)    #base_order = ("name", "asc")    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns    add_exclude_columns = edit_exclude_columns = audit_exclude_columns    #add_columns = person_list_columns + ref_columns + contact_columns    #edit_columns = person_list_columns + ref_columns + contact_columns    #list_columns = person_list_columns + ref_columns + contact_columns    #list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)    #related_views =[]    #show_fieldsets = person_show_fieldset + contact_fieldset    #edit_fieldsets = add_fieldsets = \ 
			# ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset    #description_columns = {"name":"your models name column","address":"the address column"}    #show_template = "appbuilder/general/model/show_cascade.html"    #edit_template = "appbuilder/general/model/edit_cascade.html"

    @action("muldelete", "Delete", Markup("<p>Delete all Really?</p><p>Ok then...</p>"), "fa-rocket")
    def muldelete(self, items):
        self.datamodel.delete_all(items)
        self.update_redirect()
        return redirect(self.get_redirect())


class CustomerView(ModelView):#MasterDetailView, MultipleView    datamodel=SQLAInterface(Customer, db.session)    #add_title =    #list_title =    #edit_title =    #show_title =    #add_widget = (FormVerticalWidget|FormInlineWidget)    #show_widget = ShowBlockWidget    #list_widget = (ListThumbnail|ListWidget)    #base_order = ("name", "asc")    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns    add_exclude_columns = edit_exclude_columns = audit_exclude_columns    #add_columns = person_list_columns + ref_columns + contact_columns    #edit_columns = person_list_columns + ref_columns + contact_columns    #list_columns = person_list_columns + ref_columns + contact_columns    #list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)    #related_views =[]    #show_fieldsets = person_show_fieldset + contact_fieldset    #edit_fieldsets = add_fieldsets = \ 
			# ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset    #description_columns = {"name":"your models name column","address":"the address column"}    #show_template = "appbuilder/general/model/show_cascade.html"    #edit_template = "appbuilder/general/model/edit_cascade.html"

    @action("muldelete", "Delete", Markup("<p>Delete all Really?</p><p>Ok then...</p>"), "fa-rocket")
    def muldelete(self, items):
        self.datamodel.delete_all(items)
        self.update_redirect()
        return redirect(self.get_redirect())


class DvdView(ModelView):#MasterDetailView, MultipleView    datamodel=SQLAInterface(Dvd, db.session)    #add_title =    #list_title =    #edit_title =    #show_title =    #add_widget = (FormVerticalWidget|FormInlineWidget)    #show_widget = ShowBlockWidget    #list_widget = (ListThumbnail|ListWidget)    #base_order = ("name", "asc")    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns    add_exclude_columns = edit_exclude_columns = audit_exclude_columns    #add_columns = person_list_columns + ref_columns + contact_columns    #edit_columns = person_list_columns + ref_columns + contact_columns    #list_columns = person_list_columns + ref_columns + contact_columns    #list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)    #related_views =[]    #show_fieldsets = person_show_fieldset + contact_fieldset    #edit_fieldsets = add_fieldsets = \ 
			# ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset    #description_columns = {"name":"your models name column","address":"the address column"}    #show_template = "appbuilder/general/model/show_cascade.html"    #edit_template = "appbuilder/general/model/edit_cascade.html"

    @action("muldelete", "Delete", Markup("<p>Delete all Really?</p><p>Ok then...</p>"), "fa-rocket")
    def muldelete(self, items):
        self.datamodel.delete_all(items)
        self.update_redirect()
        return redirect(self.get_redirect())


class GenreView(ModelView):#MasterDetailView, MultipleView    datamodel=SQLAInterface(Genre, db.session)    #add_title =    #list_title =    #edit_title =    #show_title =    #add_widget = (FormVerticalWidget|FormInlineWidget)    #show_widget = ShowBlockWidget    #list_widget = (ListThumbnail|ListWidget)    #base_order = ("name", "asc")    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns    add_exclude_columns = edit_exclude_columns = audit_exclude_columns    #add_columns = person_list_columns + ref_columns + contact_columns    #edit_columns = person_list_columns + ref_columns + contact_columns    #list_columns = person_list_columns + ref_columns + contact_columns    #list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)    #related_views =[]    #show_fieldsets = person_show_fieldset + contact_fieldset    #edit_fieldsets = add_fieldsets = \ 
			# ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset    #description_columns = {"name":"your models name column","address":"the address column"}    #show_template = "appbuilder/general/model/show_cascade.html"    #edit_template = "appbuilder/general/model/edit_cascade.html"

    @action("muldelete", "Delete", Markup("<p>Delete all Really?</p><p>Ok then...</p>"), "fa-rocket")
    def muldelete(self, items):
        self.datamodel.delete_all(items)
        self.update_redirect()
        return redirect(self.get_redirect())


class MovieView(ModelView):#MasterDetailView, MultipleView    datamodel=SQLAInterface(Movie, db.session)    #add_title =    #list_title =    #edit_title =    #show_title =    #add_widget = (FormVerticalWidget|FormInlineWidget)    #show_widget = ShowBlockWidget    #list_widget = (ListThumbnail|ListWidget)    #base_order = ("name", "asc")    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns    add_exclude_columns = edit_exclude_columns = audit_exclude_columns    #add_columns = person_list_columns + ref_columns + contact_columns    #edit_columns = person_list_columns + ref_columns + contact_columns    #list_columns = person_list_columns + ref_columns + contact_columns    #list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)    #related_views =[]    #show_fieldsets = person_show_fieldset + contact_fieldset    #edit_fieldsets = add_fieldsets = \ 
			# ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset    #description_columns = {"name":"your models name column","address":"the address column"}    #show_template = "appbuilder/general/model/show_cascade.html"    #edit_template = "appbuilder/general/model/edit_cascade.html"

    @action("muldelete", "Delete", Markup("<p>Delete all Really?</p><p>Ok then...</p>"), "fa-rocket")
    def muldelete(self, items):
        self.datamodel.delete_all(items)
        self.update_redirect()
        return redirect(self.get_redirect())


class ShelveView(ModelView):#MasterDetailView, MultipleView    datamodel=SQLAInterface(Shelve, db.session)    #add_title =    #list_title =    #edit_title =    #show_title =    #add_widget = (FormVerticalWidget|FormInlineWidget)    #show_widget = ShowBlockWidget    #list_widget = (ListThumbnail|ListWidget)    #base_order = ("name", "asc")    search_exclude_columns = person_exclude_columns + biometric_columns + person_search_exclude_columns    add_exclude_columns = edit_exclude_columns = audit_exclude_columns    #add_columns = person_list_columns + ref_columns + contact_columns    #edit_columns = person_list_columns + ref_columns + contact_columns    #list_columns = person_list_columns + ref_columns + contact_columns    #list_widget = ListBlock|ListItem|ListThumbnail|ListWidget (default)    #related_views =[]    #show_fieldsets = person_show_fieldset + contact_fieldset    #edit_fieldsets = add_fieldsets = \ 
			# ref_fieldset + person_fieldset + contact_fieldset #+  activity_fieldset + place_fieldset + biometric_fieldset + employment_fieldset    #description_columns = {"name":"your models name column","address":"the address column"}    #show_template = "appbuilder/general/model/show_cascade.html"    #edit_template = "appbuilder/general/model/edit_cascade.html"

    @action("muldelete", "Delete", Markup("<p>Delete all Really?</p><p>Ok then...</p>"), "fa-rocket")
    def muldelete(self, items):
        self.datamodel.delete_all(items)
        self.update_redirect()
        return redirect(self.get_redirect())

#
#
# class AttorneyChartView(GroupByChartView):
#     datamodel = SQLAInterface(Attorney , db.session)
#     chart_title = 'Grouped Attorney by Birth'
#     label_columns = AttorneyView.label_columns
#     chart_type = 'PieChart'
#
#     definitions = [
#         {
#             'group' : 'age_today',
#             "series" : [(aggregate_count,"age_today")]
#         },
#         {
#             'group' : 'gender',
#             "series" : [(aggregate_count,"age_today")]
#         }
#     ]
#
#
# class AttorneyTimeChartView(GroupByChartView):
#     datamodel = SQLAInterface(Attorney , db.session)
#
#     chart_title = 'Grouped Birth Attorney'
#     chart_type = 'AreaChart'
#     label_columns = AttorneyView.label_columns
#     definitions = [
#         {
#             'group' : 'age_today',
#             'formatter': pretty_month_year,
#             "series" : [(aggregate_count,"age_today")]
#         },
#         {
#             'group': 'age_today',
#             'formatter': pretty_year,
#             "series" : [(aggregate_count,"age_today")]
#         }
#     ]
#
#
#
# class PlaintiffChartView(GroupByChartView):
#     datamodel = SQLAInterface(Plaintiff , db.session)
#     chart_title = 'Grouped Plaintiff by Birth'
#     label_columns = PlaintiffView.label_columns
#     chart_type = 'PieChart'
#
#     definitions = [
#         {
#             'group' : 'age_today',
#             "series" : [(aggregate_count,"age_today")]
#         },
#         {
#             'group' : 'gender',
#             "series" : [(aggregate_count,"age_today")]
#         }
#     ]
#
#
# class PlaintiffTimeChartView(GroupByChartView):
#     datamodel = SQLAInterface(Plaintiff , db.session)
#
#     chart_title = 'Grouped Birth Plaintiff'
#     chart_type = 'AreaChart'
#     label_columns = PlaintiffView.label_columns
#     definitions = [
#         {
#             'group' : 'age_today',
#             'formatter': pretty_month_year,
#             "series" : [(aggregate_count,"age_today")]
#         },
#         {
#             'group': 'age_today',
#             'formatter': pretty_year,
#             "series" : [(aggregate_count,"age_today")]
#         }
#     ]
#
#
#
# class ObserverChartView(GroupByChartView):
#     datamodel = SQLAInterface(Observer , db.session)
#     chart_title = 'Grouped Observer by Birth'
#     label_columns = ObserverView.label_columns
#     chart_type = 'PieChart'
#
#     definitions = [
#         {
#             'group' : 'age_today',
#             "series" : [(aggregate_count,"age_today")]
#         },
#         {
#             'group' : 'gender',
#             "series" : [(aggregate_count,"age_today")]
#         }
#     ]
#
#
# class ObserverTimeChartView(GroupByChartView):
#     datamodel = SQLAInterface(Observer , db.session)
#
#     chart_title = 'Grouped Birth Observer'
#     chart_type = 'AreaChart'
#     label_columns = ObserverView.label_columns
#     definitions = [
#         {
#             'group' : 'age_today',
#             'formatter': pretty_month_year,
#             "series" : [(aggregate_count,"age_today")]
#         },
#         {
#             'group': 'age_today',
#             'formatter': pretty_year,
#             "series" : [(aggregate_count,"age_today")]
#         }
#     ]
#
#
#
# class SuretyChartView(GroupByChartView):
#     datamodel = SQLAInterface(Surety , db.session)
#     chart_title = 'Grouped Surety by Birth'
#     label_columns = SuretyView.label_columns
#     chart_type = 'PieChart'
#
#     definitions = [
#         {
#             'group' : 'age_today',
#             "series" : [(aggregate_count,"age_today")]
#         },
#         {
#             'group' : 'gender',
#             "series" : [(aggregate_count,"age_today")]
#         }
#     ]
#
#
# class SuretyTimeChartView(GroupByChartView):
#     datamodel = SQLAInterface(Surety , db.session)
#
#     chart_title = 'Grouped Birth Surety'
#     chart_type = 'AreaChart'
#     label_columns = SuretyView.label_columns
#     definitions = [
#         {
#             'group' : 'age_today',
#             'formatter': pretty_month_year,
#             "series" : [(aggregate_count,"age_today")]
#         },
#         {
#             'group': 'age_today',
#             'formatter': pretty_year,
#             "series" : [(aggregate_count,"age_today")]
#         }
#     ]
#
#
#
# class ProsecutorChartView(GroupByChartView):
#     datamodel = SQLAInterface(Prosecutor , db.session)
#     chart_title = 'Grouped Prosecutor by Birth'
#     label_columns = ProsecutorView.label_columns
#     chart_type = 'PieChart'
#
#     definitions = [
#         {
#             'group' : 'age_today',
#             "series" : [(aggregate_count,"age_today")]
#         },
#         {
#             'group' : 'gender',
#             "series" : [(aggregate_count,"age_today")]
#         }
#     ]
#
#
# class ProsecutorTimeChartView(GroupByChartView):
#     datamodel = SQLAInterface(Prosecutor , db.session)
#
#     chart_title = 'Grouped Birth Prosecutor'
#     chart_type = 'AreaChart'
#     label_columns = ProsecutorView.label_columns
#     definitions = [
#         {
#             'group' : 'age_today',
#             'formatter': pretty_month_year,
#             "series" : [(aggregate_count,"age_today")]
#         },
#         {
#             'group': 'age_today',
#             'formatter': pretty_year,
#             "series" : [(aggregate_count,"age_today")]
#         }
#     ]
#
#
#
# class PolicemanChartView(GroupByChartView):
#     datamodel = SQLAInterface(Policeman , db.session)
#     chart_title = 'Grouped Policeman by Birth'
#     label_columns = PolicemanView.label_columns
#     chart_type = 'PieChart'
#
#     definitions = [
#         {
#             'group' : 'age_today',
#             "series" : [(aggregate_count,"age_today")]
#         },
#         {
#             'group' : 'gender',
#             "series" : [(aggregate_count,"age_today")]
#         }
#     ]
#
#
# class PolicemanTimeChartView(GroupByChartView):
#     datamodel = SQLAInterface(Policeman , db.session)
#
#     chart_title = 'Grouped Birth Policeman'
#     chart_type = 'AreaChart'
#     label_columns = PolicemanView.label_columns
#     definitions = [
#         {
#             'group' : 'age_today',
#             'formatter': pretty_month_year,
#             "series" : [(aggregate_count,"age_today")]
#         },
#         {
#             'group': 'age_today',
#             'formatter': pretty_year,
#             "series" : [(aggregate_count,"age_today")]
#         }
#     ]
#
#
#
# class JudgeChartView(GroupByChartView):
#     datamodel = SQLAInterface(Judge , db.session)
#     chart_title = 'Grouped Judge by Birth'
#     label_columns = JudgeView.label_columns
#     chart_type = 'PieChart'
#
#     definitions = [
#         {
#             'group' : 'age_today',
#             "series" : [(aggregate_count,"age_today")]
#         },
#         {
#             'group' : 'gender',
#             "series" : [(aggregate_count,"age_today")]
#         }
#     ]
#
#
# class JudgeTimeChartView(GroupByChartView):
#     datamodel = SQLAInterface(Judge , db.session)
#
#     chart_title = 'Grouped Birth Judge'
#     chart_type = 'AreaChart'
#     label_columns = JudgeView.label_columns
#     definitions = [
#         {
#             'group' : 'age_today',
#             'formatter': pretty_month_year,
#             "series" : [(aggregate_count,"age_today")]
#         },
#         {
#             'group': 'age_today',
#             'formatter': pretty_year,
#             "series" : [(aggregate_count,"age_today")]
#         }
#     ]
#
#
#
# class DefendantChartView(GroupByChartView):
#     datamodel = SQLAInterface(Defendant , db.session)
#     chart_title = 'Grouped Defendant by Birth'
#     label_columns = DefendantView.label_columns
#     chart_type = 'PieChart'
#
#     definitions = [
#         {
#             'group' : 'age_today',
#             "series" : [(aggregate_count,"age_today")]
#         },
#         {
#             'group' : 'gender',
#             "series" : [(aggregate_count,"age_today")]
#         }
#     ]
#
#
# class DefendantTimeChartView(GroupByChartView):
#     datamodel = SQLAInterface(Defendant , db.session)
#
#     chart_title = 'Grouped Birth Defendant'
#     chart_type = 'AreaChart'
#     label_columns = DefendantView.label_columns
#     definitions = [
#         {
#             'group' : 'age_today',
#             'formatter': pretty_month_year,
#             "series" : [(aggregate_count,"age_today")]
#         },
#         {
#             'group': 'age_today',
#             'formatter': pretty_year,
#             "series" : [(aggregate_count,"age_today")]
#         }
#     ]


# How to create a MasterDetailView
 
#class DetailView(ModelView):
#    datamodel = SQLAInterface(DetailTable, db.session)
 
#class MasterView(MasterDetailView):
#    datamodel = SQLAInterface(MasterTable, db.session)
#    related_views = [DetailView]
 
 
# How to create a MultipleView
#class MultipleViewsExp(MultipleView):
#    views = [GroupModelView, ContactModelView]
 
#View Registration
db.create_all()
fill_gender()
 
appbuilder.add_view(AgeRatingView(), "AgeRatings", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(CusDvdView(), "CusDvds", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(CustomerView(), "Customers", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(DvdView(), "Dvds", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(GenreView(), "Genres", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(MovieView(), "Movies", icon="fa-folder-open-o", category="Setup") 

appbuilder.add_view(ShelveView(), "Shelves", icon="fa-folder-open-o", category="Setup") 

 
 
appbuilder.add_view(AttorneyChartView(), 'Attorney Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(AttorneyTimeChartView(), 'Attorney Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(PlaintiffChartView(), 'Plaintiff Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(PlaintiffTimeChartView(), 'Plaintiff Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(ObserverChartView(), 'Observer Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(ObserverTimeChartView(), 'Observer Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(SuretyChartView(), 'Surety Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(SuretyTimeChartView(), 'Surety Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(ProsecutorChartView(), 'Prosecutor Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(ProsecutorTimeChartView(), 'Prosecutor Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(PolicemanChartView(), 'Policeman Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(PolicemanTimeChartView(), 'Policeman Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(JudgeChartView(), 'Judge Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(JudgeTimeChartView(), 'Judge Time Chart', icon='fa-dashboard', category='Reports')
 
appbuilder.add_view(DefendantChartView(), 'Defendant Age Chart', icon='fa-dashboard', category='Reports')
appbuilder.add_view(DefendantTimeChartView(), 'Defendant Time Chart', icon='fa-dashboard', category='Reports')
 
#appbuilder.add_separator("Setup")
#appbuilder.add_separator("My Views")
#appbuilder.add_link(name, href, icon='', label='', category='', category_icon='', category_label='', baseview=None)
