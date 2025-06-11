# Utilisation d'une image Python légère
FROM python:3.11-slim

# Définir le dossier de travail
WORKDIR /app

# Copier le fichier de dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY ./app /app/app

# Commande par défaut pour le backend
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]