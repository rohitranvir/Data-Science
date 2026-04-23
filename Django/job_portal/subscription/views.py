from django.shortcuts import render
import uuid
# Create your views here.
from django.db import transaction
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permission import IsAuthenticated
4rr