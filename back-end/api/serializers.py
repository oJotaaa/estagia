# api/serializers.py
from rest_framework import serializers
from .models import Usuario, Habilidade, Vaga, Alerta, Curso


class HabilidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habilidade
        fields = ['id', 'name']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = '__all__'


class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'
        extra_kwargs = {
            'usuario': {'read_only': True}
        }


class UsuarioSerializer(serializers.ModelSerializer):
    habilidades = serializers.ListField(
        child=serializers.CharField(), write_only=True, required=False
    )

    class Meta:
        model = Usuario
        fields = ["username", "email", "password", "habilidades"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Separar os dados relacionados
        habilidades_data = validated_data.pop('habilidades', [])

        # Criar o usuário e criptografar a senha
        usuario = Usuario.objects.create_user(**validated_data)

        # Criar/ligar habilidades
        for nome_habilidade in habilidades_data:
            habilidade_obj, created = Habilidade.objects.get_or_create(nome=nome_habilidade)
            usuario.habilidades.add(habilidade_obj)

        return usuario