import express  from "express";
import clientesRouter from "./routes/cliente.js";

const app = express();

app.use(clientesRouter);

app.listen(3000, () => {
    console.log("SERVIDOR CRIADO!")
})