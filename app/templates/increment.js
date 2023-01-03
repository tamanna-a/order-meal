function incrementButton() {
    var element = document.getElementById('incrementText');
    var value = element.innerHTML;
    console.log(value)

    ++value;
    console.log(value)
    document.getElementById('incrementText').innerHTML = value;
}