-- It is fact table because it stores numerical stock trading metrics. 

CREATE TABLE stock_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    trade_date DATE,
    stock_symbol VARCHAR(20),
    open_price DOUBLE,
    high_price DOUBLE,
    low_price DOUBLE,
    close_price DOUBLE,
    volume BIGINT
);

SELECT * FROM stock_prices;



-- Create Metadata Table that is dimension table 

CREATE TABLE stock_metadata (
    company_name VARCHAR(100),
    industry VARCHAR(50),
    stock_symbol VARCHAR(20),
    series VARCHAR(5),
    isin_code VARCHAR(20),
    PRIMARY KEY (stock_symbol)
);

SELECT * FROM stock_metadata;



-- Total rows
SELECT COUNT(*) FROM stock_prices;

-- Unique companies
SELECT COUNT( DISTINCT( stock_symbol)) FROM stock_prices;

-- Date range
SELECT MIN( trade_date), MAX( trade_date ) FROM stock_prices;

-- Missing values
SELECT COUNT(*) FROM stock_prices
WHERE  close_price IS NULL;


-- Top traded stocks
SELECT stock_symbol, ROUND(AVG(volume),2) AS avg_volume
FROM stock_prices
GROUP BY stock_symbol
ORDER BY avg_volume DESC
LIMIT 5;

-- Best performing stocks
SELECT stock_symbol, MAX(close_price) - MIN(close_price)  AS growth
FROM stock_prices
GROUP BY stock_symbol
ORDER BY growth DESC
LIMIT 5;

-- Sector performance
SELECT industry, ROUND(AVG(close_price),2) avg_price
FROM stock_full_data
GROUP BY industry
ORDER BY avg_price DESC;


-- Join the tables
CREATE VIEW stock_full_data AS
SELECT
    s.trade_date,
    s.stock_symbol,
    m.company_name,
    m.industry,
    s.open_price,
    s.high_price,
    s.low_price,
    s.close_price,
    s.volume
FROM stock_prices s
JOIN stock_metadata m
ON s.stock_symbol = m.stock_symbol;






