from flask_cache_manifest import FlaskCacheManifest
from unittest.mock import MagicMock


def test_init(appFactory):
    app = appFactory()

    flaskCacheManifest = FlaskCacheManifest()
    flaskCacheManifest.init_app(app)

    assert flaskCacheManifest.app == app


def test_init_with_app(appFactory):
    app = appFactory()

    FlaskCacheManifest.init_app = MagicMock()
    flaskCacheManifest = FlaskCacheManifest(app)
    FlaskCacheManifest.init_app.assert_called_with(app)

    assert flaskCacheManifest.app == app
