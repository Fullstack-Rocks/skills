-- Fixture schema: every kind of relation and constraint the schema stage reads.
CREATE TABLE customers (
  id serial PRIMARY KEY,
  ref text NOT NULL UNIQUE,
  email text NOT NULL,
  created_at timestamptz DEFAULT now()
);

CREATE TABLE IF NOT EXISTS public."orders" (
  id bigserial PRIMARY KEY,
  customer_id integer REFERENCES customers (id),
  meta jsonb NOT NULL DEFAULT '{}',
  total_cents integer CHECK (total_cents >= 0),
  status text NOT NULL DEFAULT 'new',
  CONSTRAINT orders_status_check CHECK (status IN ('new', 'paid'))
);

CREATE TABLE order_items (
  order_id bigint NOT NULL,
  sku text NOT NULL,
  quantity integer NOT NULL DEFAULT 1,
  PRIMARY KEY (order_id, sku),
  FOREIGN KEY (order_id) REFERENCES orders (id)
);

CREATE TEMPORARY TABLE import_rows (line integer, payload jsonb);

CREATE VIEW paid_orders AS SELECT o.* FROM orders o WHERE o.status = 'paid';

CREATE MATERIALIZED VIEW customer_totals AS
  SELECT c.id, sum(o.total_cents) AS total
  FROM customers c
  JOIN orders o ON o.meta->>'customer_ref' = c.ref
  GROUP BY c.id;

CREATE INDEX orders_customer_idx ON orders (customer_id);
CREATE UNIQUE INDEX customers_email_idx ON customers USING btree (email);
