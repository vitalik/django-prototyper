import os
import json

USER_PLUGINS_DIR = os.path.join(os.path.dirname(__file__), '..', 'demo_plugins')  # TODO: mabye ~/.prototyper ?


def search_plugins(query):
    results = []
    ud = USER_PLUGINS_DIR
    if os.path.exists(ud):
        for item in os.listdir(ud):
            config = os.path.join(ud, item, 'config.json')
            if not os.path.exists(config):
                continue
            with open(config) as f:
                data = json.load(f)
                meta = {k: data.get(k, '') for k in ['name', 'title', 'version', 'description']}
                meta['url'] = os.path.join(ud, item)
                results.append(meta)
    return results
