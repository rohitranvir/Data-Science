from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('exam/',views.exams_view),
    path('attedence/',views.attedence_view),
    path('fees',views.fees_view),

]