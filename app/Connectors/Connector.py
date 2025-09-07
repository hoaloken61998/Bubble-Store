import mysql.connector
import traceback
import pandas as pd
from Utils.schemas_prettier import schemas_prettier

class Connector:
    def __init__(self, server=None, port=None, username=None, database=None, password=None):
        self.server = server
        self.port = port
        self.username = username
        self.database = database
        self.password = password
        self.conn = None
        self.schema_dictionary = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host=self.server,
                port=self.port,
                user=self.username,
                database=self.database,
                password=self.password,
                auth_plugin='mysql_native_password')

            self.get_all_schemas()
            return self.conn
        except Exception as e:
            self.conn = None
            traceback.print_exc()
            return None

    def disconnect(self):
        if self.conn is not None:
            self.conn.close()

    def get_index_of_table(self, table_name=None):
        tables = self.schema_dictionary[self.database]['Tables']
        index = None
        for i in range(len(tables)):
            if tables[i]['TableName'] == table_name:
                index = i
                break
            else:
                continue
        return index

    def filter_username_password(self, table_name, username, password):
        index = self.get_index_of_table(table_name)
        if index is not None:
            columns_sql = self.schema_dictionary[self.database]['Tables'][index]['Columns']
            column_names = [column['ColumnName'] for column in columns_sql]
            try:
                data_sql = f"""
                            SELECT * FROM {self.conn.database}.{table_name}
                            WHERE Username ='{username}'    
                            AND Password = '{password}'
                            """
                with self.conn.cursor() as cursor:
                    cursor.execute(data_sql)
                    data = cursor.fetchall()
                    df = pd.DataFrame(data, columns=column_names)
                    return not df.empty
            except Exception as e:
                traceback.print_exc()
                return False

    def get_all_schemas(self):
        try:
            sql = f"""SELECT 
                        c.TABLE_SCHEMA AS schema_name,
                        c.TABLE_NAME AS table_name,
                        c.COLUMN_NAME AS column_name,
                        c.DATA_TYPE AS data_type,
                        kcu.CONSTRAINT_NAME AS pk_name,
                        CASE 
                            WHEN extra = 'auto_increment' THEN 'YES'
                            ELSE 'NO'
                        END AS is_auto_increment
                    FROM 
                        INFORMATION_SCHEMA.COLUMNS c
                    LEFT JOIN 
                        INFORMATION_SCHEMA.KEY_COLUMN_USAGE kcu ON c.TABLE_SCHEMA = kcu.TABLE_SCHEMA 
                                                                    AND c.TABLE_NAME = kcu.TABLE_NAME 
                                                                    AND c.COLUMN_NAME = kcu.COLUMN_NAME 
                                                                    AND c.TABLE_SCHEMA = '{self.database}'
                                                                    AND kcu.CONSTRAINT_NAME = 'PRIMARY'
                    WHERE 
                        c.TABLE_SCHEMA = '{self.database}'
                    ORDER BY 
                        c.TABLE_SCHEMA, c.TABLE_NAME, c.ORDINAL_POSITION;
                    """
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                lst = cursor.fetchall()
                lst_schemas = schemas_prettier(lst)
                self.schema_dictionary = lst_schemas

                self.table_names = [table['TableName'] for table in lst_schemas[self.database]['Tables']]

                return self.schema_dictionary
        except Exception as e:
            traceback.print_exc()
            return None

    def query_dataset(self, sql):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchall()
                if result:
                    df = pd.DataFrame(result)
                    df.columns = [desc[0] for desc in cursor.description]  # Set DataFrame column names
                    return df
                else:
                    return pd.DataFrame()  # Return an empty DataFrame if no data
        except Exception as e:
            traceback.print_exc()
            return None

    def execute_query(self, sql):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
            self.conn.commit()  # Commit changes to the database
        except Exception as e:
            traceback.print_exc()
            self.conn.rollback()  # Rollback changes if any error occurs

    def execute_multi_queries(self, queries):
        try:
            with self.conn.cursor() as cursor:
                for query in queries:
                    cursor.execute(query)
                self.conn.commit()  # Commit changes to the database
        except Exception as e:
            traceback.print_exc()
            self.conn.rollback()  # Rollback changes if any error occurs

    def queryDataset(self, sql):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                column_names = [desc[0] for desc in cursor.description]
                data = cursor.fetchall()
                df = pd.DataFrame(data, columns=column_names)

                # Extract the value of the first column and first row
                first_value = None
                if not df.empty:
                    first_value = str(df.iloc[0, 0])  # Convert first_value to text

                return df, first_value

        except Exception as e:
                traceback.print_exc()
                return None, None  # Return both DataFrame and first value as None in case of an error

    def queryOne(self, sql):
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                result = cursor.fetchone()
                if result:
                    return result[0]  # Return the first value in the row as is
                else:
                    return None
        except Exception as e:
            print(f"Error executing SQL query: {e}")
            return None

    def queryDataframe(self, sql):
        try:
            if self.conn is None:
                raise ValueError("Database connection is not initialized.")

            with self.conn.cursor() as cursor:
                cursor.execute(sql)
                column_names = [desc[0] for desc in cursor.description]
                data = [row for row in cursor.fetchall()]  # Convert fetched data to a list of tuples
                df = pd.DataFrame(data, columns=column_names)
                return df
        except Exception as e:
            # Log the error instead of printing directly
            traceback.print_exc()
            return None  # Return None in case of an error


