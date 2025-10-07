import express from 'express';

const app = express();
const PORT = 3000;

const DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1425152322891419679/d9ktFQQWzJfV6g2ADDw_OMUeHJYudj3Ev8Cs7hfl8X1gwiFVd_etiX9-cmuBDAMY0PSl'

app.use(express.json())

app.post('/notify', (req, res) => {
    const {message} = req.body;

    if(!message){
        return res.status(400).json({error: 'message is required'});
    }

    fetch(DISCORD_WEBHOOK_URL, {
        method: 'POST',
        headers: {'Content-type': 'application/json'},
        body: JSON.stringify({content:message})
    })
    .then(response => {
        if(!response.ok){
            throw new Error(`Discord responded with status ${response.status}`)
        }
        res.json({status: 'Message sent...'})
    })
    .catch(error => {
        console.error('error sending to discord', error)
        res.status(500).json({error: 'failed sending your message'});
    })
})

app.listen(PORT, () =>{
    console.log(`Server running at localhost: ${PORT}`);
})