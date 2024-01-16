# 使用tushare获取数据
import tushare as ts
# 设置好你的token
# token = '5e0883692141c916676a527d3d33643c79eb40c471163961afe71402'
token = 'b3252a4869a96c045a5111ed9f879b44bfcd0f02f2f84f9fe6d487a5'


class TSDataAPI:
    def __init__(self, token=token) -> None:
        self.pro = ts.pro_api(token)


if __name__ == "__main__":
    ts_api = TSDataAPI()
    df_daily = ts_api.pro.trade_cal(
        start_date='20231101',
        end_date='20231107',
        exchange="SSE",
        is_open=1
    )
