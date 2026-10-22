import React, { useEffect, useState } from "react";

function BeEFHook() {
  const [clients, setClients] = useState([]);

  useEffect(() => {
    const fetchClients = async () => {
      try {
        // Call your FastAPI proxy route instead of BeEF directly
        const res = await fetch("http://127.0.0.1:8000/beef/clients");
        const data = await res.json();
        setClients(data.hooked_browsers || []);
      } catch (err) {
        console.error("Failed to fetch BeEF clients:", err);
      }
    };

    fetchClients();
    const interval = setInterval(fetchClients, 5000); // poll every 5s
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <h3>BeEF Hook Integration</h3>
      <p>Hook URL: <code>http://127.0.0.1:3000/hook.js</code></p>

      {clients.length === 0 ? (
        <p>No hooked clients yet.</p>
      ) : (
        <table border="1" cellPadding="5">
          <thead>
            <tr>
              <th>ID</th>
              <th>IP</th>
              <th>Browser</th>
              <th>OS</th>
              <th>Last Seen</th>
            </tr>
          </thead>
          <tbody>
            {clients.map((client) => (
              <tr key={client.id}>
                <td>{client.id}</td>
                <td>{client.ip}</td>
                <td>{client.browser?.name} {client.browser?.version}</td>
                <td>{client.os?.name}</td>
                <td>{client.lastseen}</td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </div>
  );
}

export default BeEFHook;
