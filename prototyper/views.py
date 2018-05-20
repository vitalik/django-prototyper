import os
import json
from django.conf import settings
from django.template import Template, Context
from django.http import JsonResponse, HttpResponse
from prototyper import VERSION
from .build import run_build
from . import plugins

HOME_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>prototyper</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link href="https://use.fontawesome.com/releases/v5.0.7/css/all.css" rel="preload" as="style">
    <link href="https://use.fontawesome.com/releases/v5.0.7/css/all.css" rel="stylesheet">
</head>
<body>
    <div id="prototyper"></div>
    
    <script>
        var PROJECT_DATA = {{ PROJECT_DATA|safe }}
        var PROTOTYPER_VERSION = '{{ VERSION }}'
    </script>
    <script type="text/javascript" src="{{JS_BUNDLE}}"></script>
</body>
</html>
"""


def _js_bundle():
    if settings.DEV_MODE and not os.environ.get('STATIC_BUNDLE'):
        return 'http://localhost:9000/dist/build.js'
    return '/static/build.js'


def main_view(request):
    data = settings.PROTOTYPER_PROJECT.load()
    ctx = {
        'PROJECT_DATA': json.dumps(data),
        'JS_BUNDLE': _js_bundle(),
        'VERSION': VERSION,
    }
    html = Template(HOME_TEMPLATE).render(Context(ctx))
    return HttpResponse(html)


def api_build(request):
    build = run_build()
    return JsonResponse({
        'success': build.success,
        'logs': build.logger.serialize()
    })


def api_save(request):
    data = _json_body(request)
    settings.PROTOTYPER_PROJECT.save(data)
    return JsonResponse({'success': True})


def discover_plugins(request):
    query = request.GET['q']
    data = plugins.search_plugins(query)
    return JsonResponse({'success': True, 'results': data})


def install_plugin(request):
    data = _json_body(request)
    plugin = plugins.install(data['name'], data['url'])
    return JsonResponse({'success': True, 'plugin': plugin})


def _json_body(request):
    return json.loads(request.body.decode('utf-8'))
