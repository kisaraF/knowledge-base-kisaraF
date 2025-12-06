# Using Regex Patterns inside `COPY INTO`

## Case:

I have an external stage which has a folder as "New Folder" without any underscroes (contains whitespace). When I try to execute a copy into statement like from @database.stage_name/foo/New Folder/date_1 it doesn't work. How to fix this?

## Answer:

```sql
COPY INTO PROD_DLK_DB.EXT_TABS.TEST_AIRTEL_HIS_X
FROM @COMMON_OBJECTS.MANUAL_RECOVERIES_AWS/Airtel/Airtel_History_Loading/
FILE_FORMAT = (TYPE = 'CSV' FIELD_OPTIONALLY_ENCLOSED_BY = '"' SKIP_HEADER = 1)
PATTERN = '.*R1000016_TransactionReport_B_.*\.csv'
ON_ERROR = 'CONTINUE';
```
- Else can use the AWS CLI. But if the access to AWS CLI is not available the above can be used

