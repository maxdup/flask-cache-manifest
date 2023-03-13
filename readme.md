# Flask-Cache-Manifest
    Flask extension serving md5 hashed assets.

    Full Documentation:

    Turns:
    ```Jinja
    <link type="text/css" rel="stylesheet"
        href="{{ hashed_url_for('static', filename='css/app.css') }}">

    ```

    into
    ```Jinja
    <link type="text/css" rel="stylesheet"
        href="/static/css/app-d41d8cd98f00b204e9800998ecf8427e.css">
    ```
