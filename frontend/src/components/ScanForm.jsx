import React, { useState } from "react";

function ScanForm() {
  const [target, setTarget] = useState("");
  const [results, setResults] = useState(null);

  const runScan = async () => {
    try {
      const res = await fetch(`http://127.0.0.1:8000/nmap/${target}`);
      const data = await res.json();
      setResults(data);
    } catch (err) {
      console.error("Scan failed:", err);
    }
  };

  return (
    <div>
      <input
        type="text"
        value={target}
        onChange={(e) => setTarget(e.target.value)}
        placeholder="Enter target (e.g. 10.10.0.1)"
      />
      <button onClick={runScan}>Run Nmap Scan</button>

      {results && (
        <div>
          <h3>Scan Results for {results.target}</h3>
          <p>Status: {results.status}</p>
          <p>Timestamp: {results.timestamp}</p>

          {/* If we have raw_output, show it in a pre block */}
          {results.scan.raw_output && (
            <pre style={{ whiteSpace: "pre-wrap" }}>
              {results.scan.raw_output}
            </pre>
          )}

          {/* If we have parsed JSON (future upgrade with -oJ), render ports */}
          {results.scan.hosts && (
            <table border="1" cellPadding="5">
              <thead>
                <tr>
                  <th>Port</th>
                  <th>State</th>
                  <th>Service</th>
                  <th>Version</th>
                </tr>
              </thead>
              <tbody>
                {results.scan.hosts[0].ports.map((port, idx) => (
                  <tr key={idx}>
                    <td>{port.portid}/{port.protocol}</td>
                    <td>{port.state}</td>
                    <td>{port.service.name}</td>
                    <td>{port.service.version || "-"}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>
      )}
    </div>
  );
}

export default ScanForm;
