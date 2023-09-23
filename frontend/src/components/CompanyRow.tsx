import { GoOrganization } from "react-icons/go";
import { BsPersonLinesFill } from "react-icons/bs";

const CompanyRow = () => {
  return (
    <article className="section company-row">
      <div className="company-row-logo">
        <GoOrganization />
      </div>
      <span className="company-row-name">Lorem ipsum dolor sit </span>
      <div className="company-row-email">
        <span>email@email.xy</span>
      </div>
      <div className="number-of-employees">
        <BsPersonLinesFill />
        <span>10</span>
      </div>
    </article>
  );
};

export default CompanyRow;
