from djangocrud.api import views
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'users/',views.usersViewSet)
#router.register(r'users/(?P&lt;pk&gt;[0-9]+)$',views.usersViewSet)





