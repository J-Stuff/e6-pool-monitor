import sqlite3, time, logging
logger = logging.getLogger("main")
class DB():
    pool_db_location = "./data/pools.db"

    def __init__(self):
        logger.debug("New database class initialized")
        self.conn = sqlite3.connect(self.pool_db_location)
        logger.debug(f"Connected to database @ {self.pool_db_location}")
        self.c = self.conn.cursor()
        self.c.execute("""
                        CREATE TABLE IF NOT EXISTS pools (
                        pool_id INTEGER NOT NULL UNIQUE, 
                        added INTEGER NOT NULL, 
                        updated INTEGER NOT NULL, 
                        latest_page_id INTEGER NOT NULL, 
                        subscribers TEXT NOT NULL, 
                        pool_name TEXT NOT NULL, 
                        PRIMARY KEY(pool_id))
                        """)
        self.conn.commit()
        logger.debug("Database table check ran")
    
    def add_new_pool(self, pool_id:int, latest_page_id:int, subscriber:str, pool_name:str):
        logger.debug(f"Adding new pool to database: {pool_id}, {latest_page_id}, {subscriber}, {pool_name}")
        self.c.execute("""
                        INSERT INTO pools (pool_id, added, updated, latest_page_id, subscribers, pool_name) 
                        VALUES (?, ?, ?, ?, ?, ?)
                        """, (pool_id, int(time.time()), 0, latest_page_id, f"[{subscriber}]", pool_name))
        self.conn.commit()
        logger.debug(f"Added new pool to database: {pool_id}, {latest_page_id}, {subscriber}, {pool_name}")