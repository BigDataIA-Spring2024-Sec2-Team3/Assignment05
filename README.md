# Assignment05

## Related Link

[![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=1_EVY7qw2AOmJMTH19rpEHbZXWMg41mmHHT5Jv6ofbEc):link for codelab

[![Streamlit](https://camo.githubusercontent.com/2d35d09dad4cee1f9f94d8813d50c187602f2d319d36553cc576f827393182a0/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f53747265616d6c69742d4646344234423f7374796c653d666f722d7468652d6261646765266c6f676f3d53747265616d6c6974266c6f676f436f6c6f723d7768697465)]():link for streamlit service



## Technologies Used

[![Python](https://camo.githubusercontent.com/bb64b34d04a01cfa79658e2704085740d88e209c21905d0f5b55ebc87a83aa3a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d4646443433423f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d626c7565)](https://www.python.org/) [![Docker](https://camo.githubusercontent.com/143024f77b90a42cca6ecc238a7d00d7d72c216cdacd319939d2d9d26748120a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446f636b65722d2532333234393645443f7374796c653d666f722d7468652d6261646765266c6f676f3d446f636b657226636f6c6f723d626c7565266c6f676f436f6c6f723d7768697465)](https://www.docker.com/) [![Google Cloud](https://camo.githubusercontent.com/90e06e46d213cea885f8f8ad83ba8dd50ea199b6ab308f9cc6fad723612aa53c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f476f6f676c655f436c6f75642d2532333432383546342e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d676f6f676c652d636c6f7564266c6f676f436f6c6f723d7768697465)](https://cloud.google.com/) ![Snowflake](https://camo.githubusercontent.com/0dbe98edfb3f64ca11a164e3e6bb92b5c33fe90726c1dd16ec29d6d218c77909/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f736e6f77666c616b652d2532333432383546343f7374796c653d666f722d7468652d6261646765266c6f676f3d736e6f77666c616b65266c696e6b3d68747470732533412532462532467777772e736e6f77666c616b652e636f6d253246656e2532462533465f6761253344322e34313530343830352e3636393239333936392e313730363135313037352d313134363638363130382e313730313834313130332532365f676163253344312e3136303830383532372e313730363135313130342e436a304b4351694168384f74426843514152497341496b576236386a354e7854366c716d4856626147647a51594e537a37553063665243732d53546a785a746750635a45562d325673322d6a38484d614171507345414c775f776342266c6f676f436f6c6f723d7768697465) [![FastAPI](https://camo.githubusercontent.com/d9fcef32b07a52e62acde87c779d3a33b6c0d7111149031c2cef1ec24f9c802c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f666173746170692d3130393938393f7374796c653d666f722d7468652d6261646765266c6f676f3d46415354415049266c6f676f436f6c6f723d7768697465)](https://fastapi.tiangolo.com/) 

## Problem Statement

As part of the "Development of a Structured Database and Text Extraction System for Finance Professional Development Resources," we are tasked with creating a comprehensive system that leverages cutting-edge technologies to address the ongoing challenge of effectively curating and utilizing vast amounts of professional development content from various sources. The finance industry, with its depth and complexity of content, particularly benefits from systems that can automate and enhance the retrieval, understanding, and interaction with professional and developmental materials.

## Project Goals

The objective of this project is to design and implement a structured database system that uses Models as a Service APIs to build intelligent applications capable of handling complex knowledge retrieval and question/answer tasks. This system will be developed using Pinecone and OpenAI's APIs to harness the power of vector databases and advanced natural language processing models.

The key components of the project include:

1. **Creation of Knowledge Summaries**: Utilizing OpenAI's GPT to generate comprehensive summaries from the CFA Institute’s professional development materials which include introductions, summaries, and Learning Outcome Statements (LOS).
2. **Development of a Contextual Knowledge Base**: Constructing a dynamic Q/A database that not only stores information but also provides contextual answers based on the content extracted and summarized from the designated resources.
3. **Implementation of a Vector Database**: Using Pinecone to manage and retrieve knowledge pieces efficiently, enabling the system to find and answer complex queries with high accuracy and speed.
4. **Single-Click Operational Interface**: Designing a user-friendly API and interface that allows end-users, specifically financial analysts, to interact with the system seamlessly. This interface will support single-click operations to execute tasks such as data extraction, summary generation, and query handling.
5. **Automation and Scalability**: Automating the entire process using AirFlow to ensure that the system is not only effective in real-time but also scalable for future expansions and capable of integrating additional data sources and analytical tools.



## Setup and Execution

### **Before running :**

Python: Ensure Python is installed on your system.

Docker: Ensure Docker-desktop is installed on your system.

Google Cloud Platform: Create a Google Cloud Engine. Ensure you have the necessary credentials and configurations set up in the configurations.properties file.

### Run the code:

#### prepare the environment

Clone the repository to get all the source code on your machine.

Use `source /venv/bin/activate` to activate the environment.

Create a `.env` file in the root directory with the following variables:

```
[snowflake]
SNOWFLAKE_ACCOUNT=
SNOWFLAKE_USER=
SNOWFLAKE_PASSWORD=
SNOWFLAKE_WAREHOUSE=
SNOWFLAKE_DATABASE=
SNOWFLAKE_SCHEMA=
[API]
OPENAI_API_KEY=
PINECONE_API_KEY=
```

#### prepare the Q/A bank and tech note

Run the scripts with questions example files to get the Q/A bank.

Run jupyternote files to prepare the the technical note.

#### Make your questions  

Once you have set up your environment variables and knowledage base, use `make build-up` to create the docker image and run the streamlit.

Access the Streamlit UI by navigating to [0.0.0.0:8080]() in you browser and input your questions.



## Program Structure

```
📦 Assignment05
├── Diagrams
│   ├── CFA.png
│   ├── Data Architecture.ipynb
│   ├── docker.png
│   ├── fastapi.png
│   ├── openai.png
│   ├── pydantic-logo.png
│   ├── rag-based_openai_data_architecture.png
│   ├── snowflake.png
│   ├── sqlalchemy.png
│   └── streamlit.png
├── FastAPI
│   ├── dockerfile
│   ├── main.py
│   └── requirements.txt
├── JupyterNotebook
│   ├── DataValidation.ipynb
│   ├── Upload_clean_webscrape_data.ipynb
│   └── step1.ipynb
├── README.md
├── Scripts
│   ├── Web_Scraping.py
│   └── creat_knowledge.py
├── Streamlit
│   ├── __init__.py
│   ├── dockerfile
│   ├── main.py
│   ├── pages
│   │   └── 1_Data_Querying.py
│   └── requirements.txt
├── data
│   ├── Validation_data.csv
│   ├── cfa_data.csv
│   └── items.csv
├── requirements.txt
└── utils
    └── URLclass.py
```


## Learning Outcomes

**By completing this assignment, you will:**

**Intelligent Application Development:**

- Develop an understanding of how to use Models as a Service APIs to create intelligent applications that can perform complex knowledge retrieval and Q/A tasks.
- Gain experience in leveraging advanced natural language processing models for generating knowledge summaries and contextual question-answering systems.

**Vector Database Utilization:**

- Learn to implement and manage a vector database using Pinecone to efficiently handle and retrieve large datasets for dynamic query answering.
- Understand the principles of vector space modeling and its application in real-world problem-solving scenarios within the finance sector.

**Knowledge Base Construction:**

- Construct a knowledge base using GPT from OpenAI for summarizing complex financial topics and generating relevant question-answer pairs that aid in professional development and learning.
- Employ techniques to chunk and store processed data into Pinecone, ensuring efficient data retrieval for question answering and analysis.

**Practical Application of Theoretical Knowledge:**

- Apply theoretical knowledge from finance and analytics to build practical solutions that can be operationalized within an enterprise context, enhancing the decision-making and learning process for financial analysts.
- Evaluate the effectiveness of different technological approaches in real enterprise scenarios through structured experiments and analysis.

**Professional Skills Development:**

- Enhance project management and teamwork skills by collaborating on a multi-component system involving various technologies and platforms.
- Develop a professional approach to designing, documenting, and presenting technology solutions tailored to specific user needs within the finance industry.

## Team

| Name         | NUID      |
| ------------ | --------- |
| Dongyu Liu   | 002837324 |
| Ekta Bhatia  | 002767736 |
| Parth Kalani | 002766306 |
| Sumit Sharma | 002778911 |
