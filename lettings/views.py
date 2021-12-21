from django.shortcuts import render
from .models import Letting

""" Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
Sed non placerat massa. Integer est nunc, pulvinar a tempor et, bibendum id\n
arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere\n
cubilia curae; Cras eget scelerisque"""


def index(request):
    lettings_list = Letting.objects.all()
    context = {'lettings_list': lettings_list}
    return render(request, 'lettings_index.html', context)


""" Cras ultricies dignissim purus, vitae hendrerit ex varius non. In accumsan\n
porta nisl id eleifend. Praesent dignissim, odio eu consequat pretium, purus\n
urna vulputate arcu, vitae efficitur lacus justo nec purus. Aenean finibus\n
faucibus lectus at porta. Maecenas auctor, est ut luctus congue, dui enim\n
mattisenim, ac condimentum velit libero in magna. Suspendisse potenti. In\n
tempus a nisi sed laoreet. Suspendisse porta dui eget sem accumsan interdum.\n
Ut quis urna pellentesque justo mattis ullamcorper ac non tellus. In tristique\n
mauris eu velit fermentum, tempus pharetra est luctus. Vivamus consequat\n
aliquam libero, eget bibendum lorem. Sed non dolor risus. Mauris condimentum\n
auctor elementum. Donec quis nisi ligula. Integer vehicula tincidunt enim, ac\n
lacinia augue pulvinar sit amet."""


def letting(request, letting_id):
    letting = Letting.objects.get(id=letting_id)
    context = {
        'title': letting.title,
        'address': letting.address,
    }
    return render(request, 'letting.html', context)
