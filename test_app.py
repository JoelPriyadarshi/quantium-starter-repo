from dash.testing.composite import DashComposite
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from app import app

def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)
    header = dash_duo.find_element("h1")
    assert "Pink Morsel Sales Visualiser" in header.text

def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    graph = dash_duo.find_element("#sales-line-chart")
    assert graph is not None

def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region-picker", timeout=10)
    region_picker = dash_duo.find_element("#region-picker")
    assert region_picker is not None