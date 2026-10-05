from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from movies.models import Movie
from movies.serializer import MovieSerializer
from rest_framework import status

# Create your views here.

# API View for reading all record
# class MovieList(APIView):
#     def get(self,request):
#         m=Movie.objects.all()
#         serializer_instance=MovieSerializer(m,many=True)
#         return Response(serializer_instance.data)
#
# # API View for creating new record
# class MovieCreate(APIView):
#     def post(self,request):
#         form_data=request.data
#         serializer_instance=MovieSerializer(data=form_data)
#         if serializer_instance.is_valid():
#
#             # cleaned_data=serializer_instance.validated_data   # Data after validation
#             # title=cleaned_data['title']
#
#             serializer_instance.save()
#             return Response(serializer_instance.data)
#         else:
#             return Response(serializer_instance.errors)

# API View for reading all record and creating new record in single class
class MovieListCreate(APIView):
    def get(self,request):
        m=Movie.objects.all()
        serializer_instance=MovieSerializer(m,many=True)
        return Response(serializer_instance.data,status=status.HTTP_200_OK)

    def post(self,request):
        form_data=request.data
        serializer_instance=MovieSerializer(data=form_data)
        if serializer_instance.is_valid():

            # cleaned_data=serializer_instance.validated_data   # Data after validation
            # title=cleaned_data['title']

            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

# API View for reading specific record,full update specific record,partial update specific record,delete a record in one class
class MovieRetrieveUpdateDelete(APIView):

# API View for retrieving specific record
    def get(self,request,id):
        m=get_object_or_404(Movie,id=id)
        serializer_instance=MovieSerializer(m)
        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)

# API View for full update specific record
    def put(self,request,id):
        form_data=request.data
        m=Movie.objects.get(id=id)
        serializer_instance=MovieSerializer(m,data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

# API View for partial update specific record
    def patch(self,request,id):
        form_data=request.data
        m=Movie.objects.get(id=id)
        serializer_instance=MovieSerializer(m,data=form_data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

# API View for deleting a record
    def delete(self,request,id):
        m=get_object_or_404(Movie,id=id)
        m.delete()
        return Response({'Message': 'Movie Record Deleted'},status=status.HTTP_204_NO_CONTENT)
