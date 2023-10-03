import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { ToastContainer } from "react-toastify";
import { Suspense, lazy } from "react";
import Background from "./layout/Background";
// lazy load pages
const CreateCompanyWithEmployees = lazy(
  () => import("./pages/CreateCompanyWithEmployees")
);
const ErrorPage = lazy(() => import("./pages/ErrorPage"));
const ResultsPage = lazy(() => import("./pages/ResultsPage"));
const MainPage = lazy(() => import("./pages/MainPage"));
const Companies = lazy(() => import("./pages/Companies"));
const SingleCompany = lazy(() => import("./pages/SingleCompany"));

const App = () => {
  return (
    <>
      <Router>
        <Suspense
          fallback={
            <Background>
              <div>Loading...</div>
            </Background>
          }
        >
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
        </Suspense>
      </Router>
      <ToastContainer />
    </>
  );
};

export default App;
