import React from "react";
import Background from "../layout/Background";
import HomeButton from "../components/buttons/HomeButton";
import CompanyList from "../components/CompanyList";

const Companies = () => {
  return (
    <Background className="companies-page-layout">
      <aside className="section card">
        <header>
          <h1>Create Company</h1>
        </header>
      </aside>
      <aside className="section card">
        <header>
          <h1>Add employee</h1>
        </header>
      </aside>
      <main className="companies-page section">
        <header>
          <h1>Companies</h1>
          <p>This section you can manage companies data</p>
        </header>
        <CompanyList />
      </main>
      <HomeButton />
    </Background>
  );
};

export default Companies;
