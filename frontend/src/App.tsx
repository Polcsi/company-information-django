import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { ToastContainer } from "react-toastify";
// import pages
import CreateCompanyWithEmployees from "./pages/CreateCompanyWithEmployees";
import ErrorPage from "./pages/ErrorPage";
import ResultsPage from "./pages/ResultsPage";
import MainPage from "./pages/MainPage";
import Companies from "./pages/Companies";
import SingleCompany from "./pages/SingleCompany";

const App = () => {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/companies" element={<Companies />} />
          <Route path="/companies/:id" element={<SingleCompany />} />
          <Route
            path="/create-company"
            element={<CreateCompanyWithEmployees />}
          />
          <Route path="results" element={<ResultsPage />} />
          <Route path="/*" element={<ErrorPage />} />
        </Routes>
      </Router>
      <ToastContainer />
    </>
  );
};

export default App;
