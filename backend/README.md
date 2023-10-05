# Python Django Backend Documentation

This is a Django backend application which is responsible for the following tasks:

- Create, update, delete companies
- Create, update, delete employees
- Read companies and employees

## Table of Contents

- [Python Django Backend Documentation](#python-django-backend-documentation)
  - [Installation](#installation)
  - [Endpoints](#endpoints)
    - [Companies](#companies)
      - [Create Company](#create-company)
      - [Update Company](#update-company)
      - [Delete Company](#delete-company)
      - [Get Companies](#get-companies)
    - [Employees](#employees)
      - [Create Employee](#create-employee)
      - [Update Employee](#update-employee)
      - [Delete Employee](#delete-employee)
      - [Get Employees](#get-employees)
    - [Combined Endpoints](#combined-endpoints)
      - [Create Company with list of employees](#create-company-with-list-of-employees)
      - [Update Company with list of employees](#update-company-with-list-of-employees)
      - [Get Companies and employees](#get-companies-and-employees)
  - [Models](#models)
    - [Company](#company)
    - [Employee](#employee)

## Installation

1. Clone the repository

```bash
git clone https://github.com/Polcsi/company-information-django.git
```

3. Go to the backend folder

```bash
cd company-information-django/backend
```

3. Create a virtual environment

```ps
python3 -m venv venv
```

4. Activate the virtual environment

_**Windows**_:

```bash
.venv/Scripts/activate
```

5. Install the requirements

```ps
pip install django
pip install djangorestframework
```

6. Run the migrations

```ps
python manage.py migrate
```

6. Run the server

```ps
python manage.py runserver
```

## Endpoints

### Companies

| Endpoint      | Method                                                    | Description                              |
| ------------- | --------------------------------------------------------- | ---------------------------------------- |
| /company      | <span style="color: yellow;font-weight: bold">POST</span> | [Create a new company ](#create-company) |
| /company/:id/ | <span style="color: cyan;font-weight: bold">PUT</span>    | [Update a company](#update-company)      |
| /company/:id/ | <span style="color: red;font-weight: bold">DELETE</span>  | [Delete a company](#delete-company)      |
| /company      | <span style="color: lime;font-weight: bold">GET</span>    | [Get all companies](#get-companies)      |

#### Create Company

| URL      | Method |
| -------- | ------ |
| /company | `POST` |

**Data Params**:

```json
{
  "name": "string",
  "email": "string",
  "description": "string"
}
```

**Success Response:**

- **Code:** 201 CREATED <br />
- **Content:**

```json
{
  "id": 1,
  "name": "string",
  "email": "string",
  "description": "string",
  "number_of_employees": "integer"
}
```

#### Update Company

| URL           | Method |
| ------------- | ------ |
| /company/:id/ | `PUT`  |

- **Data Params**

```json
{
  "name": "string",
  "email": "string",
  "description": "string",
  "number_of_employees": "integer"
}
```

- **Success Response:**

  - **Code:** 200 OK <br />
  - **Content:**

  ```json
  {
    "id": 1,
    "name": "string",
    "email": "string",
    "description": "string",
    "number_of_employees": "integer"
  }
  ```

#### Delete Company

| URL           | Method   |
| ------------- | -------- |
| /company/:id/ | `DELETE` |

- **Success Response:**

  - **Code:** 204 NO CONTENT <br />

#### Get Companies

| URL      | Method |
| -------- | ------ |
| /company | `GET`  |

- **Success Response:**

  - **Code:** 200 OK <br />
  - **Content:**

```json
[
  {
    "id": "number",
    "name": "string",
    "email": "string",
    "description": "string"
  }
]
```

### Employees

| Endpoint      | Method                                                    | Description                                  |
| ------------- | --------------------------------------------------------- | -------------------------------------------- |
| /employee/    | <span style="color: yellow;font-weight: bold">POST</span> | [Create a new employee](#create-employee)    |
| /employee/:id | <span style="color: cyan;font-weight: bold">PUT</span>    | [Update an employee](#update-employee)       |
| /employee/:id | <span style="color: red;font-weight: bold">DELETE</span>  | [Delete an employee](#delete-employee)       |
| /employee/    | <span style="color: lime;font-weight: bold">GET</span>    | [Get all employees](#get-employees)          |
| /employee/:id | <span style="color: lime;font-weight: bold">GET</span>    | [Get an employee by id](#get-employee-by-id) |

#### Create Employee

| URL       | Method |
| --------- | ------ |
| employee/ | `POST` |

- **Data Params**

  ```json
  {
    "company": "integer",
    "name": "string",
    "age": "integer",
    "email": "string",
    "job": "string",
    "cv": "string"
  }
  ```

- **Success Response:** - **Code:** 201 CREATED <br /> - **Content:**

```json
{
  "employeeID": "nubmer",
  "companyID": "number",
  "name": "string",
  "email": "string",
  "age": "number",
  "job": "string",
  "cv": "string"
}
```

#### Update Employee

| URL           | Method |
| ------------- | ------ |
| employee/:id/ | `PUT`  |

- **Data Params**

  ```json
  {
    "companyID": "integer",
    "name": "string",
    "age": "integer",
    "email": "string",
    "job": "string",
    "cv": "string"
  }
  ```

- **Success Response:**

  - **Code:** 200 OK <br />
  - **Content:**

```json
{
  "employeeID": "nubmer",
  "companyID": "number",
  "name": "string",
  "email": "string",
  "age": "number",
  "job": "string",
  "cv": "string"
}
```

#### Delete Employee

| URL           | Method   |
| ------------- | -------- |
| employee/:id/ | `DELETE` |

- **Success Response:**

  - **Code:** 204 NO CONTENT <br />

#### Get Employees

| URL       | Method |
| --------- | ------ |
| employee/ | `GET`  |

- **Success Response:**

  - **Code:** 200 OK <br />
  - **Content:**

```json
[
  {
    "employeeID": "nubmer",
    "companyID": "number",
    "name": "string",
    "email": "string",
    "age": "number",
    "job": "string",
    "cv": "string"
  }
]
```

#### Get Employee by id

| URL           | Method |
| ------------- | ------ |
| employee/:id/ | `GET`  |

- **Success Response:**

  - **Code:** 200 OK <br />
  - **Content:**

```json
{
  "employeeID": "nubmer",
  "companyID": "number",
  "name": "string",
  "email": "string",
  "age": "number",
  "job": "string",
  "cv": "string"
}
```

## Combined Endpoints

| Endpoint                  | Method                                                    | Description                                                                           |
| ------------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| company/add_employees     | <span style="color: yellow;font-weight: bold">POST</span> | [Create a new company with list of employees](#create-company-with-list-of-employees) |
| company/:**id**/employees | <span style="color: cyan;font-weight: bold">PUT</span>    | [Update a company and employees](#update-company-with-list-of-employees)              |
| company/:**id**/employees | <span style="color: lime;font-weight: bold">GET</span>    | [Get all companies with list of employees](#get-companies-and-employees)              |

#### Create Company with list of employees

| URL                   | Method |
| --------------------- | ------ |
| company/add_employees | `POST` |

- **Data Params**

```json
{
  "name": "string",
  "email": "string",
  "description": "string",
  "employees": [
    {
      "name": "string",
      "age": "integer",
      "email": "string",
      "job": "string",
      "cv": "string"
    }
  ]
}
```

### Update Company with list of employees

| URL                       | Method |
| ------------------------- | ------ |
| company/:**id**/employees | `PUT`  |

- **Data Params**

```json
{
  "name": "string",
  "email": "string",
  "description": "string",
  "employees": [
    {
      "employeeID": "number",
      "name": "string",
      "age": "integer",
      "email": "string",
      "job": "string",
      "cv": "string"
    }
  ]
}
```

### Get Companies and employees

| URL                       | Method |
| ------------------------- | ------ |
| company/:**id**/employees | `GET`  |

- **Success Response:**

  - **Code:** 200 OK <br />
  - **Content:**

```json
[
  {
    "companyID": "number",
    "name": "string",
    "email": "string",
    "description": "string",
    "employees": [
      {
        "employeeID": "nubmer",
        "name": "string",
        "email": "string",
        "age": "number",
        "job": "string",
        "cv": "string"
      }
    ]
  }
]
```

## Models

### Company

| Field         | Type                       | Description                           |
| ------------- | -------------------------- | ------------------------------------- |
| **companyID** | **Primary key**, (integer) | The id of the company                 |
| name          | string                     | The name of the company               |
| email         | string                     | The email address of the company      |
| description   | string, (optional)         | A short description about the company |

### Employee

| Field          | Type                       | Description                                    |
| -------------- | -------------------------- | ---------------------------------------------- |
| **employeeID** | **Primary key**, (integer) | The id of the employee                         |
| **companyID**  | **ForeignKey**, (integer)  | The id of the company where the employee works |
| name           | string                     | The name of the employee                       |
| age            | integer                    | The age of the employee                        |
| email          | string                     | The email address of the employee              |
| job            | string                     | The job of the employee                        |
| cv             | string, (optional)         | The cv of the employee (optional)              |

> **Note:** The cv field is optional

> **Note:** Job field is a string because it can be a string like `Software Engineer`, `Data Scientist`, `Product Manager`, `Data Analyst`, `Software Developer`, `UI/UX Designer`, `Manager`, `Software Tester` or `Accountant`.
