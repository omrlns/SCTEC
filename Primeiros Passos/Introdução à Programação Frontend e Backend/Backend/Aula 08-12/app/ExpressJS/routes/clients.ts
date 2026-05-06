import { Router } from "express";
import clientsController from "../controller/clientsController.js";

const router = Router();

router.get("/", clientsController.index);

router.get("/create", clientsController.create);
router.post("/create", clientsController.store);

router.get("/carreira", (req, res) => {
    res.send("Trabalhe conosco");
})

router.get("/carreira", (req, res) => {
    res.send("Trabalhe conosco");
})
router.get("/contato", (req, res) => {
    res.send("Contato");
})

export default router;