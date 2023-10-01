import { GoOrganization } from "react-icons/go";
import { BsPersonLinesFill } from "react-icons/bs";
import { BiTrash } from "react-icons/bi";
import axios, { AxiosError } from "axios";
import { CompanyData } from "../pages/Companies";
import useSWR from "swr";
import { useNavigate } from "react-router-dom";

export interface FullCompanyData {
  companyID: number;
  description: string;
  email: string;
  name: string;
  employees: {
    employeeID: number;
    name: string;
    email: string;
    age: number;
    job: string;
  }[];
}

const CompanyRow = ({
  companyID,
  name,
  email,
}: Omit<CompanyData, "description">) => {
  const navigate = useNavigate();

  const fetcher = (url: string) =>
    axios.get(url).then((res) => {
      return res.data;
    });

  const { data } = useSWR<FullCompanyData[], AxiosError>(
    `http://127.0.0.1:8000/company/${companyID}/employees`,
    fetcher,
    {
      refreshInterval: 1000,
      revalidateOnFocus: true,
      refreshWhenOffline: true,
      refreshWhenHidden: false,
      revalidateOnMount: true,
      onError(error) {
        console.log(`%c ${error}`, "color: red");
      },
    }
  );

  const handleDelete = async () => {
    try {
      await axios.delete(`http://127.0.0.1:8000/company/${companyID}`);
    } catch (error) {
      console.error(error);
    }
  };

  const handleClick = () => {
    navigate(`/companies/${companyID}`);
  };

  return (
    <article
      className="company-row"
      id={`${companyID}-company`}
      onClick={handleClick}
    >
      <div className="company-row-logo">
        <GoOrganization />
      </div>
      <span className="company-row-name">{name} </span>
      <div className="company-row-email">
        <span>{email}</span>
      </div>
      <div
        style={{
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <button
          type="button"
          style={{
            color: "red",
            background: "none",
            border: "none",
            fontSize: "1.5rem",
            verticalAlign: "middle",
            display: "flex",
            alignItems: "center",
            cursor: "pointer",
          }}
          onClick={handleDelete}
        >
          <BiTrash />
        </button>
      </div>
      <div className="number-of-employees">
        <BsPersonLinesFill />
        <span>{data ? data[0].employees.length : 0}</span>
      </div>
    </article>
  );
};

export default CompanyRow;
