# Delta Lake

- Delta lake is an open source `storage layer` that brings ACID transactions to data lake.
- It maintains this compliance through a metadata transaction log. It sits on top of the data lake storage (S3, ADLS, HDFS) and manages a transaction log (_delta_log) to ensure consistency and reliability.
- Has many features like:
    - ACID transactions
    - Tune travel
    - Schema enforcement & evolution
    - DML operations


## Delta Table

- A table which has delta lake format. 
-  `Delta lake` is the __technology__ which gives the ACID, time travel, etc. whereas `Delta table` is the __dataset__ managed by Delta Lake. 
- A delta table will always have delta lake (format) but there NEVER is a delta lake wihout a delta table.

```
Analogy:
Think of Delta Lake as the engine or framework that powers ACID-compliant storage, and Delta Tables as the cars built using that engine.
```

## Delta table API vs `spark.read.format("delta")`

- This is a distinction which can be best described as managing vs reading delta tables.

- `spark.read.format("delta")` method gives you the ability to read the delta table into a dataframe and do basic operations.

- Delta table API lets you access to the full dela features such as time travel, ACID, update & upserts, etc.

- If you need to delete some records you can do that directly using the API. If used the normal method, you'd have to first read it -> filter it -> overwrite to save. 

- But if the table is in billions of records, it's not efficient and cost effective to overwrite whereas it's extremely useful that delta table can interact directly. 
