import duckdb

def kalshi_m():
    con = duckdb.connect()

    result = con.execute("SELECT * FROM 'data/kalshi/markets/markets_170000_180000.parquet' ORDER BY RANDOM() LIMIT 5").fetchall()

    for row in result:
        print(row)
        print('\n')
        

def kalshi_m():
    con = duckdb.connect()

    result = con.execute("SELECT COUNT(*) FROM 'data/kalshi/markets/markets_170000_180000.parquet' ORDER BY RANDOM() LIMIT 5").fetchall()

    for row in result:
        print(row)
        print('\n')
        
def kalshi_m_count():
    con = duckdb.connect()

    result = con.execute("SELECT COUNT(*) FROM 'data/kalshi/markets/markets_170000_180000.parquet'").fetchall()

    print(result)
        
def kalshi_t():
    con = duckdb.connect()

    result = con.execute("SELECT * FROM 'data/kalshi/trades/trades_230000_240000.parquet' ORDER BY RANDOM() LIMIT 5").fetchall()

    for row in result:
        print(row)
        print('\n')

def kalshi_describe():
    con = duckdb.connect()

    result1 = con.execute("DESCRIBE SELECT * FROM 'data/kalshi/trades/trades_1070000_1080000.parquet'").fetchall()
    result2 = con.execute("DESCRIBE SELECT * FROM 'data/kalshi/markets/markets_610000_620000.parquet'").fetchall()

    print(result1)
    print('\n')

    print(result2)
    print('\n')


def kalshi_m_dist():
    con = duckdb.connect()

    result = con.execute("SELECT event_ticker, COUNT(*) as count FROM 'data/kalshi/markets/markets_170000_180000.parquet' GROUP BY event_ticker ORDER BY RANDOM()").fetchall()

    for row in result:
        print(row)
        print('\n')

def kalshi_m_ticker():
    con = duckdb.connect()

    result = con.execute("""
        SELECT 
        REGEXP_EXTRACT(event_ticker, '^([A-Z]+)', 1) as category,
        COUNT(*) as count
    FROM 'data/kalshi/markets/markets_7510000_7520000.parquet'
    WHERE event_ticker IS NOT NULL
    GROUP BY category
    ORDER BY count DESC
""").fetchall()

    print(result)


def kalshi_m_resolved():
    con = duckdb.connect()

    result = con.execute("""
    SELECT result, COUNT(*) as count
    FROM 'data/kalshi/markets/markets_7510000_7520000.parquet'
    GROUP BY result
""").fetchall()
    print(result)

def kalshi_m_vol():
    con = duckdb.connect()

    result = con.execute("""
    SELECT 
        MIN(volume), MAX(volume), AVG(volume), MEDIAN(volume)
    FROM 'data/kalshi/markets/*.parquet'
""").fetchall()
    
    print(result)

if __name__ == "__main__":
    kalshi_m_vol()
