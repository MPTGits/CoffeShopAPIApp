from typing import Union

from app.gateways.base_gateway import BaseGateway
from app.utils.singleton import Singleton


class CustomerGateway(BaseGateway, metaclass=Singleton):
    _table_name = "Customer"

    async def fetch_customers_by_birthday_date(self, birthday_date: str) -> list[Union[dict | None]]:
        sql = f'''SELECT customer_id, customer_first_name
                   FROM "{self._table_name}"
                   WHERE birthdate=\'{birthday_date}\''''
        return await self.db_conn.execute_query(sql)

    async def fetch_latest_customers_order(self) -> list[Union[dict | None]]:
        sql = f'''SELECT c.customer_id, c.customer_email, MAX(sr.transaction_date) AS last_order_date
                   FROM "{self._table_name}" c
                   LEFT JOIN "Sales_Reciept" sr 
                     ON sr.customer_id = c.customer_id
                  GROUP BY c.customer_id, c.customer_email
                '''
        return await self.db_conn.execute_query(sql)