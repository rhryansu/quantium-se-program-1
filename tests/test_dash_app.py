from app import app


def test_daap001(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#header", timeout=10)


def test_daap002(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#visualization", timeout=10)


def test_daap_003(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region_picker", timeout=10)