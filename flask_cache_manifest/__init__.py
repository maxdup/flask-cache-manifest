import logging
import json
import os

from flask import request, url_for


class FlaskCacheManifest(object):
    def __init__(self, app=None):
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """
        :param app: Flask application
        :return: None
        """
        self.manifests = {}

        self.load_manifest("static", app)
        for endpoint, blueprint in app.blueprints.items():
            self.load_manifest(f"{endpoint}.static", blueprint)

        app.add_template_global(self.static_url_for)

    def load_manifest(self, endpoint, scaffold):
        if not scaffold.has_static_folder:
            return

        manifest_path = os.path.join(scaffold._static_folder,
                                     "cache_manifest.json")
        try:
            with scaffold.open_resource(manifest_path, "r") as f:
                self.manifests[endpoint] = json.load(f)
        except json.JSONDecodeError:
            logging.warning(f"Couldn't decode file: {manifest_path}")
        except PermissionError:
            logging.warning(f"Couldn't access file: {manifest_path}")
        except (FileNotFoundError, Exception):
            pass

    def hashed_url_for(self, endpoint, **values):
        """
        :param endpoint: The endpoint of the URL
        :type endpoint: str
        :param values: Arguments of the URL rule
        :return: Static file path.
        """

        if request is not None:
            blueprint_name = request.blueprint
            if endpoint[:1] == ".":
                if blueprint_name is not None:
                    endpoint = f"{blueprint_name}{endpoint}"
                else:
                    endpoint = endpoint[1:]

        manifest = self.manifests.get(endpoint, {})
        filename = values.get("filename", None)
        values['filename'] = manifest.get(filename, filename)

        return url_for(endpoint, **values)
