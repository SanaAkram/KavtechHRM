from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Kavtech/', include('account.urls')),
    path('Kavtech/quiz/', include('quiz.urls')),
    path('Kavtech/dashboard/', include('dashboard.urls'))

]
