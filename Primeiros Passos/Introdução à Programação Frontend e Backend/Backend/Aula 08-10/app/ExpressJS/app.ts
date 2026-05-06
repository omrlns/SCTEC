import express  from "express";
import clientesRouter from "./routes/clients.js";
import db from "./db.js"

const app = express();

app.use(clientesRouter);
app.set("view engine", "pug");
app.set("views", "./views");

db.sync().then(() => {
    console.log("CONECTADO COM O BANCO: " + process.env.DB_NAME);
});

app.listen(process.env.PORT, () => {
    console.log("SERVIDOR CRIADO!")
})