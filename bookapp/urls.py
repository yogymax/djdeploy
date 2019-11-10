from rest_framework.routers import SimpleRouter
from bookapp.views import BookOperations
simpleRouter = SimpleRouter()
simpleRouter.register('books',BookOperations)
urlpatterns=simpleRouter.urls