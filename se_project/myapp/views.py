from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('menu')  # เปลี่ยนเส้นทางไปหน้าเมนู
        else:
            return render(request, 'login.html', {'error_message': 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง'})

    return render(request, 'login.html')

# หน้าเลือกเมนู
def menu(request):
    return render(request, 'menu.html')