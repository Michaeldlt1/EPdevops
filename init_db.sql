CREATE TABLE IF NOT EXISTS productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    precio NUMERIC(10,2) NOT NULL,
    stock INTEGER NOT NULL
);

INSERT INTO productos (nombre, precio, stock)
VALUES
('Laptop Lenovo', 850.00, 10),
('Mouse Logitech', 25.50, 50),
('Teclado Mecánico', 70.00, 20),
('Monitor Samsung', 230.00, 15),
('Disco SSD 1TB', 95.00, 30);