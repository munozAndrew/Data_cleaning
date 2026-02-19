import duckdb

def poly_m():
    con = duckdb.connect()

    result = con.execute("SELECT * FROM 'data/polymarket/markets/markets_220000_230000.parquet' ORDER BY RANDOM() LIMIT 5").fetchall()

    for row in result:
        print(row)
        print('\n')
        

def poly_m_count():
    con = duckdb.connect()

    result = con.execute("SELECT COUNT(*) FROM 'data/polymarket/markets/markets_320000_330000.parquet' ORDER BY RANDOM() LIMIT 5").fetchall()

    for row in result:
        print(row)
        print('\n')
        
def kalshi_m_count():
    con = duckdb.connect()

    result = con.execute("SELECT COUNT(*) FROM 'data/kalshi/markets/markets_170000_180000.parquet'").fetchall()

    print(result)
        
def poly_t():
    con = duckdb.connect()

    result = con.execute("SELECT * FROM 'data/polymarket/trades/trades_230000_240000.parquet' ORDER BY RANDOM() LIMIT 5").fetchall()

    for row in result:
        print(row)
        print('\n')

def poly_describe():
    con = duckdb.connect()

    result1 = con.execute("DESCRIBE SELECT * FROM 'data/polymarket/trades/trades_230000_240000.parquet'").fetchall()
    result2 = con.execute("DESCRIBE SELECT * FROM 'data/polymarket/markets/markets_390000_400000.parquet'").fetchall()

    print(result1)
    print('\n')

    print(result2)
    print('\n')


def poly_m_dist():
    con = duckdb.connect()

    result = con.execute("SELECT question, COUNT(*) as count FROM 'data/polymarket/markets/markets_170000_180000.parquet' GROUP BY question ORDER BY RANDOM()").fetchall()

    for row in result:
        print(row)
        print('\n')

def kalshi_m_ticker():
    con = duckdb.connect()

    result = con.execute("""
        SELECT 
            SPLIT_PART(slug, '-', 1) as category,
            COUNT(*) as count
        FROM 'data/polymarket/markets/markets_170000_180000.parquet'
        WHERE slug IS NOT NULL
        GROUP BY category
        ORDER BY count DESC
        LIMIT 30
    """).fetchall()

    print(result)


def poly_m_resolved():
    con = duckdb.connect()

    result = con.execute("""
        SELECT active, closed, COUNT(*) as count
        FROM 'data/polymarket/markets/markets_170000_180000.parquet'
        GROUP BY active, closed
        ORDER BY count DESC
    """).fetchall()
    print(result)

def poly_m_vol():
    con = duckdb.connect()

    result = con.execute("""
    SELECT 
        MIN(volume), MAX(volume), AVG(volume), MEDIAN(volume)
    FROM 'data/polymarket/markets/markets_190000_200000.parquet'
""").fetchall()
    
    print(result)

if __name__ == "__main__":
    poly_m_vol()
