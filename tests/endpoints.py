

def test_specific_endpoints(app, client):
    huf = app.jinja_env.globals['hashed_url_for']

    # static endpoint
    with app.test_request_context():
        css_url = huf('static', filename='app.css')
        assert css_url == '/static/app.298c725b7e42a4c6419f.css'
        js_url = huf('static', filename='app.js')
        assert js_url == '/static/app-afc95bdb227d3f19d501.js'

    assert client.get(css_url).status_code == 200
    assert client.get(js_url).status_code == 200

    # one.static endpoint
    with app.test_request_context():
        css_url = huf('one.static', filename='app.css')
        assert css_url == '/one/static/app.f156bde7a0c92f6878e6.css'
        js_url = huf('one.static', filename='app.js')
        assert js_url == '/one/static/app-439356ae5e62a44e8476.js'

    assert client.get(css_url).status_code == 200
    assert client.get(js_url).status_code == 200

    # one.a.static endpoint
    with app.test_request_context():
        css_url = huf('one.a.static', filename='app.css')
        assert css_url == '/one/a/static/app.2c9a71a69b1e717b6a86.css'
        js_url = huf('one.a.static', filename='app.js')
        assert js_url == '/one/a/static/app-fdcc95dac4268db0ebad.js'

    assert client.get(css_url).status_code == 200
    assert client.get(js_url).status_code == 200

    # two.static endpoint
    with app.test_request_context():
        css_url = huf('two.static', filename='app.css')
        assert css_url == '/two-static/app.2c9a71a69b1e717b6a86.css'
        js_url = huf('two.static', filename='app.js')
        assert js_url == '/two-static/app-fdcc95dac4268db0ebad.js'

    assert client.get(css_url).status_code == 200
    assert client.get(js_url).status_code == 200


def test_relative_endpoints(app, client):
    huf = app.jinja_env.globals['hashed_url_for']

    # static endpoint
    with app.test_request_context('/'):
        css_url = huf('.static', filename='app.css')
        assert css_url == '/static/app.298c725b7e42a4c6419f.css'
        js_url = huf('.static', filename='app.js')
        assert js_url == '/static/app-afc95bdb227d3f19d501.js'

    assert client.get(css_url).status_code == 200
    assert client.get(js_url).status_code == 200

    # one.static endpoint
    with app.test_request_context('/one/'):
        css_url = huf('.static', filename='app.css')
        assert css_url == '/one/static/app.f156bde7a0c92f6878e6.css'
        js_url = huf('.static', filename='app.js')
        assert js_url == '/one/static/app-439356ae5e62a44e8476.js'

    assert client.get(css_url).status_code == 200
    assert client.get(js_url).status_code == 200

    # one.a.static endpoint
    with app.test_request_context('/one/a'):
        css_url = huf('.static', filename='app.css')
        assert css_url == '/one/a/static/app.2c9a71a69b1e717b6a86.css'
        js_url = huf('.static', filename='app.js')
        assert js_url == '/one/a/static/app-fdcc95dac4268db0ebad.js'

    assert client.get(css_url).status_code == 200
    assert client.get(js_url).status_code == 200

    # two.static endpoint
    with app.test_request_context('/two'):
        css_url = huf('.static', filename='app.css')
        assert css_url == '/two-static/app.2c9a71a69b1e717b6a86.css'
        js_url = huf('.static', filename='app.js')
        assert js_url == '/two-static/app-fdcc95dac4268db0ebad.js'

    assert client.get(css_url).status_code == 200
    assert client.get(js_url).status_code == 200
