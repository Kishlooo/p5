from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('trail/',views.trial,name="Trial"),
    path('profile/',views.profile,name="profile"),
    path('signup/',views.signup,name="signup"),
    path('get_demo/',views.get_demo,name="get_demo"),
    path('post_demo/',views.post_demo,name="post_demo"),
    path('register/',views.register,name="register"),
    path('multi/',views.multi,name="multiselect"),
    path('img/',views.img_upld,name="img"),
    path('img_dipslay/',views.img_display,name="img_disp"),
    path('imgs/',views.imgs_upld,name="imgs"),
    path('imgs_diplay/',views.imgs_display,name="imgs_disp"),
    path('builtin/',views.builtin,name="builtin"),
]