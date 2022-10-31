from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from fliter_api.models import Filter_data
from fliter_api.seralizers import FileUploadSerializer,SaveFileSerializer
import io, csv, pandas as pd
from django.db import connection


"""
   Description: Here we are upload csv file filtering data based on sesiion_init filter and save the data to the db
"""

class UploadFileView(generics.CreateAPIView):
    serializer_class=FileUploadSerializer
    def post(self,request,*args,**kwargs):
        seralizer=self.get_serializer(data=request.data)
        seralizer.is_valid(raise_exception=True)
        file=seralizer.validated_data['file']
        #read csv fileer
        data=pd.read_csv(file)
        filterinfDataframe = data[(data['action'] == 'SESSION_INIT')]
        filterinfDataframe.drop_duplicates('shopper_id', keep='last')
        for index, row in filterinfDataframe.iterrows():
            users = Filter_data(action=row['action'], publisher_id=row['publisher_id'],
                                timestamp_at=row['time_stamp'],
                                shopper_id=row['shopper_id']
                                )
            users.save()
        return Response({"status": "success"},
                        status.HTTP_201_CREATED)


class GetData(APIView):
    '''
    Hello post brand name,start_time,end_time
    '''
    def post(self, request):

        brand = request.data.get('brand')
        start_time = request.data.get('start_time')
        print(start_time)
        end_times = request.data.get('end_time')
        print(end_times)
        print(type(end_times))
        items={}
        try:
            if brand!=None and start_time!=None:
                cursor = connection.cursor()
                cursor.execute(f'''select * from fliter_filter_data where timestamp_at between '{start_time}' and '{end_times}' and publisher_id='{brand}';''')
                list_data = cursor.fetchall()
                items['filterdata'] = list_data
                items['success'] = True
                items['message'] = "success"
                return Response(items, status=status.HTTP_200_OK)
        except:
            items['success'] = False
            items['message'] = "data not available in database"
            return Response(items, status=status.HTTP_404_NOT_FOUND)

