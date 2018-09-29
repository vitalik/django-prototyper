import os
import shutil
from pathlib import Path
from django.template import Template, Context


def build_template(path, dest, context):
    for root, dirs, files in os.walk(path):
        for f in files:
            filename = os.path.join(root, f)
            text = render_file(filename, context)

            rel = os.path.relpath(filename, path)
            rel = render_str(rel, context)
            
            dest_file = Path(os.path.join(dest, rel))
            dest_file.parent.mkdir(parents=True, exist_ok=True)
            dest_file.write_text(text)


def render_str(s, context):
    return Template(s).render(Context(context))


def render_file(tpl_file, context):
    with open(tpl_file) as f:
        return render_str(f.read(), context)
