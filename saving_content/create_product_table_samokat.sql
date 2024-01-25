-- Необходимо предварительно создать базу данных, если она не существует

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS products (
    id UUID PRIMARY KEY,
    name TEXT,
    price INTEGER,
    has_discount BOOLEAN,
    old_price INTEGER,
    discount_percent INTEGER,
    quantity INTEGER,
    is_available BOOLEAN,
    highlights TEXT,
    preview_image TEXT,
    has_variants BOOLEAN
);