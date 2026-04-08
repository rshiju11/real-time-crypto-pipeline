USE crypto_db;

CREATE TABLE IF NOT EXISTS crypto_prices (
    id INT AUTO_INCREMENT PRIMARY KEY,
    coin_name VARCHAR(50) NOT NULL,
    symbol VARCHAR(20) NOT NULL,
    price_usd DECIMAL(18,8) NOT NULL,
    change_24h DECIMAL(10,4),
    last_updated_at BIGINT,
    fetched_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);