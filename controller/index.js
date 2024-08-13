//const express = require('express');
const express = require('express');
const app = express();
const port = 3000;
const fantasy = require('./services/fantasy');
const cors = require('cors');

app.use(cors());

app.get('/', async (req, res) => {
    let data = await fantasy.getMultiple(req.query.page);
    res.send(data);
});

/* Error handler middleware */
app.use((err, req, res, next) => {
    const statusCode = err.statusCode || 500;
    console.error(err.message, err.stack);
    res.status(statusCode).json({ message: err.message });
    return;
  });

app.listen(port, () => {
    console.log(`Example app listening at http://localhost:${port}`);
})