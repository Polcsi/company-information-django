import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { ToastContainer } from "react-toastify";
// import pages
import CreateCompanyWithEmployees from "./pages/CreateCompanyWithEmployees";
import ErrorPage from "./pages/ErrorPage";
import ResultsPage from "./pages/ResultsPage";
import MainPage from "./pages/MainPage";

const App = () => {
  return (
    <>
      <Router>
        <Routes>
          <Route path="/" element={<MainPage />} />
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
