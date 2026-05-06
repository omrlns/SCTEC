import { Router } from "express";
import clientsController from "../controller/clientsController.js";

const router = Router();

router.get("/", clientsController.index);

router.get("/create", clientsController.create);
router.post("/create", clientsController.store);

router.get("/:id", clientsController.show);

router.get("/edit/:id", clientsController.edit);
router.post("/edit/:id", clientsController.update);

router.get("/del/:id", clientsController.del);

export default router;