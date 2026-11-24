require('dotenv').config();

const express = require('express');
const fs = require('fs');
const path = require('path');
const { Pool } = require('pg');

const app = express();

const hostname = process.env.HOSTNAME;
const port = process.env.PORT;

app.use(express.json());

const pool = new Pool({
    user: "revision_system",
    host: "localhost",
    database: "revision_system",
    password: process.env.DB_PASSWORD,
    port: 5432
});

app.get('/', (req, res) => {
    res.sendFile(
        path.join(__dirname, '../public/views/index.html')
    );
});

app.get('/api/users', async (req, res) => {
    try {
        const result = await pool.query(
            "SELECT * FROM users;"
        );

        res.json(result.rows);

    } catch (error) {
        console.error("Database error:", error);

        res.status(500).json({
            error: "Failed to retrieve users"
        });
    }
});

app.use((req, res) => {
    res.status(404).json({
        error: "Route not found"
    });
});

app.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
