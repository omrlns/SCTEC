import type { Request, Response } from "express";
import type { IClients } from "../model/clients.js";
import clientsModel from "../model/clientsModel.js";

async function index(req: Request, res: Response, next: any) {
    // res.render("index");
    const clients = await clientsModel.findAll();
    res.json(clients);
}

async function create(req: Request, res: Response, next: any) {
    res.render("create");
}

async function store(req: Request, res: Response, next: any) {
    try {
        const { name, email } = req.body; // se o formulário enviar "name"

        await clientsModel.create({ nome: name, email: email });
        res.redirect("/");
    } catch (error: any) {
        console.log("ERRO DETALHADO: ", error.message)
        console.log("ERRO DE VALIDAÇÃO: ", error.errors?.map((e: any) => e.message));
        res.status(500).send("ERRO AO SALVAR!");
    }
}

async function show(req: Request, res: Response, next: any) {
    try {
        // buscamos o cliente pelo id
        const client = await clientsModel.findByPk(req.params.id as string);

        // verificamos se o cliente realmente existe no banco
        if (!client) {
            // Se for null, retornamos 404 (Not Found)
            return res.status(404).json({ error: "CLIENTE NÃO ENCONTRADO!" });
        }

        // se existir, enviamos o JSON
        res.json(client);

    } catch (error: any) {
        // tratamento de erro caso o banco falhe
        console.error("ERRO AO BUSCAR O CLIENTE: ", error.message);
        res.status(500).json({ error: "ERRRO INTERNO DO SERVIDOR!." });
    }
}

async function edit(req: Request, res: Response, next: any) {
    const client = await clientsModel.findByPk(req.params.id as string);
    res.render("edit", { client: client });
}

async function update(req: Request, res: Response, next: any) {
    await clientsModel.update(
        req.body as IClients, {
        where: {
            id: req.params.id
        }
    }
    );

    res.redirect("/");

}

async function del(req: Request, res: Response, next: any) {
    await clientsModel.destroy({
        where: {
            id: req.params.id
        }
    }
    );

    res.redirect("/");

}

export default { index, create, store, show, edit, update, del };