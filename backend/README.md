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
  - [Models](#models)
    - [Company](#company)
    - [Employee](#employee)

## Installation

1. Clone the repository

```bash
git clone https://github.com/Polcsi/company-information-django.git
```

2. Create a virtual environment

```bash
python3 -m venv venv
```

3. Activate the virtual environment

```bash
source venv/bin/activate
```

4. Install the requirements

5. Run the migrations

```bash
python manage.py migrate
```

6. Run the server

```bash
python manage.py runserver
```

## Endpoints

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

### Companies

#### Create Company

| URL      | Method | Data Properties                          | Success Response                                          |
| -------- | ------ | ---------------------------------------- | --------------------------------------------------------- |
| /company | `POST` | **name**<br>**email**<br>**description** | **companyID**<br>**name**<br>**email**<br>**description** |

**Data Params**:

```json
{
  "name": "string",
  "email": "string",
  "description": "string"
}
```

#### Update Company

- **URL**

/api/companies/:id/

- **Method:**

`PUT`

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

- **URL**

  /api/companies/:id/

- **Method:**

  `DELETE`

- **Success Response:**

  - **Code:** 204 NO CONTENT <br />

#### Get Companies

- **URL**

  /api/companies/

- **Method:**

  `GET`

- **Success Response:**

  - **Code:** 200 OK <br />
  - **Content:**

  ```json
  [
    {
      "id": 1,
      "name": "string",
      "email": "string",
      "description": "string",
      "number_of_employees": "integer"
    }
  ]
  ```

### Employees

#### Create Employee

- **URL**

  /api/employees/

- **Method:**

  `POST`

- **Data Params**

  ```json
  {
    "name": "string",
    "age": "integer",
    "email": "string",
    "job": "string",
    "company": "integer"
  }
  ```

- **Success Response:** - **Code:** 201 CREATED <br /> - **Content:**
  `json
{
    "id": 1,
    "name": "string",
    "age": "integer",
    "email": "string",
    "job": "string",
    "company": "integer"
}
`

#### Update Employee

- **URL**

  /api/employees/:id/

- **Method:**

  `PUT`

- **Data Params**

  ```json
  {
    "name": "string",
    "age": "integer",
    "email": "string",
    "job": "string",
    "company": "integer"
  }
  ```

- **Success Response:**

  - **Code:** 200 OK <br />
  - **Content:**

  ```json
  {
    "id": 1,
    "name": "string",
    "age": "integer",
    "email": "string",
    "job": "string",
    "company": "integer"
  }
  ```

#### Delete Employee

- **URL**

  /api/employees/:id/

- **Method:**

  `DELETE`

- **Success Response:**

  - **Code:** 204 NO CONTENT <br />

#### Get Employees

- **URL**

  /api/employees/

- **Method:**

  `GET`

- **Success Response:**

  - **Code:** 200 OK <br />
  - **Content:**

  ```json
  [
    {
      "id": 1,
      "name": "string",
      "age": "integer",
      "email": "string",
      "job": "string",
      "company": "integer"
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
