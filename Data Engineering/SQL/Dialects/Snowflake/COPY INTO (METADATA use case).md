# COPY INTO (`METADATA` use case)

## Prompt: 

I'm using a copy into command to get data from a file in S3 location in snowflake. My staging table has a column as file_name. In the data file in S3 there's no such column. I need to add the name of the file to the column when using copy into to ingest data. I heard that 

```sql
COPY INTO table1 FROM @stage1
MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE
INCLUDE_METADATA = (
    ingestdate = METADATA$START_SCAN_TIME, filename = METADATA$FILENAME);

-- can be used to do this. The following is how my copy into command is in right now:

copy into <staging_table> ( 
        col_1,
        col_2,
        file_name,
        col_3,
        col_4
        ) 
        from 
        ( 
        select 
        $1::VARCHAR(200) , 
        $2::VARCHAR(200) ,
        <for_file_name> 
        $3::VARCHAR(200) ,
        FROM @<stage_to_be_inserted> )
        file_format = (skip_header = 1)
        FORCE = TRUE
        ON_ERROR = 'CONTINUE'
        purge = false;
```

How do I use the meta data option to do this with the current query I have. Can you re-write it?

Also should I add that before options like file_name or is there a specific order?

## Answer:

To include the filename as part of your `COPY INTO` command in Snowflake, you can utilize the `INCLUDE_METADATA` option as you mentioned. You will need to adjust your `COPY INTO` command to include the metadata for the filename directly in the `SELECT` statement.

Here’s how you can rewrite your `COPY INTO` command to include the filename:

```sql
COPY INTO <staging_table> ( 
        col_1,
        col_2,
        file_name,
        col_3,
        col_4
        ) 
FROM 
(
    SELECT 
        $1::VARCHAR(200) AS col_1, 
        $2::VARCHAR(200) AS col_2,
        METADATA$FILENAME AS file_name,  -- Include the filename from metadata
        $3::VARCHAR(200) AS col_3,
        $4::VARCHAR(200) AS col_4
    FROM @<stage_to_be_inserted>
) 
FILE_FORMAT = (skip_header = 1)
FORCE = TRUE
ON_ERROR = 'CONTINUE'
PURGE = FALSE;
```

#### Key Changes:

1. **Include Filename**: The `METADATA$FILENAME` is used directly in the `SELECT` statement to populate the `file_name` column.
2. **Column Order**: The order of the columns in the `COPY INTO` command should match the order in the `SELECT` statement. Ensure that the columns in the `COPY INTO` clause correspond correctly to the selected columns.

#### Additional Notes:

- The `INCLUDE_METADATA` option is not explicitly required in this case since you are directly selecting the metadata in the `SELECT` statement.
- Ensure that the data types in the `SELECT` statement match the data types defined in your staging table.

This should allow you to successfully ingest the data while also capturing the filename from the S3 location. If you have any further questions or need additional assistance, feel free to ask!