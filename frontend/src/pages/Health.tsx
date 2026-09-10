import { useEffect, useState } from "react";
import { getHealth } from "@services/api";

export default function Health() {
  const [data, setData] = useState<any>(null);

  useEffect(() => {
    getHealth().then(setData);
  }, []);

  return (
    <div>
      <h1>Health Check</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
