import express  from "express";
import clientesRouter from "./routes/clients.js";

const app = express();

app.use(clientesRouter);
app.set("view engine", "pug");
app.set("views", "./views");

app.listen(3000, () => {
    console.log("SERVIDOR CRIADO!")
})