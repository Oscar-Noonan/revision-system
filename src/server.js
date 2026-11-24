// import secrets from .env file
require('dotenv').config();

// import node modules
const cookieParser = require('cookie-parser');
const express = require('express');
const fs = require('fs');
const path = require('path');
const { Pool } = require('pg');

const app = express();
const authRoutes = require('./routes/auth');

// configure environment variables
const hostname = process.env.HOSTNAME;
const port = process.env.PORT;

// configures middleware
app.use(cookieParser());
app.use(express.json());
app.use(express.static('public'));

// configures routes
app.use('/api/auth', authRoutes);

// creates authenticated database connection
const pool = new Pool({
    user: "revision_system",
    host: "localhost",
    database: "revision_system",
    password: process.env.DB_PASSWORD,
    port: 5432
});

// send root get requests to index.html
app.get('/', (req, res) => {
    res.sendFile(
        path.join(__dirname, '../public/views/index.html')
    );
});

// return a list of all users emails
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

// configures response if requested route does not exist
app.use((req, res) => {
    res.status(404).json({
        error: "Route not found"
    });
});

// starts a server using express
app.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`);
});
