from django.shortcuts import render


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
