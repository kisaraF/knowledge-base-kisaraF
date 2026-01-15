# What is this `adapter.dispatch()` in dbt macros?

In dbt you can write macros which are more like reusable code snippets that you don't need to repeat on each model they are being used to improve maintainability and code quality with DRY concepts.

And dbt has an option as `adapter.dispatch()` when defining a macro. This is extremely useful when you want portability in your macros. Especially when migrating warehouses or when doing distribution of models (as packages maybe).

What it does for you is, imagine if you have a string date column in a model. And in each dialect of SQL, converting a string date like "yyyymmdd" is different. So for that reason we can use `adapter.dispatch()`.

First what to do is, define the adapter method like below

```sql
{% macro base_select_source() %}
    {{ return(adapter.dispatch('base_select_source', '<project-name>')()) }}
{% endmacro %}
```
This will confirm which adapter you are using; whether it's Databricks, Postgres or Snowflake, etc.

Then you can have a multiple versions of this macro for each adapter like below

```sql
{% macro databricks__base_select_source() %}
...
{% endmacro %}

{% macro snowflake__base_select_source() %}
...
{% endmacro %}

{% macro default__base_select_source() %}
...
{% endmacro %}
```

If your adapter is Databricks, then it will pick Databricks, if it's Snowflake, it will pick the Snowflake specific macro version. And finally using a `default__macro_name` just as a fallback. If this isn't provided then it will error out. _For example: if you use this macro on a duckdb adapter and if it doesn't has a specific macro then, and there's no default, this will fail_

## Calling the macro

This is the best part about this. When calling the macro, you'd just call it using the name you gave at the "adapter.dispatch()" snippet. Which is `base_select_source()`

```sql
SELECT 
    {{ base_select_source() }}
FROM <table_A>
```