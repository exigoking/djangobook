from django.conf.urls import patterns, url
from djangobook import views
from simplenation import views
from simplenation.views import PasswordResetRequestView, PasswordResetConfirmView

urlpatterns = patterns('',
	url(r'^$', views.index, name = 'index'),
	url(r'^term/(?P<term_name_slug>[\w\-]+)/$', views.term, name = 'term'),
	url(r'^search/', views.search, name = 'search'),
	url(r'^registration_form/$', views.register, name='register'),
	url(r'^account_deletion/(?P<account_deletion_key>\w+)/$', views.account_deletion, name='account_deletion'),
	url(r'^signin/$', views.user_login, name='signin'),
	url(r'^signout/$', views.user_logout, name='signout'),
	url(r'^add_term/$', views.add_term, name='add_term'),
	url(r'^profile/(?P<profile_name_slug>[\w\-]+)/$', views.profile, name = 'profile'),
	url(r'^profile/(?P<profile_name_slug>[\w\-]+)/edit_profile/$', views.edit_profile, name='edit_profile'),
	#url(r'^term/(?P<term_name_slug>[\w\-]+)/edit_exp/(?P<explanation_id>[\w\-]+)/$', views.edit_exp, name = 'edit_exp'),
	url(r'^like_explanation/$', views.like_explanation, name='like_explanation'),
	url(r'^edit_exp/$', views.edit_exp, name='edit_exp'),
	url(r'^add_tags_to_term/$', views.add_tags_to_term, name='add_tags_to_term'),
	url(r'^tag_select/$', views.tag_select, name='tag_select'),
	url(r'^search_tags/$', views.search_tags, name='search_tags'),
	url(r'^reset_password/$', PasswordResetRequestView.as_view(), name="reset_password"),
	url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
	url(r'^password_sent_confirmation/$', views.password_sent_confirmation, name="password_sent_confirmation"),
	url(r'^report_explanation/$', views.report_explanation, name='report_explanation'),

)
