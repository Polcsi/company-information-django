# This is a React Application which collect company and employees information

Application seperated three pages:

- "/" home page
- "/results" where after the form submission the data going to be represented
- "/\*" error page: when the user navigates to a non-implemented page

The pages have very clean looking and designed make the page easy to use for the user. Every single page is responsive so it will look good on mobile and large screens.

---

### Home Page "/"

The home page includes a company form section where the user be able to give the company name, email address, number of employees and a short description about company. Furthermore there is an employees section on the home page which is dinamically rendered it depends on how many number of employees were given in the comapny section. In the employees section the user will be able to give the employee name, age, email, job and cv pdf file. The user can submit the forms with the submit button in the company section. After the user clicks on the submit button and all the required fields is filled then it navigates to the results page where the entered values will be represented.

![home-page-image](/docs/images/main-page.png)

---

### Results Page "/results"

The results page represents the submitted data. There is a section for company information and there is a section for employees. The page left bottom corner there is a button which navigates back to the home page.

![results-page-image](/docs/images/results-page.png)

---

### Error Page "/\*"

Error page just simply says that "404, page not found" on the page and provides a button for the user to be able to navigate back to the home page.

![error-page-image](/docs/images/error-page.png)
