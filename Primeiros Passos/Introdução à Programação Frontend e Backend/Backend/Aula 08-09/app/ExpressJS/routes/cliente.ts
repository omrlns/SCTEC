import { Router } from "express";

const router = Router();

router.get("/", (req, res) => {
    res.send("Olá mundo!");
})

router.get("/sobre", (req, res) => {
    res.send("Rota falando sobre nós");
})

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