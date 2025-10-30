import pytest

from src.views.utils import get_sale_report_view

def test_text_view():
    
    View = get_sale_report_view(name="text")
    text_view = View(
        total_sale_by_prod={"prod 1": 100.0, "prod 2": 50.0},
        overall_sales=88,
        most_sold_prod="Test"
    )
    assert type(text_view.create()) == str

def test_json_view():
    View = View = get_sale_report_view(name="json")
    text_view = View(
        total_sale_by_prod={"prod 1": 100.0, "prod 2": 50.0},
        overall_sales=88,
        most_sold_prod="Test"
    )
    assert type(text_view.create()) == dict

def test_fail_view():
    with pytest.raises(TypeError):
        get_sale_report_view(name="fail")