# dbt + Snowflake Learning Project
This project is a hands-on learning experience with dbt (data build tool) and Snowflake. It includes setting up the environment, configuring dbt, creating and transforming models, using macro functions, applying tests, and deploying models using Airflow.

## Table of Contents
- [Setup dbt + Snowflake](#setup-dbt--snowflake)
- [Configure dbt_project.yml and Packages](#configure-dbt_projectyml-and-packages)
- [Create Source and Staging Tables](#create-source-and-staging-tables)
- [Transformed Models (Fact Tables, Data Marts)](#transformed-models-fact-tables-data-marts)
- [Macro Functions](#macro-functions)
- [Generic and Singular Tests](#generic-and-singular-tests)
- [Deploy Models Using Airflow](#deploy-models-using-airflow)
- [Lessons learnt](#lessons-learnt)
- [Credit](#credits)
- [Restriction](#restriction)
- [Disclaimer](#disclaimer)

## Built with:
![dbt](https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white)
![snowflake](https://img.shields.io/badge/Snowflake-29B5E8.svg?style=for-the-badge&logo=Snowflake&logoColor=white)
![Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE.svg?style=for-the-badge&logo=Apache-Airflow&logoColor=white)
## Setup dbt + Snowflake

1. **Install dbt**: Follow the [official dbt installation guide](https://docs.getdbt.com/docs/about-setup) to install dbt on your local machine.
2. **Snowflake Account**: Ensure to have access to a Snowflake account. 
3. **Set Up Connection**: Configure the connection to Snowflake by setting up your `profiles.yml` file with the necessary Snowflake credentials.

## Configure dbt_project.yml and Packages

1. **dbt_project.yml**: Configure the `dbt_project.yml` file to define the project's configuration, such as project name, version, and profile.
2. **Install Packages**: Use the `packages.yml` file to define and install any required dbt packages.

## Create Source and Staging Tables
- Source Tables: Define the source tables.
- Staging Tables: Create staging models in the `models/staging` directory to clean and prepare your source data for further transformations.

## Transformed Models (Fact Tables, Data Marts)
Data Marts: Create data marts in the models/marts directory to organize data in a way that is useful for analysis and reporting.

## Macro Functions
Create reusable SQL snippets using dbt's Jinja-based macros. Store these macros in the macros directory.

## Generic and Singular Tests
- Generic Tests: Apply built-in or custom generic tests to ensure data quality.
- Singular Tests: Write singular tests to validate specific business logic or data constraints.

## Deploy Models Using Airflow
1. Setup Airflow: Install and configure Apache Airflow.
2. Create DAGs: Define Directed Acyclic Graphs (DAGs) in Airflow to orchestrate the execution of dbt models.
3. Deploy: Use Airflow to schedule and run your dbt transformations.

## Lessons learnt
- During the configuration, Snowflake account name should be formatted as `ORGNAME-ACCNAME` ([refer to the documentation here](https://docs.snowflake.com/en/user-guide/admin-account-identifier)).
- Ensure the `dbt_project.yml` file is located at a fixed path to prevent errors when importing the DAG into Airflow.
- Debugged an Airflow failure caused by issues reading the audit log.

## Credits
Code along with Jayzern

## Restriction
The code is provided for educational purposes and demonstration use only. 

## Disclaimer
This code is provided "as is" without warranty of any kind, and I am not liable for any issues that arise from its use. While you are welcome to learn from it, please do not copy or distribute it for your own coursework or assignments without permission.

