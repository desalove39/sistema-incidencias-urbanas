-- Creación de la base de datos para el Sistema de Incidencias Urbanas
CREATE DATABASE IF NOT EXISTS reportes_urbanos_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Creación del usuario de aplicación
CREATE USER IF NOT EXISTS 'Usuario'@'%' IDENTIFIED BY 'mi_contraseña';

-- Otorgar privilegios sobre la base de datos
GRANT ALL PRIVILEGES ON reportes_urbanos_db.* TO 'Usuario'@'%';

-- Aplicar cambios de privilegios
FLUSH PRIVILEGES;