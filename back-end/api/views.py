from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Curso, Vaga, Usuario, Alerta
from .serializers import CursoSerializer, VagaSerializer, UsuarioSerializer, AlertaSerializer


# Create your views here.
class CursoListAPIView(generics.ListAPIView):
    # Busca todos os cursos
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class VagaListAPIView(generics.ListAPIView):
    # Busca todas as vagas
    queryset = Vaga.objects.all()
    serializer_class = VagaSerializer


class CadastroUsuarioAPIView(generics.CreateAPIView):
    # Busca todos os usuarios
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class AlertaListCreateAPIView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Alerta.objects.filter(usuario=self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(usuario=self.request.user)
    
    serializer_class = AlertaSerializer


class SalvarVagaAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, id):
        # Busca a vaga pelo id
        vaga = Vaga.objects.get(id=id);

        # Adiciona o usuário logado à lista
        vaga.usuarios_que_salvaram.add(request.user)

        return Response({"detalhe": "Vaga salva com sucesso"}, status=status.HTTP_200_OK)


class VagasSalvasAPIView(generics.ListAPIView):
    serializer_class = VagaSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self, ):
        return Vaga.objects.filter(usuarios_que_salvaram=self.request.user)
    

class RemoverVagaAPIView(APIView):
    serializer_class = VagaSerializer

    permission_classes = [IsAuthenticated]

    def delete(self, request, id):
        # Busca a vaga de acordo com o id
        vaga = Vaga.objects.get(id=id)

        # Remove o usuario da lista de salvos
        vaga.usuarios_que_salvaram.remove(request.user)

        return Response({"detalhe": "Vaga removida com sucesso"}, status=status.HTTP_200_OK)
