from contextlib import closing

__author__ = 'Alexey'
from config import ConfigReader as cr
import pymysql.cursors
import inspect


class Singleton(type):
    def __init__(cls, name, bases, dic):
        super(Singleton, cls).__init__(name, bases, dic)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance


class SingletonArgs(type):
    _instances = {}
    _init = {}

    def __init__(cls, name, bases, dct):
        cls._init[cls] = dct.get('__init__', None)

    def __call__(cls, *args, **kwargs):
        init = cls._init[cls]
        if init is not None:
            key = (cls, frozenset(
                inspect.getcallargs(init, None, *args, **kwargs).items()))
        else:
            key = cls

        if key not in cls._instances:
            cls._instances[key] = super(SingletonArgs, cls).__call__(*args, **kwargs)
        return cls._instances[key]


class MySQLDB(object):
    __metaclass__ = SingletonArgs

    def __init__(self):
        self._db_connection = pymysql.connect(host=cr('db').get('mysql_host'),
                                              port=cr('db').get('mysql_port'),
                                              user=cr('db').get('mysql_user'),
                                              password=cr('db').get('mysql_password'),
                                              db=cr('db').get('mysql_dbname'),
                                              charset='utf8',
                                              use_unicode=True,
                                              cursorclass=pymysql.cursors.DictCursor)
        self._db_connection.autocommit(True)

    def get_token(self, user_id, game_id):
        with closing(self._db_connection.cursor()) as cursor:
            cursor.execute(
                'select * from tokens where user_id={user_id} and game_id={game_id} limit 1'.format(user_id=user_id,
                                                                                                    game_id=game_id))
            result = cursor.fetchone()
            return result
			
    def get_updated_index(self):
        with closing(self._db_connection.cursor()) as cursor:
            sql = "SELECT `table_name`, `column_name`, IF(extra like '%on update CURRENT_TIMESTAMP%', 1, 0) AS `updates`, IF(column_key <> '', 1, 0) AS `has_key` FROM `information_schema`.`columns` WHERE (`table_schema`=DATABASE()) AND (`column_name`='updated_at') GROUP BY `table_name`, `column_name` HAVING `table_name` LIKE 'user%';"
            cursor.execute(sql)
            res = cursor.fetchall()
            return res
			
    def get_db_collation(self):
        with closing(self._db_connection.cursor()) as cursor:
            sql = "SELECT `table_name`, TABLE_COLLATION FROM `information_schema`.`tables` WHERE `table_schema`=DATABASE() GROUP BY `table_name`;"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result


