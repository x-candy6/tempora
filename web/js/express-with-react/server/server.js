const express = require("express");
const app = express();

app.get("/api", (req, res) => {
    res.json({ users: ["userOne", "userTwo"] });
});

app.listen(3879, () => {
    console.log("Server started on port 3879.");
});
