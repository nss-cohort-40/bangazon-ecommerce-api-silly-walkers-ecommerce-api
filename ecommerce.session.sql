DELETE FROM ecommerceapi_orderproduct
WHERE id = 19;

-- Populating ProductType Table
-- Luke

INSERT INTO ecommerceapi_producttype
    (name)
VALUES
    ("Animals"),
    ("Autos"),
    ("Missed-Connections"),
    ("Electronics"),
    ("Magic Props");