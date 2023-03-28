from datetime import datetime
from typing import Union

from app.gateways.customer_gateway import CustomerGateway
from app.handlers.base_handler import BaseHandler


class BaseCustomerHandler(BaseHandler):

    def __init__(self, customer_gateway: CustomerGateway):
        self.customer_gateway = customer_gateway


class CustomerBirthdayHandler(BaseCustomerHandler):

    @property
    def method(self):
        return ['GET']

    @property
    def path(self):
        return '/customers/birthday'

    def get_today_date(self):
        return datetime.today().strftime('%Y-%m-%d')

    async def callback_handler(self) -> list[Union[dict | None]]:
        """Returns customer that that has birthday today.
           Response structure:
           {
            "customers: [
                        {
                         "customer_id": integer,
                         ""customer_first_name":": string,
                        },
                      ]
            }
           """
        return await self.customer_gateway.fetch_customers_by_birthday_date(self.get_today_date())


class CustomersLatestOrderHandler(BaseCustomerHandler):

    @property
    def method(self):
        return ['GET']

    @property
    def path(self):
        return '/customers/last-order-per-customer'


    async def callback_handler(self) -> list[Union[dict | None]]:
        """Returns customers latest orders.
           Response structure:
                {
                    "customers: [
                                {
                                 "customer_id": integer,
                                 "customer_email": string,
                                 "last_order_date": string
                                },
                              ]
                }
        """
        return await self.customer_gateway.fetch_latest_customers_order()