console.log("Davit")


function GetAscii() {
    var letters = '';
    for (var i = 97; i <= 122; i++) { // ASCII codes for lowercase letters (97 to 122)
        letters += String.fromCharCode(i);
    }
    for (var i = 65; i <= 90; i++) { // ASCII codes for uppercase letters (65 to 90)
        letters += String.fromCharCode(i);
    }

    return letters
}


console.log(GetAscii())
