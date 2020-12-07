function changecolor()
{
    let nowurl = window.location.href;
    if(nowurl.match(/index.html/)){
        let link =$("#deslink");
        link.css("background","#4169E1");
        link.css("color","black");
    }else if(nowurl.match(/rsa.html/)){
        let link =$("#rsalink");
        link.css("background","#4169E1");
        link.css("color","black");
    }
}

changecolor();
