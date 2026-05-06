import type { Request, Response } from "express";
import type { IUsers } from "../model/users.js";
import usersModel from "../model/usersModel.js";

async function login(req: Request, res: Response, next: any) {
    res.render("login");
}

export default {login};