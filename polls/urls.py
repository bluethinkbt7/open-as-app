from django.conf.urls import url
from polls import views


urlpatterns = [
    url(r'^$', views.upload, name='uplink'),
    url(r'^import/', views.import_data, name="import"),
    url(r'^handson_view/', views.handson_table, name="handson_view"),
    # survey_result
    url('^survey_result/',
        views.survey_result, name='survey_result'),
    url(r'^import_sheet_using_isave/',
        views.import_sheet_using_isave_to_database),
]
