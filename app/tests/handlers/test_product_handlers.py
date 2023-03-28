from unittest.mock import create_autospec

from app.gateways.product_gateway import ProductGateway
from app.handlers.produt_handler import ProductTopSalseHandler


def get_product_top_sales_handler():
    product_gateway = create_autospec(ProductGateway)
    return ProductTopSalseHandler(product_gateway)


async def test_product_top_sales_handler_endpoint_properties():
    product_top_sales_handler = get_product_top_sales_handler()
    assert product_top_sales_handler.LIMIT_PRODUCTS_TO_FETCH == 10
    assert product_top_sales_handler.method == ['GET']
    assert product_top_sales_handler.path == '/products/top-selling-products/{year}'


async def test_product_top_sales_handler_calls_correct_gateway_method_with_passed_year_as_param():
    product_top_sales_handler = get_product_top_sales_handler()
    await product_top_sales_handler.callback_handler(1998)
    product_top_sales_handler.product_gateway.fetch_top_selling_products_by_year.assert_called_once_with(1998, 10)