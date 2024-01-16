import psycopg2
from psycopg2.extras import execute_values


class PostgreSQLClient:
    def __init__(
            self,
    ):
        self.host = 'localhost'
        self.port = 5432
        self.user = 'postgres'
        self.password = '123456'
        self.database = 'tushare'
        self.conn = psycopg2.connect(
            host=self.host,
            port=self.port,
            user=self.user,
            password=self.password,
            database=self.database
        )


class DBOperations:
    @staticmethod
    def insert_df_tosql(db_client, df, table_name):
        cur = db_client.conn.cursor()
        values = [tuple(row) for row in df.to_numpy()]
        execute_values(
            cur,
            f"INSERT INTO {table_name} ({(', ').join(df.columns.to_list())}) VALUES %s",
            values
        )
        db_client.conn.commit()
        cur.close()

    # @staticmethod
    # def create_table(db_client, table_name):
    #     query = """

    #     """

    #     with db_client.conn.cursor() as cur:
    #         cur.execute(query)
    #         result = cur.fetchall()

    @staticmethod
    def execute_query(db_client, query=None):
        with db_client.conn.cursor() as cur:
            cur.execute(query)
            result = cur.fetchall()
        return result


def get_trade_date(pro, client):
    df = pro.trade_cal(exchange='SSE', is_open='1',
                       start_date='20230301',
                       end_date='20230303',
                       fields='cal_date')

    for date in df['cal_date'].values:
        df_stock = pro.daily(trade_date=date)
        df_basic = pro.daily_basic(trade_date=date)
        print(f"{date}\n{df.head(1)}")
        DBOperations.insert_df_tosql(client, df_stock, "stock_daily")
        DBOperations.insert_df_tosql(client, df_basic, "basic_daily")


if __name__ == "__main__":
    from data_api import TSDataAPI

    pro = TSDataAPI().pro
    postgresql_client = PostgreSQLClient()
    get_trade_date(pro, postgresql_client)
