from django.shortcuts import render
#from .models import Profile, Letting, Address
from lettings.models import Letting, Address
#from .models import Profile
from profiles.models import Profile

""" Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque molestie\n
quam lobortis leo consectetur ullamcorper non id est. Praesent dictum, nulla\n
eget feugiat sagittis, sem mi convallis eros, vitae dapibus nisi lorem dapibus\n
sem. Maecenas pharetra purus ipsum, eget consequat ipsum lobortis quis.\n
Phasellus eleifend ex auctor venenatis tempus. Aliquam vitae erat ac orci\n
placerat luctus. Nullam elementum urna nisi, pellentesque iaculis enim cursus\n
in. Praesent volutpat porttitor magna, non finibus neque cursus id."""


def index(request):
    return render(request, 'index.html')


""" Aenean leo magna, vestibulum et tincidunt fermentum, consectetur quis velit.
Sed non placerat massa. Integer est nunc, pulvinar a tempor et, bibendum id\n
arcu. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere\n
cubilia curae; Cras eget scelerisque"""


def lettings_index(request):
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


""" Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed\n
consequat libero pulvinar eget. Fusc faucibus, urna quis auctor pharetra,\n
massa dolor cursus neque, quis dictum lacus d"""


def profiles_index(request):
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles_index.html', context)


"""Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet\n
neque quis, pellentesque dui. Nullam facilisis pharetra vulputate. Sed\n
tincidunt, dolor id facilisis fringilla, eros leo tristique lacus, it. Nam\n
aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et\n
netus et males"""


def profile(request, username):
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profile.html', context)
