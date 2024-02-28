import abc
import sqlite3
from contextlib import contextmanager
from pathlib import Path


class BaseDB:

    @contextmanager
    def __connection(self, db: str = None):
        if db is None:
            db = f'{Path(__file__).parent.parent.parent}/test.db'
        con = sqlite3.connect(db)
        try:
            yield con
        except Exception as e:
            print(e)
            con.rollback()
        else:
            con.commit()
        finally:
            con.close()

    def _execute_last_rowid(self, cur, sql, params=None):
        cur.execute(sql) if params is None else cur.execute(sql, params)
        return cur.lastrowid

    def _execute_fetch_all(self, cur, sql, params=None):
        cur.execute(sql) if params is None else cur.execute(sql, params)
        return cur.fetchall()

    # def _execute_fetch_many(self, cur, sql, params=None):


    def insert(self, sql: str, params: tuple = None):
        with self.__connection() as con:
            return self._execute_last_rowid(con.cursor(), sql, params)

    def bulk_insert(self, sql: str, params: list = None):
        with self.__connection() as con:
            cur = con.cursor()
            cur.executemany(sql, params)

    def query(self, sql, params: tuple = None, size: int = None):
        with self.__connection() as con:
            cur = con.cursor()
            if params is None:
                cur.execute(sql)
            else:
                cur.execute(sql, params)

            if size is None:
                return cur.fetchall()
            else:
                return cur.fetchmany(size=size)
            # return self._execute_fetch_all(con.cursor(), sql, params)

    def scalar(self, sql, params: tuple = None):
        with self.__connection() as con:
            cur = con.cursor()
            if params is None:
                cur.execute(sql)
            else:
                cur.execute(sql, params)
            return cur.fetchone()