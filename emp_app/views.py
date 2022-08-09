from ast import Delete
from genericpath import exists
from logging import exception
from re import I
from urllib import response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee,Role,Department
from .serializers import Departmentserializer,Employeeserializer,Roleserializer
from rest_framework.views import APIView
from emp_app import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class Updateemployeeview(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated ]

    def put(self,request,id):
        #print(request)
        #id = request.query_params["id"]
        employee_object = Employee.objects.get(id=id)
        data=request.data
        serializer=Employeeserializer(employee_object,data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": True, "response": "Data updated succesfully"},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": False, "response": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    def delete(self,request,id):
        try:
            employee=Employee.objects.get(id=id)
            employee.delete()
            return Response("Employee Deleted succesfully.")
        except:
            return Response("Employee does not exist.")


    def get(self, request,id):
        
        try:
            employee = Employee.objects.get(id=id)
            serializer = Employeeserializer(employee)
        except:
            if id :
                return Response("EMPTY DATA!!")
            else:
                return Response("Enter the valid id!")
            

        return Response(serializer.data)





class Employeeview(APIView):

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated ]

    def get(self, request):
        emp = Employee.objects.all()
        serializer = Employeeserializer(emp, many=True)
        return Response(
            {"status": True, "response": serializer.data}, status=status.HTTP_200_OK
        ) 

    def post(self, request):
        serializer = Employeeserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": True, "response": "Employee created successfully."},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": False, "response": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

    

    

    





#class Filteremployee(APIView):
#    authentication_classes=[JWTAuthentication]
#    permission_classes=[IsAuthenticated ]

    # def get(self,request):
        
    #     employee_id=request.data.get("id=id",False)
    #     try:
    #         employee=Employee.objects.get(id=employee_id)
    #         serializer = Employeeserializer(employee)
    #         return Response({"status": True, "response": serializer.data}, status=status.HTTP_200_OK) 
    #     except:
    #         

    


    # def get(self,request):
    #     try:
    #         id=request.query_params["id"]
    #         employee=Employee.objects.get(id=id)
    #         serializer=Employeeserializer(employee)
    #         return Response({"status": True, "response": serializer.data}, status=status.HTTP_200_OK) 
    #     except:
    #         return Response("Enter the vaild id.")

                

class Departmentemployee(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated ]

    def get(self,request):
        dept = Department.objects.all()
        serializer = Departmentserializer(dept, many=True)
        return Response(
            {"status": True, "response": serializer.data}, status=status.HTTP_200_OK
        )

    def post(self,request):
        serializer = Departmentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": True, "response": "Data sended successfully."},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": False, "response": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )

        

class Roleemployee(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated ]
    def get(self,request):
        role_emp = Role.objects.all()
        serializer = Roleserializer(role_emp, many=True)
        return Response(
            {"status": True, "response": serializer.data}, status=status.HTTP_200_OK
        )

    def post(self,request):
        serializer = Roleserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"status": True, "response": "Data sended successfully."},
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(
                {"status": False, "response": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
