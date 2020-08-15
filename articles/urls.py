from rest_framework import routers
from .api import PostViewSet, CommentViewSet

app_name = "articles"
router = routers.DefaultRouter()
router.register("api/post", PostViewSet, "post")
router.register("api/comment", CommentViewSet, "comment")

urlpatterns = router.urls
