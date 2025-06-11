# FastAPI + Celery + Redis + Docker + Flower + Frontend (Vite + Vue.js + Nginx)

## 1. Présentation

Architecture clé en main pour exécuter des scripts Python de manière asynchrone via une API web, avec une interface utilisateur moderne et rapide.

- **Backend** : FastAPI (API REST)
- **Frontend** : Vue.js + TailwindCSS (servi par Nginx, build via Vite)
- **Tâches asynchrones** : Celery
- **Broker** : Redis
- **Monitoring** : Flower + Logs
- **Containerisation** : Docker & Docker Compose
- **Validation des données** : Pydantic
- **Tests Backend** : Pytest

---

## 2. Schéma Fonctionnel

```
[ Frontend (Vue.js + Nginx) ]
            |
      (HTTP Request)
            |
      +------------+           +------------+           +-----------------+
      |  FastAPI   | --push--> |   Redis    | <--pull-- |  Celery Worker  |
      |  Backend   |           |  (Broker)  |           |   (Executor)    |
      +------------+           +------------+           +-----------------+
                                        |
                                        v
                               +-----------------+
                               |     Flower      |
                               |  (Monitoring)   |
                               +-----------------+
```

---

## 3. Prérequis Serveur / VM

- **Docker** : `sudo apt install docker.io`
- **Docker Compose** : `sudo apt install docker-compose`
- **Git** : `sudo apt install git`
- **Node.js & npm** *(pour dev frontend uniquement)* : [Node.js](https://nodejs.org/) v20.19.1

---

## 4. Déploiement (Production)

```bash
git clone <repo>
cd <repo>
docker-compose up --build -d
```

- Accès :

  - **Frontend** : `http://<IP_VM>:3000`
  - **API Backend** : `http://<IP_VM>:8000`
  - **Flower** : `http://<IP_VM>:5555`

---

## 5. Workflow de Développement Frontend

### 🎨 Étapes pour développer le frontend en local :

1. **Installation des dépendances** :

   ```bash
   cd frontend
   npm install
   ```

2. **Lancer le serveur de développement Vite** :

   ```bash
   npm run dev
   ```

   ➔ Accès via `http://localhost:5173`

3. **Build manuel (optionnel en local)** :

   ```bash
   npm run build
   ```

   *(En production, ce build est géré automatiquement par Docker)*

---

## 6. Observabilité & Monitoring

- **Flower** : Monitoring des tâches Celery (`http://<IP>:5555`).
- **Logs Backend** : `backend/logs/script.log`
- **Endpoints API** :
  - `GET /health`
  - `POST /launch-task`

---

## 7. Debugging

- **Tester l'API** :
  ```bash
  curl -X POST http://localhost:8000/launch-task -H "Content-Type: application/json" -d '{}'
  ```
- **Logs Backend** :
  ```bash
  docker logs -f fastapi_backend
  ```
- **Logs Worker** :
  ```bash
  docker logs -f celery_worker
  ```
- **Logs Frontend (Nginx)** :
  ```bash
  docker logs -f nginx_frontend
  ```

---

## 8. Architecture des Fichiers

### Arborescence Globale

```
mon-projet/
├── backend/
│   ├── app/
│   ├── tests/
│   ├── logs/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── package.json
│   └── vite.config.js
│
├── docker-compose.yml
├── .env
└── README.md
```

---

## 9. Tests avec Pytest

### Lancer les tests backend en local :

```bash
cd backend
pytest /tests
```

---

## 10. Commandes Utiles

| Action                | Commande                                                 |
| --------------------- | -------------------------------------------------------- |
| Lancer l'app (prod)   | `docker-compose up --build -d`                           |
| Arrêter l'app         | `docker-compose down`                                    |
| Logs backend          | `docker logs -f fastapi_backend`                         |
| Logs worker           | `docker logs -f celery_worker`                           |
| Logs frontend (nginx) | `docker logs -f nginx_frontend`                          |
| Logs applicatifs      | `tail -f backend/logs/script.log`                        |
| Tester l'API          | `curl -X POST http://localhost:8000/launch-task -d '{}'` |
| Lancer les tests      | `pytest /tests`                                          |

---