import json
from django.conf import settings
from django.template import Template, Context
from django.http import JsonResponse, HttpResponse
from .build import run_build

HOME_TEMPLATE = """{% load render_bundle from webpack_loader %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>prototyper</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
</head>
<body>
    <div id="prototyper"></div>
    
    <script>
        var SETTINGS = {{ SETTINGS|safe }}
    </script>
    {% render_bundle 'main' %}
</body>
</html>
"""


def main_view(request):
    ctx = {'SETTINGS': json.dumps(settings.PROTOTYPER)}
    html = Template(HOME_TEMPLATE).render(Context(ctx))
    return HttpResponse(html)


def api_build(request):
    project = run_build(settings.PROTOTYPER)
    return JsonResponse({
        'success': project.success,
        'logs': project.logger.serialize()
    })


def api_save(request):
    data = json.loads(request.body)
    for a in data['apps']:
        print ('%20s' % a['name'], ':', [m['name'] for m in a['models']])
    return JsonResponse({'success': True})
