# voice_app/views.py
from django.shortcuts import render
from gtts import gTTS
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == "POST":
        text = request.POST.get("text")
        if text:
            tts = gTTS(text)
            filepath = "voice_app/static/audio/voice.mp3"
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            tts.save(filepath)
            return JsonResponse({"audio_url": "/static/audio/voice.mp3"})
    return render(request, "voice_app/index.html")
