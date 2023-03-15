from flask import Flask
from flask_cache_manifest import FlaskCacheManifest
from unittest.mock import MagicMock, call
from unittest import mock


def test_init(appFactory):
    app = appFactory()

    flaskCacheManifest = FlaskCacheManifest()
    flaskCacheManifest.init_app(app)

    assert flaskCacheManifest.app == app


def test_init_with_app(appFactory, *args):
    app = appFactory()
    with mock.patch('flask_cache_manifest.FlaskCacheManifest.init_app') \
            as mock_init_app:
        flaskCacheManifest = FlaskCacheManifest(app)
        mock_init_app.assert_called_with(app)

    assert flaskCacheManifest.app == app


def test_init_app_templates(appFactory):
    app = appFactory()
    app.config['CACHE_MANIFEST_REPLACE_URL_FOR'] = False

    with mock.patch('flask.Flask.add_template_global') \
            as mock_add_template_global:

        flaskCacheManifest = FlaskCacheManifest()
        flaskCacheManifest.init_app(app)

        mock_add_template_global.assert_called_once_with(
            flaskCacheManifest.hashed_url_for,
            name='hashed_url_for')


def test_init_app_templates_replace(appFactory):
    app = appFactory()
    app.config['CACHE_MANIFEST_REPLACE_URL_FOR'] = True

    with mock.patch('flask.Flask.add_template_global') \
            as mock_add_template_global:

        flaskCacheManifest = FlaskCacheManifest()
        flaskCacheManifest.init_app(app)

        mock_add_template_global.assert_has_calls([
            call(flaskCacheManifest.hashed_url_for, name='hashed_url_for'),
            call(flaskCacheManifest.hashed_url_for, name='url_for')],
            any_order=True)


def test_init_app_globals(appFactory):
    app = appFactory()
    app.config['CACHE_MANIFEST_REPLACE_URL_FOR'] = False

    flaskCacheManifest = FlaskCacheManifest()
    flaskCacheManifest.init_app(app)

    assert app.jinja_env.globals['hashed_url_for'] == \
        flaskCacheManifest.hashed_url_for
    assert app.jinja_env.globals['url_for'] != \
        flaskCacheManifest.hashed_url_for


def test_init_app_globals_replace(appFactory):
    app = appFactory()
    app.config['CACHE_MANIFEST_REPLACE_URL_FOR'] = True

    flaskCacheManifest = FlaskCacheManifest()
    flaskCacheManifest.init_app(app)

    assert app.jinja_env.globals['hashed_url_for'] == \
        flaskCacheManifest.hashed_url_for
    assert app.jinja_env.globals['url_for'] == \
        flaskCacheManifest.hashed_url_for
