import string
import random
from django.http import JsonResponse
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from .models import RandomKey, AvailableKey

# Create your views here.
def generate_key(request):
    generated_key = RandomKey.objects.create()
    available_key = AvailableKey()
    generated_key.api_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k = 39-len(str(generated_key.id)))) + "+" + str(generated_key.id)
    generated_key.save()
    available_key.key = generated_key
    available_key.save()
    api_data = {"Result":"API key generated successfully"}
    return JsonResponse(api_data, status=201)

def serve_key(request):
    if(AvailableKey.objects.count() > 0):
        available_key = AvailableKey.objects.last()
        key_id = available_key.key.api_key
        available_key.key.is_blocked = True
        available_key.key.save()
        available_key.delete()
    else:
        api_data = {"Result":"No API key available"}
        return JsonResponse(api_data, status=404)
    api_data = {"Result":"API key available",
                "api_key":key_id,
                }
    return JsonResponse(api_data, status=200)

@csrf_exempt
def unblock_key(request):
    if(request.method == "POST"):
        unique_key = request.POST.get("user_key")
    key_id = unique_key.split('+')[1]
    try:
        random_key = RandomKey.objects.get(id=key_id)
        random_key.is_blocked = False
        random_key.save()
        try:
            available_key = AvailableKey.objects.get(key=key_id)
        except AvailableKey.DoesNotExist:
            available_key = AvailableKey()
            available_key.key = random_key
            available_key.save()
    except:
        api_data = {"Result":"API key doesn't exist"}
        return JsonResponse(api_data, status=404)
    api_data = {"Result":"API key unblocked successfully"}
    return JsonResponse(api_data, status=200)

@csrf_exempt
def delete_key(request):
    if(request.method == "POST"):
        unique_key = request.POST.get("user_key")
    key_id = unique_key.split('+')[1]
    try:
        random_key = RandomKey.objects.get(id=key_id)
        random_key.is_deleted = True
        random_key.save()
        try:
            available_key = AvailableKey.objects.get(key=key_id)
            available_key.delete()
        except AvailableKey.DoesNotExist:
            pass
    except:
        api_data = {"Result":"API key doesn't exist"}
        return JsonResponse(api_data, status=404)
    api_data = {"Result":"API key deleted successfully"}
    return JsonResponse(api_data, status=200)

@csrf_exempt
def keep_alive(request):
    if(request.method == "POST"):
        unique_key = request.POST.get("user_key")
    key_id = unique_key.split('+')[1]
    try:
        random_key = RandomKey.objects.get(id=key_id)
        random_key.last_alive_call = datetime.now()
        random_key.save()
    except:
        api_data = {"Result":"API key doesn't exist"}
        return JsonResponse(api_data, status=404)
    api_data = {"Result":"API key will be alive for next 5 minutes"}
    return JsonResponse(api_data, status=200)
