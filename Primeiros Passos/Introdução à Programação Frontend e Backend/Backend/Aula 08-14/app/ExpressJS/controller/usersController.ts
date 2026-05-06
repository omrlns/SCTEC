import type { Request, Response } from "express";
import type { IUsers } from "../model/users.js";
import usersModel from "../model/usersModel.js";
import { log } from "node:console";

function login(req: Request, res: Response, next: any) {
    res.render("login");
}

async function checkLogin(req: Request, res: Response, next: any) {
    const login = req.body as IUsers;
    try {

        let logado = await usersModel.findOne({
            where: {
                user: login.user,
                password: login.password
            }
        });

        if (logado != null) {
            res.redirect("/clients");
        }
        else {
            console.log("SENHA INVÁLIDA!!!")
        }

    } catch(erro) {
        console.log(erro);
        res.status(500).end();
    }

}

export default { login, checkLogin }