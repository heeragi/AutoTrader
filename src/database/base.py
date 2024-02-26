import abc
import sqlite3
from contextlib import contextmanager


class BaseDB:

    @contextmanager
    def __connection(self, db: str = None):
        if db is None:
            db = '../../tests/test.db'
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

    def insert(self, sql: str, params: tuple = None):
        with self.__connection() as con:
            return self._execute_last_rowid(con.cursor(), sql, params)

    def bulk_insert(self, sql: str, params: list = None):
        with self.__connection() as con:
            cur = con.cursor()
            cur.executemany(sql, params)

    # def __query(self, sql, params: tuple = None):
    #     cur = self.__connection.cursor()
    #     try:
    #         if params is None:
    #             cur.execute(sql)
    #         else:
    #             cur.execute(sql, params)
    #     except Exception as e:
    #         print(e)
    #         return None
    #     return cur.fetchall()
