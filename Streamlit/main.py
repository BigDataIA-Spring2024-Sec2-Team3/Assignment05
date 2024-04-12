# Page to get the articles and parsing there LOS

import streamlit as st
import snowflake.connector
import pandas as pd
from pathlib import Path
import subprocess
from dotenv import load_dotenv
import os
load_dotenv(override=True)

# Snowflake config
snowflake_user = os.getenv('SNOWFLAKE_USER')
snowflake_password = os.getenv('SNOWFLAKE_PASS')
snowflake_account = os.getenv('SNOWFLAKE_ACCOUNTID')
database = os.getenv('SNOWFLAKE_DATABASE')
schema = os.getenv('SNOWFLAKE_SCHEMA')
warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')



# Streamlit UI
st.title("CreatingknowledgesummariesusingOpenAI'sGPT")

# user input file name:
input_string = st.text_input("Article Name split bt \',\':", "")

file_names =  [s.strip() for s in input_string.split(',')]

# trigher when click 
if st.button("retrive data"):
    if file_names:
        # connect to Snowflake
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
            file_name_holder = ','.join([f'\'{fn}\'' for fn in file_names])
            sql = f"SELECT NAMEOFTOPIC, INTRODUCTION, LEARNINGOUTCOME FROM CFA_COURSES WHERE NAMEOFTOPIC IN ({file_name_holder});"
            st.write(sql)
            results = cursor.execute(sql)
            if results is not None:
                df = pd.DataFrame(results.fetchall())
                df.columns = ['Introduction', 'Learning outcome', 'Title']
                st.dataframe(df)
            else:
                st.error('Fail to get data. Try again')
        except NameError as e:
            st.error(f'Program fail: {e}')
        finally:
            cursor.close()
            conn.close()




    #     # 显示查询结果
    #     if not df.empty:
    #         st.write("查询结果：")
    #         st.write(df)
            
    #         # 将查询结果保存到CSV文件中，作为后续处理的输入
    #         temp_file_path = Path("temp.csv")
    #         df.to_csv(temp_file_path, index=False)
            
    #         # 调用位于scripts文件夹下的Python脚本处理数据
    #         process_script_path = Path("scripts/process_data.py")
    #         subprocess.run(["python", process_script_path, temp_file_path], check=True)
            
    #         # 显示处理后的信息
    #         st.success("数据处理完成，请查看输出的txt文件。")
    #     else:
    #         st.warning("没有找到匹配的条目。")
    # else:
    #     st.error("请输入文件名。")
