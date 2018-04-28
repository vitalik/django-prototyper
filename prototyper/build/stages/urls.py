
from ..base import BuildStage
from pathlib import Path

TPL = """\"\"\"Django project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
\"\"\"
from django.contrib import admin
from django.urls import include, path
%(extra_imports)s
urlpatterns = [
    path('admin/', admin.site.urls),
    %(extra_lines)s
]
"""


class UrlsStage(BuildStage):
    def run(self):
        urls_py = Path(self.build.settings_pckg_path) / 'urls.py'

        extra_lines = []
        extra_imports = []

        plugins = self.build.details['plugins']
        for plugin in plugins:
            urls_conf = plugin.get('urls', {})

            imports = urls_conf.get('imports', [])
            extra_imports.extend(imports)
            
            urls = urls_conf.get('urls', [])
            extra_lines.append('')
            extra_lines.extend(urls)

        code = TPL % {
            'extra_lines': '\n    '.join(extra_lines),
            'extra_imports': '\n'.join(extra_imports),
        }
        urls_py.write_text(code)
