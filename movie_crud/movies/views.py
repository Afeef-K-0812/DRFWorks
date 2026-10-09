from django.http.response import JsonResponse
from django.shortcuts import render,get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from movies.models import Movie
from movies.serializer import MovieSerializer, UserSerializer
from rest_framework import status
from rest_framework import mixins,generics
from rest_framework import viewsets
from django.db.models import Q

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
# class MovieListCreate(APIView):
#     def get(self,request):
#         m=Movie.objects.all()
#         serializer_instance=MovieSerializer(m,many=True)
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)
#
#     def post(self,request):
#         form_data=request.data
#         serializer_instance=MovieSerializer(data=form_data)
#         if serializer_instance.is_valid():
#
#             # cleaned_data=serializer_instance.validated_data   # Data after validation
#             # title=cleaned_data['title']
#
#             serializer_instance.save()
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)


# API View for reading specific record,full update specific record,partial update specific record,delete a record in one class
# class MovieRetrieveUpdateDelete(APIView):
#
# # API View for retrieving specific record
#     def get(self,request,id):
#         m=get_object_or_404(Movie,id=id)
#         serializer_instance=MovieSerializer(m)
#         return Response(data=serializer_instance.data,status=status.HTTP_200_OK)
#
# # API View for full update specific record
#     def put(self,request,id):
#         form_data=request.data
#         m=Movie.objects.get(id=id)
#         serializer_instance=MovieSerializer(m,data=form_data)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
#
# # API View for partial update specific record
#     def patch(self,request,id):
#         form_data=request.data
#         m=Movie.objects.get(id=id)
#         serializer_instance=MovieSerializer(m,data=form_data,partial=True)
#         if serializer_instance.is_valid():
#             serializer_instance.save()
#             return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)
#
# # API View for deleting a record
#     def delete(self,request,id):
#         m=get_object_or_404(Movie,id=id)
#         m.delete()
#         return Response({'Message': 'Movie Record Deleted'},status=status.HTTP_204_NO_CONTENT)


# API View using mixins class
# class MovieListCreate(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
#     queryset=Movie.objects.all()
#     serializer_class=MovieSerializer
#
#     def get(self,request):
#         return self.list(request)
#
#     def post(self,request):
#         return self.create(request)
#
# class MovieRetrieveUpdateDelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
#     def get(self,request,pk):
#         return self.retrieve(request,pk)
#
#     def put(self,request,pk):
#         return self.update(request,pk)
#
#     def patch(self,request,pk):
#         return self.partial_update(request,pk)
#
#     def delete(self,request,pk):
#         return self.destroy(request,pk)


# API View using generics class
# class MovieListCreate(generics.ListCreateAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer
#
# class MovieRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Movie.objects.all()
#     serializer_class = MovieSerializer


# API View using Viewsets class
from rest_framework.permissions import IsAuthenticated
class MovieView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated,]
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# API View for Search
# class SearchAPIView(APIView):
#     def get(self,request):
#         data=self.request.query_params.get('search')    # Fetch data coming from request url
#         m=Movie.objects.filter(Q(title__icontains=data) | Q(director__icontains=data) | Q(language__icontains=data))    # Filter movie record having title matching with data
#         if not m.exists():
#             return Response({'Message':'No Record Found'},status=status.HTTP_200_OK)
#         serializer_instance=MovieSerializer(m,many=True)    # Converts the queryset into python native type using serializer class
#         return Response(serializer_instance.data,status=status.HTTP_200_OK)     # Return response as json using Response class

from rest_framework.filters import SearchFilter
class SearchAPIView(generics.GenericAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter]
    search_fields=['title','director','language']


# API View for User registration
class RegisterAPIView(APIView):
    def post(self,request):
        form_data=request.data
        serializer_instance=UserSerializer(data=form_data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

# from django.contrib.auth import authenticate
# from rest_framework.authtoken.models import Token
# # API View for Authentication - Obtain authentication Token
# class obtain_auth_token(APIView):
#     def post(self,request):
#         data=request.data
#         u=data['username']
#         p=data['password']
#         user=authenticate(username=u,password=p)    # authenicate() returns user object if a user matching with username nd password exist else return none
#         if user:
#             token,created=Token.objects.get_or_create(user=user)    # get_or_create() function returns token object and create flag if already record exists in Token table Created flag returns False Else it returns True. If we use create() it only returns token object but get_or_create() returns
#             return JsonResponse({'Token':token.key})
#         else:
#             return JsonResponse({'Message':'Invalid User Credentials'})


# API View for Logout
class Logout(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        print(self.request.user)
        self.request.user.auth_token.delete()
        return Response({'Message':'Logged out Successfully'})