# PIVOT in SQL

Pivot is a much needed transformation to keep in practice as it's often needed for analysis work

A sample query is as follows,

```
SELECT *
FROM (
    SELECT country, year, sales
    FROM sales_data
)
PIVOT (
    SUM(sales) AS total_sales
    FOR year IN (2020, 2021, 2022)
);
```

## Tidbits to Memorize

- What are we summarizing? -> `SUM(column)` // The aggregate column
- Which column’s values become new columns? -> `FOR <some_column>`
- Which specific values should become columns? -> `IN (value1, value2, …)`


_Another small example_

| country | year | sales |
|---------|------|-------|
| US      | 2020 | 100   |
| US      | 2021 | 150   |
| UK      | 2020 | 200   |
| UK      | 2021 | 340   |

```
SELECT *
FROM sales_data
PIVOT (
    SUM(sales) FOR year IN (2020, 2021)
);
```

`Result`

| country | 2020 | 2021 |
|---------|------|------|
| US      | 100  | 150  |
| UK      | 200  | 340  |
