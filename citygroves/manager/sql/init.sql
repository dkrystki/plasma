CREATE USER manager WITH PASSWORD 'password';
CREATE DATABASE manager;
GRANT ALL PRIVILEGES ON DATABASE manager TO manager;
ALTER DATABASE manager OWNER TO manager;
