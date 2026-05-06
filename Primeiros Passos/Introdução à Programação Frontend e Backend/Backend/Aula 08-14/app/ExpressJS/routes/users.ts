import { Router } from "express";
import usersController from "../controller/usersController.js";

const router = Router();

router.get("/", usersController.login);

export default router;