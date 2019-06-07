from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from OutlierDetectorApp.OutlierDetector import GetOutlierClass


class GetOutlierView(APIView):

    def get(self, request, *args, **kw):
        get_arg1 = request.GET.get('arg1', None)
        get_out = GetOutlierClass(get_arg1, *args, **kw)
        result = get_out.find_outlier_method1()
        response = Response(result)
        return response

class GetOutlierView2(APIView):
    def get(self, request, *args, **kw):
        get_arg1 = request.GET.get('arg1', None)
        get_out = GetOutlierClass(get_arg1, *args, **kw)
        result = get_out.find_outlier_method2()
        response = Response(result)
        return response
	
