from json import loads
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.db.models import Model
from rest_framework.views import APIView
from rest_framework.response import Response
from employees.models import Employee
from employees.serializers import EmployeeSerializer
from rest_framework import status


# Create your views here.

# API View for Showing All Employee records
class EmployeeList(APIView):
    def get(self,request):
        e=Employee.objects.all()                            # Read all records from Employee table (Query set)
        serializer_instance=EmployeeSerializer(e,many=True) # EmployeeSerializer converts query set into python native type, query set contains more than one record so we use many=True
        return Response(data=serializer_instance.data,status=status.HTTP_200_OK)      # Sends python native data as json using Response class

# API View for Creating a New Employee record
class EmployeeCreate(APIView):
    def post(self,request):         # View receives data as request.data (client side data-python native type)
        serializer_instance=EmployeeSerializer(data=request.data)   # Calls serializer class for deserialization, here we pass request.data as argument
        if serializer_instance.is_valid():
            serializer_instance.save()      # After validation serializer saves data as model object inside data base table
           # return Response({'Message':'Data Inserted'})
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    # Django View
        # data = request.data  # Python native type data or dictionary
        # data=loads(request.body)
        # empid=data['empid']
        # name=data['name']
        # age=data['age']
        # place=data['place']
        # gender=data['gender']
        # joiningdate=data['joiningdate']
        # salary=data['salary']
        # designation=data['designation']
        # e=Employee.objects.create(empid=empid,name=name,age=age,place=place,gender=gender,joiningdate=joiningdate,salary=salary,designation=designation)
        # e.save()
        # e=Employee.objects.create(**data)
        # e.save()
        # return Response({'Message': 'Employee Data Inserted'})

# API View for Particular Employee record
class EmployeeDetail(APIView):
    def get(self,request,i):
        # e=Employee.objects.get(id=i)
        e=get_object_or_404(Employee,id=i)
        serializer_instance=EmployeeSerializer(e)
        return Response(data=serializer_instance.data)

# API View for Full Update of Particular Employee record
class EmployeeFullUpdate(APIView):
    def put(self,request,i):
        e=get_object_or_404(Employee,id=i)
        serializer_instance=EmployeeSerializer(e,request.data)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_instance.errors,status=status.HTTP_400_BAD_REQUEST)

    # Django View
        # data=request.data
        # try:
        #     e=Employee.objects.get(id=i)
        #     e.empid=data['empid']
        #     e.name=data['name']
        #     e.age=data['age']
        #     e.place=data['place']
        #     e.gender=data['gender']
        #     e.joiningdate=data['joiningdate']
        #     e.salary=data['salary']
        #     e.designation=data['designation']
        #     e.save()
        #
        #     return Response({'Message':'Employee Details Updated'})
        # except:
        #     return Response({'Message':'No Employee Record'})

# API View for Partial Update of particular Employee
class EmployeePartialUpdate(APIView):
    def patch(self,request,i):
        e=get_object_or_404(Employee,id=i)
        serializer_instance=EmployeeSerializer(e,request.data,partial=True)
        if serializer_instance.is_valid():
            serializer_instance.save()
            return Response(serializer_instance.data)
        else:
            return Response(serializer_instance.errors)

    # Django View
        # data=request.data
        # try:
        #     e=Employee.objects.get(id=i)
        #     if 'empid' in data:
        #         e.empid=data['empid']
        #     if 'name' in data:
        #         e.name=data['name']
        #     if 'age' in data:
        #         e.age=data['age']
        #     if 'place' in data:
        #         e.place=data['place']
        #     if 'marks' in data:
        #         e.gender=data['gender']
        #     if 'joiningdate' in data:
        #         e.joiningdate=data['joiningdate']
        #     if 'salary' in data:
        #         e.salary=data['salary']
        #     if 'designation' in data:
        #         e.designation=data['designation']
        #     e.save()
        #     return Response({'Message':'Employee Data Updated Partially'})
        # except:
        #     return Response({'Message':'No Employee Record'})

# API View for Deleting  specific Employee record
class EmployeeDelete(APIView):
    def delete(self,request,i):
        e=get_object_or_404(Employee,id=i)
        e.delete()
        return Response({'Message':'Employee Record Deleted'})
