alembic -c alembic_sqlite/alembic.ini revision --autogenerate -m "Init SQLite"
alembic -c alembic_sqlite/alembic.ini upgrade head


alembic -c alembic_postgres/alembic.ini revision --autogenerate -m "Init PostgreSQL"
alembic -c alembic_postgres/alembic.ini upgrade head