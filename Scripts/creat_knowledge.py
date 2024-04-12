## Pre-Creating knowledge of LOS
import snowflake.connector
import pandas as pd
from pathlib import Path
from dotenv import load_dotenv
import os
load_dotenv(override=True)
from openai import OpenAI




# Snowflake config
snowflake_user = os.getenv('SNOWFLAKE_USER')
snowflake_password = os.getenv('SNOWFLAKE_PASS')
snowflake_account = os.getenv('SNOWFLAKE_ACCOUNTID')
database = os.getenv('SNOWFLAKE_DATABASE')
schema = os.getenv('SNOWFLAKE_SCHEMA')
warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')

def get_3_data():
    """get Introduction LOS Summary"""
    df = {}
    try:
        conn = snowflake.connector.connect(       
            user=snowflake_user,
            password=snowflake_password,
            account=snowflake_account,
            warehouse=warehouse,
            database=database,
            schema=schema,
        )
        
        # run the sql query to get data from snowflake
        cursor = conn.cursor()
        sql = f"SELECT NAMEOFTOPIC, INTRODUCTION, LEARNINGOUTCOME, SUMMARY FROM CFA_COURSES ;"

        results = cursor.execute(sql)
        if results is not None:
            df = pd.DataFrame(results.fetchall())
            df.columns = ['Topic','Introduction', 'Learning outcomes', 'Summary']
        else:
            print('Fail to get data. Try again')
    except NameError as e:
        print(f'Program fail: {e}')
    finally:
        cursor.close()
        conn.close()

    return df

df = get_3_data()

def creat_knowledge(topic, introduction, summary, los):

    client = OpenAI()
    response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    response_format={ "type": "json_object" },
    messages=[
        {"role": "system", "content": "You are a helpful assistant to generate techincal note for CFA Refresher Readings articles."},
        {"role": "user", "content": f"## Topic\n{topic}\n\n## Introduction\n{introduction}\n\n## Summary\n{summary}\n\n## Learning Outcomes\n{los}\n\n---\n\nBased on the information provided, create a detailed technical note in Markdown format that covers the key aspects and insights of the topic."}
    ]
    )
    print(response.choices[0].message.content)