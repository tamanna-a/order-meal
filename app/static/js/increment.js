function incrementButton() {
    var element = document.getElementById('incrementText');
    var value = element.innerHTML;
    console.log(value)

    ++value;
    console.log(value)
    document.getElementById('incrementText').innerHTML = value;
}

//sned POST request via AJAX/javascript to python backend
function func() {
    var xml = new XMLHttpRequest();
    xml.open("POST", "{{url_for()}}", true) //true means asynchronous
    xml.setRequestHeader("Content-type","application/x-www-url-formencoded" ):

    xml.onload = function() {
        //parse if you are receiving dictionary from server
        var dataReply = JSON.parse(this.responseText) //python response
        alert(dataReply)
    };
    dataSend = JSON.stringify({'somedata': 'data',
                'moredata': 'moredata'});

    xml.send(dataSend) //sent to pyson backend
}