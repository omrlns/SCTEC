import type { Request, Response } from "express";
import type { IClients } from "../model/clients.js";
import clientsModels from "../model/clientsModels.js";
import { error } from "node:console";

async function index(req: Request, res: Response, next: any) {
    // res.render("index");
    const clients = await clientsModels.findAll();
    res.json(clients);
}

function create(req: Request, res: Response, next: any) {
    res.render("create");
}

async function store(req: Request, res: Response, next: any) {
    try {
        const { name, email } = req.body; // se o formulário enviar "name"

        await clientsModels.create({ nome: name, email: email });
        res.redirect("/");
    } catch (error: any) {
        console.log("ERRO DETALHADO: ", error.message)
        console.log("ERRO DE VALIDAÇÃO: ", error.errors?.map((e: any) => e.message));
        res.status(500).send("ERRO AO SALVAR!");
    }
}

export default { index, create, store };