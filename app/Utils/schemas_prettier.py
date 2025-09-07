def schemas_prettier(data):
    result = {}

    for row in data:
        schema_name, table_name, column_name, data_type, pk_name, auto_increment = row
        if schema_name not in result:
            result[schema_name] = {"Tables": []}

        table_info = next((table for table in result[schema_name]["Tables"] if table["TableName"] == table_name), None)

        if table_info is None:
            table_info = {"TableName": table_name, "Columns": []}
            result[schema_name]["Tables"].append(table_info)

        is_pk = True if pk_name is not None else False
        python_data_type = None
        # data_type = str(data_type).split("\'")[1]

        if data_type in ['int', 'smallint', 'bigint', 'tinyint']:
            python_data_type = 'int'
        elif data_type in ['varchar', 'char', 'text']:
            python_data_type = 'string'
        elif data_type in ['float', 'decimal', 'numeric']:
            python_data_type = 'float'
        elif data_type in ['date', 'datetime', 'timestamp']:
            python_data_type = 'datetime'  # Using datetime from datetime module

        # Mapping auto_increment value
        is_auto_increment = True if auto_increment == 'YES' else False

        table_info["Columns"].append({
            "ColumnName": column_name,
            "DataType": python_data_type,
            "IsPk": is_pk,
            "IsAutoIncrement": is_auto_increment
        })
    return result
