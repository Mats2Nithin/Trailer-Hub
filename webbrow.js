// Javascript to take input from the form and handle the submit button's click event by searching the trailer of the entered movie.

var button = document.getElementById('click');
button.addEventListener('click',function(){
var input = document.getElementById('movies').value;
window.open("https://www.google.co.in/?gfe_rd=cr&ei=s6fuV6SbC-qHuwTiiLKgBQ&gws_rd=ssl#q="+input+" movie trailer", '_self');});