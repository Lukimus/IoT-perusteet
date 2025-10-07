const { response } = require("express")

const url = "https://api.thingspeak.com/channels/3103787/feeds.json?api_key=HX9W2A6JWZL439KQ"

fetch(url)
.then(response => response.json())
.then(data => {
    const feeds = data.feeds;

    const temperatures = feeds.map(feed =>({
        time: feed.created_at,
        temp: parseFloat(feed.field1)
    }));
    document.getElementById("output").textContent = JSON.stringify(temperatures);
})
.catch(error => {
    console.error("error fetching data", error);
    document.getElementById("output").textContent = "error loading data";
})