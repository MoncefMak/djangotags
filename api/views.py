from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from api.serializers import TagSerializer
from tags.models import Tag


class TagsPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = 1000

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data['pages'] = self.page.paginator.num_pages
        return response

class TagsViewset(ModelViewSet):
    serializer_class = TagSerializer
    queryset = Tag.objects.all()
    pagination_class = TagsPagination




