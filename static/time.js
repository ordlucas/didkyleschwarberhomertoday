function getTime() {
    var offset = new Date().getTimezoneOffset();
    document.cookie = "tzOffset = " + offset;
}