const http = require('http');

const hostname = '192.168.7.242';
const port = 3000;

const server = http.createServer((req, res) => {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/html');

    res.end('<h1>Hello World!</h1><p>My server is running!</p>');
});

server.listen(port, hostname, () => {
    console.log(`Server running at http://${hostname}:${port}/`)
})