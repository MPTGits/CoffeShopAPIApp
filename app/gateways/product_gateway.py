from typing import Union

from app.gateways.base_gateway import BaseGateway
from app.utils.singleton import Singleton


class ProductGateway(BaseGateway, metaclass=Singleton):
    _table_name = "Product"

    async def fetch_top_selling_products_by_year(self, year: int, products_limit: int) -> list[Union[dict | None]]:
        sql = f'''SELECT p.product, SUM(pi.quantity_sold) as total_sales
                    FROM "{self._table_name}" p
                    JOIN "Pastry_Inventory" pi ON pi.product_id = p.product_id
                   WHERE pi.transaction_date >= \'{year}-01-01\'
                     AND pi.transaction_date < \'{year+1}-01-01\'
                GROUP BY pi.product_id, p.product
                ORDER BY total_sales DESC
                   LIMIT {products_limit}'''
        return await self.db_conn.execute_query(sql)