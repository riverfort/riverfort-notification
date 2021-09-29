import psycopg2
import logger
import sys


class DatabaseConnection(object):
    """ Handles the main connection to the database of the app
          setting """

    def __init__(self, database, user, password, host, port):
        self.database = database
        self.user = user
        self.password = password
        self.port = port
        self.host = host

    def connect(self):
        connection = None
        try:
            logger.debug_msg('Connecting to the PostgreSQL database...')
            # Connect to postgres sql database
            connection = psycopg2.connect(database=self.database,
                                          user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port)
            # Create a cursor
            cursor = connection.cursor()

            # execute a statement
            cursor.execute('SELECT version()')

            # display the PostgreSQL database server version
            db_version = cursor.fetchone()
            logger.debug_msg(f'PostgreSQL database version: {db_version}')
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error("DB-ERROR: ", str(error))
        finally:
            if connection is not None:
                connection.close()
                logger.debug_msg('Database is connected successfully.')
            else:
                logger.debug_msg('Database is not connected successfully.')
                sys.exit()

    def create_table(self, command):

        connection = None
        try:
            # Connect to postgres sql database
            connection = psycopg2.connect(database=self.database,
                                          user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port)
            # Create a cursor
            cursor = connection.cursor()
            cursor.execute(command)
            # print(cursor.query)
            cursor.close()
            connection.commit()
            connection.close()
            print("Table created successfully\n")
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error("DB-ERROR: ", str(error))
        finally:
            if connection is not None:
                connection.close()

    def insert_data(self, sql, values):
        connection = None
        try:
            # Connect to postgres sql database
            connection = psycopg2.connect(database=self.database,
                                          user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port)
            # Create a cursor
            cursor = connection.cursor()
            cursor.execute(sql, values)
            # print(cursor.query)
            id = cursor.fetchone()[0]
            cursor.close()
            connection.commit()
            connection.close()
            return id
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error("DB-ERROR: ", str(error))
        finally:
            if connection is not None:
                connection.close()

    def select_data(self, sql):
        connection = None
        try:
            # Connect to postgres sql database
            connection = psycopg2.connect(database=self.database,
                                          user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port)
            # Create a cursor
            cursor = connection.cursor()
            cursor.execute(sql)
            # print("Selecting rows:")
            records = cursor.fetchall()
            # print(cursor.query)
            cursor.close()
            connection.close()
            return records
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error("DB-ERROR: ", str(error))
        finally:
            if connection is not None:
                connection.close()

    def filter_data(self, sql, values):
        connection = None
        try:
            # Connect to postgres sql database
            connection = psycopg2.connect(database=self.database,
                                          user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port)
            # Create a cursor
            cursor = connection.cursor()
            cursor.execute(sql, values)
            # records = cursor.fetchone()[0]
            records = cursor.fetchall()
            # print(cursor.query)
            cursor.close()
            connection.close()
            return records
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error("DB-ERROR: ", str(error))
        finally:
            if connection is not None:
                connection.close()

    def delete_all(self, sql):
        connection = None
        try:
            # Connect to postgres sql database
            connection = psycopg2.connect(database=self.database,
                                          user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port)
            # Create a cursor
            cursor = connection.cursor()
            cursor.execute(sql)
            rows_deleted = cursor.rowcount

            connection.commit()
            cursor.close()
            connection.close()

            return rows_deleted
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error("DB-ERROR: ", str(error))
        finally:
            if connection is not None:
                connection.close()

    def delete(self, sql, values):
        connection = None
        try:
            # Connect to postgres sql database
            connection = psycopg2.connect(database=self.database,
                                          user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port)
            # Create a cursor
            cursor = connection.cursor()
            cursor.execute(sql, values)
            rows_deleted = cursor.rowcount

            connection.commit()
            cursor.close()
            connection.close()

            return rows_deleted
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error("DB-ERROR: ", str(error))
        finally:
            if connection is not None:
                connection.close()

    def update_data(self, sql, values):
        connection = None
        try:
            # Connect to postgres sql database
            connection = psycopg2.connect(database=self.database,
                                          user=self.user,
                                          password=self.password,
                                          host=self.host,
                                          port=self.port)
            # Create a cursor
            cursor = connection.cursor()
            cursor.execute(sql, values)
            # get the number of updated rows
            updated_rows = cursor.rowcount
            cursor.close()
            connection.commit()
            connection.close()
            return updated_rows
        except (Exception, psycopg2.DatabaseError) as error:
            logger.error("DB-ERROR: ", str(error))
        finally:
            if connection is not None:
                connection.close()
