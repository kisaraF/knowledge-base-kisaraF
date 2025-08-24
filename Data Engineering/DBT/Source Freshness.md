# Sources YAML 

```
sources:
  - name: btc_raw
    database: btc_db
    schema: btc_schema
    tables:
      - name: btc_landing
        freshness:
          warn_after:
            count: 1
            period: hour
          error_after:
            count: 24
            period: hour
        loaded_at_field: BLOCK_TIMESTAMP
```

- Here what we are doing is defining the source in a YAML file.
- By doing this we keep source modular. Meaning wherever we need to query data from the source, we can do it as the following:
    - ``` select * from {{ source('btc_raw','btc_landing') }} ```
    - This way we make sure, in future if the source schema or  table is changed, it won't affect the models, where we'd have to go to each single file to replace the source.


### Source Freshness

- To check the source freshness we use the following command:
    - ``` dbt source freshness ```
- This is used to check how recent the data is. In our `.yml` file we have made sure,
    - If the identifier column (`BLOCK_TIMESTAMP` in this case) has a new record or if it's latest record is older than 1 hour from current time, to push a ***Warning***
    - But if the latest record is older than 24 hours we have made sure to push an ***Error***.

- In the following Screenshot, you can see that it gives an error.

<img width="574" alt="source-freshness-ss" src="https://github.com/user-attachments/assets/ba34f4e1-0abf-4717-a577-dc77b0267655">