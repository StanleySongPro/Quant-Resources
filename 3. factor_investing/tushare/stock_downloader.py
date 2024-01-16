from db_client import (
    DBOperations
)
from utils import timing_decorator, timing_decorator_async
from logs import TushareLogger
import pandas as pd
import asyncio
import concurrent.futures
import time

logger = TushareLogger.get_logger()


class FetchStockDataThreadPool:
    def __init__(self, tspro, db_client):
        self.tspro = tspro
        self.db_client = db_client

        # success dates
        self.stock_sdates = self._get_stock_sdate()
        self.basic_sdates = self._get_basic_sdate()

        # fail dates
        self.stock_fdates = []
        self.basic_fdates = []

    def _get_stock_sdate(self):
        cur = self.db_client.conn.cursor()
        cur.execute(
            """
            SELECT DISTINCT trade_date
            FROM stock_daily
            ORDER BY trade_date ASC;
            """
        )
        lresult = [i[0] for i in cur.fetchall()]
        return lresult

    def _get_basic_sdate(self):
        cur = self.db_client.conn.cursor()
        cur.execute(
            """
            SELECT DISTINCT trade_date
            FROM basic_daily
            ORDER BY trade_date ASC;
            """
        )
        lresult = [i[0] for i in cur.fetchall()]
        return lresult

    def get_daily(self, date):
        return self.tspro.daily(trade_date=date)

    def get_basic(self, date):
        return self.tspro.daily_basic(trade_date=date)

    # def fetch_daily_data(self, date):
    #     df_stock = self.get_daily(date)
    #     df_basic = self.get_basic(date)
    #     return (df_stock, df_basic)

    def fetch_daily_data(self, date):
        if not date in self.stock_sdates:
            try:
                df_stock = self.get_daily(date)
                DBOperations.insert_df_tosql(
                    self.db_client, df_stock, "stock_daily")
                self.stock_sdates.append(date)
                logger.debug(
                    f"{date} - Stock - Done"
                )
            except Exception as e:
                logger.error(
                    f"{date} - Stock - {e}"
                )
                self.stock_fdates.append(date)

        if not date in self.basic_sdates:
            try:
                df_basic = self.get_basic(date)
                DBOperations.insert_df_tosql(
                    self.db_client, df_basic, "basic_daily")
                self.basic_sdates.append(date)
                logger.debug(
                    f"{date} - Basic - Done"
                )
                time.sleep(2)
            except Exception as e:
                logger.error(
                    f"{date} - Basic - {e}"
                )
                self.basic_fdates.append(date)

    def __call__(self, df):
        assert "cal_date" in df.columns
        dates = df.cal_date.unique()
        with concurrent.futures.ThreadPoolExecutor() as executor:
            # results = list(executor.map(self.fetch_daily_data, dates))
            executor.map(self.fetch_daily_data, dates)
        logger.error(
            f"FAIL_DATES:\n{sorted(set(self.stock_fdates+self.basic_fdates))}")
        logger.debug(f"STOCK_DATES:\n{sorted(self.stock_sdates)}")
        logger.debug(f"BASIC_DATES:\n{sorted(self.basic_sdates)}")
        # return results


class FetchStockDataAsync:
    def __init__(self, tspro) -> None:
        self.tspro = tspro

    async def get_daily(self, date):
        return self.tspro.daily(trade_date=date)

    async def get_basic(self, date):
        return self.tspro.daily_basic(trade_date=date)

    async def fetch_daily_data(self, date):
        # 定义一个异步操作函数，接受一行数据作为参数
        df_daily = await self.get_daily(date)
        df_basic = await self.get_basic(date)
        return (df_daily, df_basic)

    # @timing_decorator_async
    async def __call__(self, df: pd.DataFrame = None):
        assert ("cal_date" in df.columns)
        # # 创建一个任务列表
        # tasks = (self.fetch_daily_data(date) for date in df.cal_date.unique())
        # # 使用asyncio.gather并行执行所有任务
        # results = await asyncio.gather(*tasks)
        results = []
        loop = asyncio.get_event_loop()
        for date in df.cal_date.unique():
            task = loop.run_in_executor(None, self.fetch_daily_data, date)
            r = await task
            results.append(r)
        # tasks = [loop.run_in_executor(None, self.fetch_daily_data, date)
        #          for date in df.cal_date.unique()]
        # for task in tasks:
        #     r = await task
        #     results.append(r)
        return results


class FetchStockData:
    def __init__(self, tspro) -> None:
        self.tspro = tspro

    def get_daily(self, date):
        return self.tspro.daily(trade_date=date)

    def get_basic(self, date):
        return self.tspro.daily_basic(trade_date=date)

    def fetch_daily_data(self, date):
        df_daily = self.get_daily(date)
        df_basic = self.get_basic(date)
        return (df_daily, df_basic)

    # @timing_decorator
    def __call__(self, df: pd.DataFrame = None):
        assert ("cal_date" in df.columns)
        results = []
        for date in df.cal_date.unique():
            results.append(self.fetch_daily_data(date))
        return results


@timing_decorator
def main():
    from data_api import TSDataAPI
    from db_client import PostgreSQLClient

    pro = TSDataAPI().pro
    df_cal = pro.trade_cal(
        start_date='20170101',
        end_date='20231109',
        exchange="SSE",
        is_open=1
    )

    # fetchStockDataAsync = FetchStockDataAsync(tspro=pro)
    # results = asyncio.run(fetchStockDataAsync(df=df_cal))
    # loop = asyncio.get_event_loop()
    # results = loop.run_until_complete(fetchStockDataAsync(df=df_cal))

    fetchStockDataThreadPool = FetchStockDataThreadPool(
        tspro=pro,
        db_client=PostgreSQLClient()
    )
    fetchStockDataThreadPool(df=df_cal)

    # fetchStockData = FetchStockData(tspro=pro)
    # results = fetchStockData(df=df_cal)

    # print(len(results))
    # print(results[4][0].shape)
    # print(results[4][1].shape)


if __name__ == "__main__":
    main()
