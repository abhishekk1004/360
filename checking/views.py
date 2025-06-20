from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, ImageUploadForm
from django.contrib.auth.decorators import login_required
import os


def home(request):
    return render(request, 'viewer/home.html', {'user': request.user})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! You can now login.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'viewer/register.html', {'form': form})

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                image = form.cleaned_data['image']
                img_dir = os.path.join('media', 'uploads')
                os.makedirs(img_dir, exist_ok=True)
                img_path = os.path.join(img_dir, image.name)
                with open(img_path, 'wb+') as destination:
                    for chunk in image.chunks():
                        destination.write(chunk)
                messages.success(request, 'Image uploaded successfully.')
                return render(request, 'viewer/view360.html', {'image_url': f'/media/uploads/{image.name}'})
            except Exception as e:
                messages.error(request, f"Error generating 360 view: {e}")
    else:
        form = ImageUploadForm()
    return render(request, 'viewer/upload.html', {'form': form})