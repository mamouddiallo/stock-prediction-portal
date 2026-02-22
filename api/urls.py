from django.urls import path
from accounts import views as UserViews

urlpatterns = [

    # ENDPOINTAPI
    path('register/', UserViews.RegisterView.as_view()),


]