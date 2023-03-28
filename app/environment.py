import itertools
from functools import cached_property

from app.configuration.configuration import Configuration
from app.configuration.database_connection import DatabaseConnection
from app.gateways.customer_gateway import CustomerGateway
from app.gateways.product_gateway import ProductGateway
from app.handlers.customer_handlers import CustomerBirthdayHandler, CustomersLatestOrderHandler, BaseCustomerHandler
from app.handlers.produt_handler import ProductTopSalseHandler


class Environment:

    def get_handlers(self) -> list:
        return list(itertools.chain(self.customer_handlers, self.product_handlers))

    @cached_property
    def customer_handlers(self) -> [BaseCustomerHandler]:
        return [
                CustomerBirthdayHandler(self.customer_gateway),
                CustomersLatestOrderHandler(self.customer_gateway),
               ]

    @cached_property
    def product_handlers(self) -> list:
        return [
                ProductTopSalseHandler(self.product_gateway),
               ]

    @cached_property
    def customer_gateway(self) -> CustomerGateway:
        return CustomerGateway(self.db_conn)

    @cached_property
    def product_gateway(self) -> ProductGateway:
        return ProductGateway(self.db_conn)

    @cached_property
    def db_conn(self) -> DatabaseConnection:
        return DatabaseConnection()

    @cached_property
    def configuration(self) -> Configuration:
        return Configuration()