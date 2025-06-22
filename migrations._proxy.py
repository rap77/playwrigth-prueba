import os
# Ejemplo de lógica para elegir la configuración
def run_migrations_for_engine(db_type):
    if db_type == "sqlite":
        os.system("alembic -c alembic_sqlite/alembic.ini upgrade head")
    elif db_type == "postgres":
        os.system("alembic -c alembic_postgres/alembic.ini upgrade head")