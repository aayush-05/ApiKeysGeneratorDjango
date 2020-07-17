from random_keys_generator.celery import app
from datetime import datetime
from keys_api.models import RandomKey, AvailableKey

@app.task
def check_last_alive():
    for key in Randomkey.objects.all():
        if((key.is_blocked==True and key.is_deleted==False) and ((datetime.now()-key.last_alive_call).total_seconds > 300.0):
            key.delete()
