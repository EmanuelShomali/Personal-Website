from django.urls import path
from . import views    # the '.' refrences the current directory

# this urls.py file belongs to the app named 'Primary'
urlpatterns = [
    path("", views.index, name="index"),
    # When you visit http://127.0.0.1:8000/Primary/ - it will 
    # run the 'index' view/function (as defined in 'views.py'), 
    # because the first parameter of path is empty + there is nothing 
    # after the forward-slash(/) that follows Primary.
    
    path("resume/", views.resume, name="resume"),

    path("<str:name>/", views.greet, name="greet"),
    # If anything proceeds the forward-slash, it will 
    # be accepted as a string input to the 'greet' view/
    # function. You can include multiple parameters which 
    # are delimited by forward-slashes in the url, you 
    # just have to modify the first parameter of the path

]