from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from .postgres_conn import insert_lines, conferir_email
from django.views.decorators.csrf import csrf_exempt
from . import valida_token as vt 


@csrf_exempt
@api_view(['POST'])
def gravar_banco(request):
    
    
    token = request.headers['Authorization']
    data = request.data
    email = request.headers['email']
    contagem_email = conferir_email(data['email'])
    
    if contagem_email > 0:
        retorno = {
            "FL_STATUS": False,
            "erro": "Esse email ja existe na base, insira outro"
        }
        return JsonResponse(retorno, status=400)
    
    else:
        
        status = vt.valida_token_navegacao(email, token, 'nav')
        status = status.json()
        if status['FL_STATUS'] == False:
            resposta = {
                "msg": "token expirado",
                "FL_STATUS": False        
                }
            return JsonResponse(resposta, status=400, safe=False)
    
        try:
            #data = JSONParser().parse(request)
            insert_lines(data)
    
            return JsonResponse({"FL_STATUS": True}, status=201, safe=False)
        
        except Exception as ex:
            response = {
                 "FL_STATUS": False,
                 "error": str(ex.args[0]),
            }
            return JsonResponse(response, status=400, safe=False)

