from logging.config import fileConfig
from sqlalchemy import engine_from_config
from sqlalchemy import pool
from alembic import context

import os
import sys

# Ajout du chemin du backend pour pouvoir importer app.*
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)
sys.path.append(os.path.join(BASE_DIR, "app"))

# Import de Base depuis ton projet FastAPI
from app.database import Base
from app import models  # IMPORTANT : importe tous tes modèles ici

# Configuration Alembic
config = context.config

# Lecture de la variable d'environnement DATABASE_URL
database_url = os.getenv("DATABASE_URL")

if database_url:
    config.set_main_option("sqlalchemy.url", database_url)

# Logging
fileConfig(config.config_file_name)

# Cible des migrations : les métadonnées SQLAlchemy
target_metadata = Base.metadata


def run_migrations_offline():
    """Mode offline : génère du SQL sans se connecter à la DB."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Mode online : applique les migrations directement dans la DB."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


# Choix du mode
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
