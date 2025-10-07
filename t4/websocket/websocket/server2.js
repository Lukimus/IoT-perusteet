const WebSocket = require('ws')

const server = new WebSocket.Server({port:8080})

server.on('connection', socket => {
    console.log('client connected');

    socket.on('message', message => {
        console.log('received', message.toString());
        socket.send(`Echo: ${message}`);
    })
    socket.on('close', () => {
        console.log('client disconnected')
    })
})