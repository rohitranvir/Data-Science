    -- Create the tables
    CREATE TABLE CUSTOMER (
        cid INT IDENTITY(1,1) PRIMARY KEY,
        cname VARCHAR(100) NOT NULL,
        addr VARCHAR(200)
    );

    CREATE TABLE PRODUCTS (
        prodid INT IDENTITY(1,1) PRIMARY KEY,
        pname VARCHAR(100) NOT NULL,
        price DECIMAL(10, 2)
    );

    CREATE TABLE ORDERS (
        ordid INT IDENTITY(1,1) PRIMARY KEY,
        orddt DATE NOT NULL,
        deldt DATE,
        cid INT,
        cname VARCHAR(100),
        addr VARCHAR(200),
        FOREIGN KEY (cid) REFERENCES CUSTOMER(cid)
    );

    CREATE TABLE ORDER_DETAILS (
        ordid INT,
        prodid INT,
        qty INT NOT NULL,
        PRIMARY KEY (ordid, prodid),
        FOREIGN KEY (ordid) REFERENCES ORDERS(ordid),
        FOREIGN KEY (prodid) REFERENCES PRODUCTS(prodid)
    );

    -- Insert 100 records into CUSTOMER
    WITH numbers AS (
        SELECT TOP 100 ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) as n
        FROM sys.objects a
        CROSS JOIN sys.objects b
    )
    INSERT INTO CUSTOMER (cname, addr)
    SELECT 
        CASE ABS(CHECKSUM(NEWID())) % 10
            WHEN 0 THEN 'John'
            WHEN 1 THEN 'Jane'
            WHEN 2 THEN 'Michael'
            WHEN 3 THEN 'Sarah'
            WHEN 4 THEN 'David'
            WHEN 5 THEN 'Emma'
            WHEN 6 THEN 'James'
            WHEN 7 THEN 'Lisa'
            WHEN 8 THEN 'Robert'
            ELSE 'Maria'
        END + ' ' +
        CASE ABS(CHECKSUM(NEWID())) % 10
            WHEN 0 THEN 'Smith'
            WHEN 1 THEN 'Johnson'
            WHEN 2 THEN 'Williams'
            WHEN 3 THEN 'Brown'
            WHEN 4 THEN 'Jones'
            WHEN 5 THEN 'Garcia'
            WHEN 6 THEN 'Miller'
            WHEN 7 THEN 'Davis'
            WHEN 8 THEN 'Rodriguez'
            ELSE 'Martinez'
        END as cname,
        CAST(ABS(CHECKSUM(NEWID())) % 9999 + 100 AS VARCHAR) + ' ' +
        CASE ABS(CHECKSUM(NEWID())) % 5
            WHEN 0 THEN 'Main St'
            WHEN 1 THEN 'Oak Ave'
            WHEN 2 THEN 'Maple Rd'
            WHEN 3 THEN 'Washington Blvd'
            ELSE 'Park Ln'
        END + ', ' +
        CASE ABS(CHECKSUM(NEWID())) % 5
            WHEN 0 THEN 'New York'
            WHEN 1 THEN 'Los Angeles'
            WHEN 2 THEN 'Chicago'
            WHEN 3 THEN 'Houston'
            ELSE 'Phoenix'
        END + ', ' +
        CASE ABS(CHECKSUM(NEWID())) % 5
            WHEN 0 THEN 'NY'
            WHEN 1 THEN 'CA'
            WHEN 2 THEN 'IL'
            WHEN 3 THEN 'TX'
            ELSE 'AZ'
        END + ' ' +
        CAST(ABS(CHECKSUM(NEWID())) % 90000 + 10000 AS VARCHAR) as addr
    FROM numbers;

    -- Insert 100 records into PRODUCTS
    WITH numbers AS (
        SELECT TOP 100 ROW_NUMBER() OVER (ORDER BY (SELECT NULL)) as n
        FROM sys.objects a
        CROSS JOIN sys.objects b
    )
    INSERT INTO PRODUCTS (pname, price)
    SELECT 
        CASE ABS(CHECKSUM(NEWID())) % 10
            WHEN 0 THEN 'Laptop'
            WHEN 1 THEN 'Smartphone'
            WHEN 2 THEN 'Tablet'
            WHEN 3 THEN 'Headphones'
            WHEN 4 THEN 'Keyboard'
            WHEN 5 THEN 'Mouse'
            WHEN 6 THEN 'Monitor'
            WHEN 7 THEN 'Printer'
            WHEN 8 THEN 'Camera'
            ELSE 'Speaker'
        END + ' ' +
        CHAR(65 + ABS(CHECKSUM(NEWID())) % 26) +
        CHAR(65 + ABS(CHECKSUM(NEWID())) % 26) + ' ' +
        CAST(ABS(CHECKSUM(NEWID())) % 9 + 1 AS VARCHAR) + '000' as pname,
        ROUND(10 + RAND(CHECKSUM(NEWID())) * 1990, 2) as price
    FROM numbers;

    -- Insert 100 records into ORDERS
    INSERT INTO ORDERS (orddt, deldt, cid, cname, addr)
    SELECT TOP 100
        DATEADD(day, -ABS(CHECKSUM(NEWID())) % 365, GETDATE()) as orddt,
        DATEADD(day, ABS(CHECKSUM(NEWID())) % 14 + 1, 
                DATEADD(day, -ABS(CHECKSUM(NEWID())) % 365, GETDATE())) as deldt,
        cid,
        cname,
        addr
    FROM CUSTOMER
    ORDER BY NEWID();

    -- Insert 100 records into ORDER_DETAILS
    INSERT INTO ORDER_DETAILS (ordid, prodid, qty)
    SELECT TOP 100
        o.ordid,
        p.prodid,
        ABS(CHECKSUM(NEWID())) % 5 + 1 as qty
    FROM ORDERS o
    CROSS JOIN PRODUCTS p
    WHERE ABS(CHECKSUM(NEWID())) % 100 < 30
    ORDER BY NEWID();

