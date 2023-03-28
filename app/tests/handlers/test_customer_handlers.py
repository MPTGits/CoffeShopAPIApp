from unittest.mock import create_autospec, patch

from app.gateways.customer_gateway import CustomerGateway
from app.handlers.customer_handlers import CustomerBirthdayHandler, CustomersLatestOrderHandler


def get_customer_birthday_handler():
    customer_gateway = create_autospec(CustomerGateway)
    return CustomerBirthdayHandler(customer_gateway)


def get_customer_latest_order_handler():
    customer_gateway = create_autospec(CustomerGateway)
    return CustomersLatestOrderHandler(customer_gateway)


async def test_customer_birthday_handler_endpoint_properties():
    customer_birthday_handler = get_customer_birthday_handler()
    assert customer_birthday_handler.method == ['GET']
    assert customer_birthday_handler.path == '/customers/birthday'


async def test_customer_birthday_handler_calls_correct_gateway_method_with_today_date_as_param():
    customer_birthday_handler = get_customer_birthday_handler()
    with patch.object(CustomerBirthdayHandler, 'get_today_date', return_value='2020-10-10'):
        await customer_birthday_handler.callback_handler()
        customer_birthday_handler.customer_gateway.fetch_customers_by_birthday_date.assert_called_once_with('2020-10-10')


async def test_customer_latest_order_endpoint_properties():
    customer_latest_order_handler = get_customer_latest_order_handler()
    assert customer_latest_order_handler.method == ['GET']
    assert customer_latest_order_handler.path == '/customers/last-order-per-customer'


async def test_customer_latest_order_calls_correct_gateway_method():
    customer_latest_order_handler = get_customer_latest_order_handler()
    await customer_latest_order_handler.callback_handler()
    customer_latest_order_handler.customer_gateway.fetch_latest_customers_order.assert_called_once_with()