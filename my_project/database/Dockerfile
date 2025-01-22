FROM postgres:13

# Set environment variables for PostgreSQL
ENV POSTGRES_USER=postgre
ENV POSTGRES_PASSWORD=123456789
ENV POSTGRES_DB=postgres

# Optional: copy any SQL scripts for database initialization
COPY init.sql /docker-entrypoint-initdb.d/
