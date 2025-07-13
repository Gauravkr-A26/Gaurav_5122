from django.shortcuts import render  # Import render for rendering templates (not used here)
from rest_framework.views import APIView  # Import APIView for class-based API views
from django.http import JsonResponse  # Import JsonResponse to return JSON responses
from rest_framework import status  # Import status codes for HTTP responses
from .models import *  # Import all models from the current app
from .serlizers import *  # Import all serializers from the current app

# Create your views here.

class GAURAV_lmsSignupUser(APIView):  # API view for user signup
    def post(self, request):  # Handle POST requests
        userdata = GAURAV_lmsSignupSerializer(data=request.data)  # Deserialize and validate incoming data
        if userdata.is_valid():  # If data is valid
            GAURAV_lmsUser.objects.create(**userdata.validated_data)  # Create a new user with validated data
            return JsonResponse({"message": "User created successfully"}, status=status.HTTP_201_CREATED)  # Return success GAURAV_response
        return JsonResponse(userdata.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if data is invalid

class GAURAV_lmsGetUserDetails(APIView):  # API view to get all user details
    def get(self, request):  # Handle GET requests
        result = list(GAURAV_lmsUser.objects.all().values())  # Get all users as a list of dictionaries
        return JsonResponse(result, safe=False, status=status.HTTP_200_OK)  # Return user data as JSON




class GAURAV_lmsUpdateEmail(APIView):  # API view to update user email
    def put(self, request):
        userdata = GAURAV_lmsUpdateEmailSerializer(data=request.data)
        if userdata.is_valid():
            email = userdata.data["email"]
            number = userdata.data["number"]
            GAURAV_lmsUser.objects.filter(number=number).update(email=email)
            message = {"message": "Email updated successfully"}
            return JsonResponse(message, status=status.HTTP_200_OK)
        return JsonResponse(userdata.errors, status=status.HTTP_400_BAD_REQUEST)
            
    
class GAURAV_lmsDeleteUser(APIView):  # API view to delete a user
    def delete(self, request, number):
        GAURAV_lmsUser.objects.filter(number=number).delete()
        message = {"message": "User deleted successfully"}
        return JsonResponse(message, status=status.HTTP_204_NO_CONTENT)  # Return success message after deletion
    
