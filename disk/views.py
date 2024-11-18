import requests
from django.shortcuts import render
from django.conf import settings
from django.views.decorators.cache import cache_page
import yadisk

YANDEX_TOKEN = settings.YANDEX_TOKEN

# ----------------- РЕАЛИЗАЦИЯ ЧЕРЕЗ БИБЛИОТЕКУ YADISK ----------------- #
# disk = yadisk.YaDisk(token=YANDEX_TOKEN)

# Определяем поддерживаемые типы файлов
# FILE_TYPES = {
#     'documents': ['.doc', '.docx', '.pdf', '.txt'],
#     'images': ['.jpg', '.jpeg', '.png', '.gif'],
#     'videos': ['.mp4', '.avi', '.mkv'],
#     'music': ['.mp3', '.wav'],
# }
#
#
# @cache_page(3 * 60)
# def get_home(request):
#     file_type = request.GET.get('media_type', 'all')  # По умолчанию показываем все файлы
#     files = disk.listdir("/")
#
#     if file_type in FILE_TYPES:
#         extensions = FILE_TYPES[file_type]
#         files = [file for file in files if any(file['name'].endswith(ext) for ext in extensions)]
#
#     return render(request, template_name='base.html', context={
#         'title': 'Главная страница',
#         'name_file': files,
#         'file_types': FILE_TYPES.keys(),
#     })


# ----------------- РЕАЛИЗАЦИЯ ЧЕРЕЗ БИБЛИОТЕКУ REQUESTS ----------------- #
get_all_file_url = 'https://cloud-api.yandex.net/v1/disk/resources/files'
headers = {
    'Authorization': f'OAuth {YANDEX_TOKEN}'
}

# Определяем поддерживаемые типы файлов
FILE_TYPES = {
    'document',
    'book',
    'video',
    'audio',
}


@cache_page(3 * 60)
def get_home(request):
    params = request.GET.get('media_type')
    response = requests.get(get_all_file_url, headers=headers, params={'media_type': params if params != 'all' else ''})
    files = response.json()
    return render(request, template_name='base.html', context={
        'title': 'Главная страница',
        'name_file': files.get('items'),
        'file_types': FILE_TYPES
    })
