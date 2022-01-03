from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import status

from jogos_blog.apps.authentication.serializer import UserSerializer, LoginSerializer

User = get_user_model()


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    
    def list(self, request, *args, **kwargs):
        if request.user.id is None:
            return Response(template_name='user_register.html')

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'users': serializer.data}, template_name='users.html')
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            messages.success(request, "Usuário criado com sucesso")
            return redirect('login')
        return Response({'errors': serializer.errors},template_name='user_register.html')
    
    def update(self, request, *args, **kwargs):
        if request.user.id is None:
            return redirect('login')

        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data, template_name='user_detail.html')
    
    def retrieve(self, request, *args, **kwargs):
        if request.user.id is None:
            return redirect('login')

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, template_name='user_detail.html')


class UserLogin(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'user_login.html'

    def get(self, request, format=None):
        if request.user.id is not None:
            return redirect('main')

        return Response(status=status.HTTP_200_OK)


    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'serializer': serializer})

        user = authenticate(username=serializer.data['username'], password=serializer.data['password'])
        if user is not None:
            login(request, user)

            return redirect('main')

        return Response({"error": "Credenciais incorretas"}, status=status.HTTP_400_BAD_REQUEST)


class UserLogout(APIView):
    def post(self, request, format=None):
        if request.user.id is not None:      
            logout(request)

        return redirect('login')


class MainView(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self, request, format=None):
        if request.user.id is None:
            return redirect('login')

        return Response(template_name='main.html')