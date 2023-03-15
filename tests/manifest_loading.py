import json
import logging

from flask_cache_manifest import FlaskCacheManifest
from unittest.mock import MagicMock, patch


def test_manifest_loading(appFactory):
    app = appFactory()
    flaskCacheManifest = FlaskCacheManifest()

    # load first endpoint
    endpoint = 'one'
    bp = app.blueprints[endpoint]

    flaskCacheManifest.load_manifest(endpoint, bp)

    assert len(flaskCacheManifest.manifests) == 1
    assert endpoint in flaskCacheManifest.manifests
    assert 'app.js' in flaskCacheManifest.manifests[endpoint]
    assert 'app.css' in flaskCacheManifest.manifests[endpoint]

    assert flaskCacheManifest.manifests[endpoint]['app.js'] == \
        'app-439356ae5e62a44e8476.js'
    assert flaskCacheManifest.manifests[endpoint]['app.css'] == \
        'app.f156bde7a0c92f6878e6.css'

    # load second endpoint
    endpoint = 'two'
    bp = app.blueprints[endpoint]

    flaskCacheManifest.load_manifest(endpoint, bp)

    assert len(flaskCacheManifest.manifests) == 2
    assert endpoint in flaskCacheManifest.manifests
    assert 'app.js' in flaskCacheManifest.manifests[endpoint]
    assert 'app.css' in flaskCacheManifest.manifests[endpoint]

    assert flaskCacheManifest.manifests[endpoint]['app.js'] == \
        'app-fdcc95dac4268db0ebad.js'
    assert flaskCacheManifest.manifests[endpoint]['app.css'] == \
        'app.2c9a71a69b1e717b6a86.css'


def test_manifest_loading_error_generic(appFactory, caplog):
    app = appFactory()

    endpoint = 'one'
    bp = app.blueprints[endpoint]

    def generic_error_mock(*args):
        raise Exception

    # test missing errors
    bp.open_resource = MagicMock(side_effect=generic_error_mock)

    flaskCacheManifest = FlaskCacheManifest()
    flaskCacheManifest.load_manifest(endpoint, bp)

    assert len(caplog.records) == 0
    assert len(flaskCacheManifest.manifests) == 0

    caplog.clear()


def test_manifest_loading_error_notfound(appFactory, caplog):
    app = appFactory()

    endpoint = 'one'
    bp = app.blueprints[endpoint]

    def not_found_error_mock(*args):
        raise FileNotFoundError

    # test missing errors
    bp.open_resource = MagicMock(side_effect=not_found_error_mock)

    flaskCacheManifest = FlaskCacheManifest()
    flaskCacheManifest.load_manifest(endpoint, bp)

    assert len(caplog.records) == 0
    assert len(flaskCacheManifest.manifests) == 0

    caplog.clear()


def test_manifest_loading_error_permission(appFactory, caplog):
    app = appFactory()

    endpoint = 'one'
    bp = app.blueprints[endpoint]

    def perm_error_mock(*args):
        raise PermissionError

    # test permission errors
    bp.open_resource = MagicMock(side_effect=perm_error_mock)

    flaskCacheManifest = FlaskCacheManifest()
    flaskCacheManifest.load_manifest(endpoint, bp)

    assert len(caplog.records) == 1
    assert caplog.records[0].message.startswith(
        "Flask-Cache-Manifest | Couldn't access file:")

    assert len(flaskCacheManifest.manifests) == 0

    caplog.clear()


def test_manifest_loading_error_json(appFactory, caplog):
    app = appFactory()

    endpoint = 'one'
    bp = app.blueprints[endpoint]

    def json_error_mock(*args):
        raise json.JSONDecodeError('error', 'file', 0)

    # test decode errors
    bp.open_resource = MagicMock(side_effect=json_error_mock)

    flaskCacheManifest = FlaskCacheManifest()
    flaskCacheManifest.load_manifest(endpoint, bp)

    assert len(caplog.records) == 1
    assert caplog.records[0].message.startswith(
        "Flask-Cache-Manifest | Couldn't decode file:")

    assert len(flaskCacheManifest.manifests) == 0

    caplog.clear()
