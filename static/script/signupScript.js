
document.getElementById("confirm password").addEventListener("input", testPass);
function testPass(){
    var password = document.getElementById("password").value;
    var confirmPass = document.getElementById("confirm password").value;
    var mismatch = document.getElementById("mismatch-msg");
    if(password != confirmPass){
        mismatch.innerHTML = "Password didn't match";
    }else{
        mismatch.innerHTML = "";
    }
}