# Airflow Core Components

## 1: Metadata Database

- Uses this to record every data regarding DAG runs and their status, timestamps, etc.
- This can be in MySQL, PostgreSQL, etc.
- Think of it as the Airflow's memory which it use to keep track like we use a calendar on important things like, task runs, dates and its status


## 2: The Scheduler

- The scheduler is responsible for running each DAG task at scheduled times.


## 3: DAG File Processor

- This is more like a sub-component of the scheduler.
- This parses the Python code file and serializes them into the metadata database. 

`Serialization`
- DAG, TASK, etc. are Python objects. 
- When the file is parsed, they need to be stored in the metadata database.
- Serialization is when those raw objects are converted into a storable format like JSON, Dicts, etc.
- This is useful to:
    - Improve performance. So webserver doesn't need to parse each DAG files each time.
    - Decopling. Scheduler only parses DAGs and Webserver displays them. If a DAG is broken, it won't affect the webserver crashes.


## 4: The Executor

- Executor only determines how to run the tasks. Whether it should be run parellely or sequentially, etc.


## 5: The Worker

- Responsible for executing the DAG tasks which is sent through the ***Executor***.


## 6: API Server

- Use to access Airflow UI, handle tasks.
- If you need to stop tasks, manually trigger, etc. for each action the API endpoint is creater via this API server.


## 7: The Queue

- A list of tasks waiting to be executed.
- Helps to manage the order of task execution.
