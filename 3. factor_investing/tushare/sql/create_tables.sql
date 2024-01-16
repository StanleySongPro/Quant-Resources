-- list all tables
SELECT table_name 
FROM information_schema.tables
WHERE table_schema = 'public';

DROP TABLE "public"."stock_daily";
DROP TABLE "public"."basic_daily";

-- create tables
CREATE TABLE "public"."stock_daily" (
    "ts_code"     VARCHAR(20),
    "trade_date"  VARCHAR(20),
    "open"        NUMERIC,
    "high"        NUMERIC,
    "low"         NUMERIC,
    "close"       NUMERIC,
    "pre_close"   NUMERIC,
    "change"      NUMERIC,
    "pct_chg"     NUMERIC,
    "vol"         NUMERIC,
    "amount"      NUMERIC
);

CREATE TABLE "public"."basic_daily" (
    "ts_code"           VARCHAR(20),
    "trade_date"        VARCHAR(20),
    "close"             NUMERIC,
    "turnover_rate"     NUMERIC,
    "turnover_rate_f"   NUMERIC,
    "volume_ratio"      NUMERIC,
    "pe"                NUMERIC,
    "pe_ttm"            NUMERIC,
    "pb"                NUMERIC,
    "ps"                NUMERIC,
    "ps_ttm"            NUMERIC,
    "dv_ratio"          NUMERIC,
    "dv_ttm"            NUMERIC,
    "total_share"       NUMERIC,
    "float_share"       NUMERIC,
    "free_share"        NUMERIC,
    "total_mv"          NUMERIC,
    "circ_mv"           NUMERIC
);

SELECT * FROM "public"."stock_daily" LIMIT 10;
SELECT * FROM "public"."basic_daily" LIMIT 10;

SELECT DISTINCT "trade_date"
FROM "public"."stock_daily"
ORDER BY "trade_date" ASC;

SELECT DISTINCT "trade_date"
FROM "public"."basic_daily"
ORDER BY "trade_date" ASC;

-- raw data for calculating the SMB HML
SELECT 
    t1.trade_date,
	t1.ts_code,
	t1.pct_chg,
    t2.circ_mv,
	t2.pb
FROM stock_daily t1
INNER JOIN basic_daily t2
ON t1.trade_date = t2.trade_date AND t1.ts_code = t2.ts_code
WHERE t1.trade_date BETWEEN '20170101' AND '20170131'
ORDER BY t1.trade_date ASC;









