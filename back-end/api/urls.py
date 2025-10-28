from django.urls import path
from .views import CursoListAPIView, VagaListAPIView, SalvarVagaAPIView, VagasSalvasAPIView, CadastroUsuarioAPIView, AlertaListCreateAPIView, RemoverVagaAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path("cursos/", CursoListAPIView.as_view()),
    path("vagas/", VagaListAPIView.as_view()),
    path("vagas/<int:id>/salvar/", SalvarVagaAPIView.as_view()),
    path("vagas/salvas/", VagasSalvasAPIView.as_view()),
    path("vagas/<int:id>/remover/", RemoverVagaAPIView.as_view()),
    path("cadastro/",  CadastroUsuarioAPIView.as_view()),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("alertas/", AlertaListCreateAPIView.as_view())
]