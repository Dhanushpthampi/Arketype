import { useEffect, useState } from "react";

function App() {
  const [status, setStatus] = useState("");

  useEffect(() => {
    fetch(`${import.meta.env.VITE_API_URL}/health/`)
      .then(res => res.json())
      .then(data => setStatus(data.status))
      .catch(err => setStatus("Error"));
  }, []);

  return (
    <div>
      <h1>Django API Status: {status}</h1>
    </div>
  );
}

export default App;
