# DECODE (Snowflake)

## Prompt: 

How to use DECODE function in a select statement given as:
```sql
SELECT 
    DECODE(STATUS,''ACTIVE'' ,''Y'',''INACTIVE'' ,''N'') as OUT_STATUS
```

## Answer:

It is more like a case statement but concise. Nothing fancy. For example, refer to the sample below:

<img width="787" height="613" alt="Image" src="https://github.com/user-attachments/assets/499b47aa-5e81-467f-855b-3143841b6e3a" />

In the example provided above:

it checks for the `Status` column first, then in that column,
- If the value is `ACTIVE` -> `Y` will be displayed,
- If the value is `INACTIVE` -> `N` will be displayed