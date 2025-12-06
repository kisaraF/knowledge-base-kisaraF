# Randomized Sampling using `ORDER BY`

## Prompt

Assume there's a table in Snowflake with 10 million records. I need to sample a 10,000-record subset which covers randomized values from a specific columns. If    I use limit to get it, it will only select the first 10,000 rows without randomity in it. How do you do a randomized sampling using Snowflake SQL (similar to shuffle in NumPy)?

## Answer

To perform a randomized sampling of 10,000 records from a table in Snowflake, you can use the `TABLESAMPLE` clause or the `ORDER BY RANDOM()` method. Since you want a specific number of records (10,000) and a randomized selection, the `ORDER BY RANDOM()` approach is more suitable. Here’s how you can do it:

**Using `ORDER BY RANDOM()`**


You can use the following SQL query to achieve this:

```sql
SELECT *
FROM your_table_name
ORDER BY RANDOM()
LIMIT 10000;
```

# Randomized Sampling using `TABLESAMPLE`

## Answer

Performance Consideration:

Keep in mind that using `ORDER BY RANDOM()` can be resource-intensive, especially with large datasets, as it requires sorting the entire dataset randomly. If performance is a concern, consider using a different approach, such as:

Using `TABLESAMPLE` (if applicable)


If your table is large and you want a more efficient way to sample, you can use the `TABLESAMPLE` clause, but note that it does not guarantee an exact number of rows:

```sql
SELECT *
FROM your_table_name
TABLESAMPLE (0.1) -- Adjust the percentage as needed
LIMIT 10000;
```

Conclusion:

For a precise random sample of 10,000 records, the `ORDER BY RANDOM()` method is the most straightforward approach. However, be mindful of performance implications on large datasets. Always test your queries to ensure they meet your performance and accuracy requirements.