import pytest
from flask import Flask, Blueprint, testing, jsonify, make_response
from flask_cache_manifest import FlaskCacheManifest


class TestClient(testing.FlaskClient):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


def create_app():
    flaskapp = Flask('flask-ext',
                     static_folder='./tests/data/bundle1',
                     static_url_path='/static')

    flaskapp.config.update({
        'TEST': True,
    })
    flaskapp.url_map.strict_slashes = True
    flaskapp.test_client_class = TestClient

    bp_one = Blueprint("one",
                       __name__,
                       url_prefix="/one",
                       static_url_path='static',
                       static_folder="./tests/data/bundle2")

    bp_two = Blueprint("two",
                       __name__,
                       static_url_path="/two-static",
                       static_folder="./tests/data/bundle3")

    bp_one_a = Blueprint("a", __name__,
                         template_folder="./templates",
                         static_url_path="/a/static",
                         static_folder="./tests/data/bundle3")

    bp_one_b = Blueprint("b", __name__)

    @flaskapp.route('/')
    @bp_one.route('/')
    @bp_two.route('/two')
    @bp_one_a.route('/a')
    @bp_one_b.route('/b')
    def mockRoute():
        return make_response(jsonify.dumps({}), 200)

    bp_one.register_blueprint(bp_one_a)
    bp_one.register_blueprint(bp_one_b)

    flaskapp.register_blueprint(bp_one)
    flaskapp.register_blueprint(bp_two)

    return flaskapp


@pytest.fixture
def appFactory():
    return create_app


@pytest.fixture
def app(appFactory):
    flaskapp = appFactory()

    flaskCacheManifest = FlaskCacheManifest()
    flaskCacheManifest.init_app(flaskapp)

    yield flaskapp


@pytest.fixture
def client(app):
    with app.test_client() as client:
        with app.app_context():
            yield client
