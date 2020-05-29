from rest_framework.response import Response
from rest_framework.decorators import api_view
import json
import requests
# Create your views here.

@api_view(['POST'])
def api_reader(request):
    try:
        context = {'text': 'error', 'code': 400}
        url = request.POST.get('url', None)
        payload = {
            'apikey': '7309e56a9788957',
            'language': 'ara',
            'isOverlayRequired': True,
            'base64image': url
        }
        ocr_host = 'https://api.ocr.space/parse/image'
        res = requests.post(ocr_host, data=payload)
        if res and res.content:
            content = json.loads(res.content.decode())['ParsedResults'][0]['TextOverlay']
            lines = [line['LineText'] for line in content['Lines']]
            text = '/n'.join(lines)
          

            data_speech = {
                'msg' : text,
                'lang': 'Zeina',
                'source': 'ttsmp3'
            }
            t2s_host = 'https://ttsmp3.com/makemp3_new.php'
            result = requests.post(t2s_host, data=data_speech)
            url_speech = json.loads(result.content.decode())['URL']
            context['code'] = 200
            context['text'] = url_speech

            return Response(context)
        else:
            context['code'] = 200
            context['text'] = 'https://ttsmp3.com/created_mp3/59f8086a0b33632ff2d51c2a9030668f.mp3'
            return Response(context)
    except:
        context['code'] = 200
        context['text'] = 'https://ttsmp3.com/created_mp3/cd9361829efaa1288749c1595fe6dfa2.mp3'
        return Response(context)
