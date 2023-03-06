from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .postgres_conn import insert_lines


@api_view(['POST'])
def gravar_banco(request):

    try:
        data = JSONParser().parse(request)
        insert_lines(data)
        confirmacao = 'Dado inserido com sucesso'
        return JsonResponse(f'{confirmacao}', status=201, safe=False)
    except Exception as ex:
        response = {
             "error": str(ex.args[0])
        }
        return JsonResponse(response, status=400)

