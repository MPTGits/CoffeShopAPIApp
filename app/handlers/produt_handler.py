from typing import Union

from app.gateways.product_gateway import ProductGateway
from app.handlers.base_handler import BaseHandler


class ProductTopSalseHandler(BaseHandler):
    LIMIT_PRODUCTS_TO_FETCH = 10

    def __init__(self, product_gateway: ProductGateway):
        self.product_gateway = product_gateway

    @property
    def method(self):
        return ['GET']

    @property
    def path(self):
        return '/products/top-selling-products/{year}'


    async def callback_handler(self, year: int) -> list[Union[dict | None]]:
        """Returns top selling products for given year.
           Response structure:
                {
                    "products: [
                                {
                                "product_name: string,
                                "total_sales": integer
                                },
                              ]
                }
         """
        return await self.product_gateway.fetch_top_selling_products_by_year(year, self.LIMIT_PRODUCTS_TO_FETCH)