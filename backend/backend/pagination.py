from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

DEFAULT_PAGE = 1
DEFAULT_PAGE_SIZE = 15


class CustomPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'data': data,
            'pagination': {
                # Thanks to https://stackoverflow.com/questions/46626994/
                'last_page': self.page.paginator.num_pages,
                'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
                'rowsNumber': self.page.paginator.count,
                'rowsPerPage': int(self.request.GET.get('size', self.page_size)),
                'sortBy': self.request.query_params.get('ordering', None)
            }
        })

class CategoryPagination(PageNumberPagination):
    page = DEFAULT_PAGE
    page_size = 5
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'data': data,
            'meta': {
                # Thanks to https://stackoverflow.com/questions/46626994/
                'last_page': self.page.paginator.num_pages,
                'page': int(self.request.GET.get('page', DEFAULT_PAGE)),
                'page_size': int(self.request.GET.get('page_size', self.page_size))
            }
        })