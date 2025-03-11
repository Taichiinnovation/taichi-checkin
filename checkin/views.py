from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .firebase_config import firebase_config
import pyrebase
import time

# 初始化Firebase
firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

@csrf_exempt  # 避免CSRF錯誤
def checkin(request):
    if request.method == "POST":
        user_id = request.POST.get("user_id")
        # 寫入Firebase
        db.child("room1").child("checkins").child(user_id).set({
            "name": f"學員{user_id}",
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S")
        })
        return render(request, "checkin.html", {"message": f"學員{user_id}簽到成功"})
    return render(request, "checkin.html")

def coach(request):
    return render(request, "coach.html")