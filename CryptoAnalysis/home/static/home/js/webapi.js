let ws = new WebSocket("wss://stream.binance.com:9443/ws/btcusdt@ticker");


ws.onerror =(e)=>{
     
}

ws.onmessage = (event=>{
    console.log(event.data);
    document.getElementById("btcprice").innerText = (JSON.parse(event.data).E).toFixed(3);
    document.getElementsByClassName("eth")[0].innerText = (JSON.parse(event.data).a);

})


