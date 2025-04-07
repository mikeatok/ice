

    const name = document.getElementById('username');
const password = document.getElementById('Password')
const form = document.getElementById('form')
from.addEventListener('click', e =>{e.preventDefault();
document.getElementById("loginButton").addEventListener("click", validateInputs)
    validateInputs();


});
const setError =(element, message) => {
    const inputcontrol = element.parentElement;
    const errorDisplay = inputcontrol.queryselector('.errror');
    errorDisplay.innerText = message;
    inputcontrol.classlist.add('error');
    inputcontrol.classlist.remove('success')
}
const setsuccess = element =>{
    const inputcontrol = element.parentElement;
    const errordisplay = inputcontrol.queryselector('.error')
    errorDisplay.innertext = '';
    inputcontrol.classlist.add('success');
    inputcontrol.classlist.remove('error');
};

const validateInputs = () => {
    const usernameValue = username.value.trim();
    const passwordValue = password.value.trim();

    if(usernameValue === ''){ setError(username,'username is required');}
    else{setsuccess(username);

    }
    if (passwordValue === ''){
        setError(password,'password is required');}
        else if (passwordValue.length<8){seterror(password,'passowrd must be at least 8 character long')}
        else{setsuccess(password);}


        for(const credential of validateInputs){
    if (credential.username === username.value && credential.passowrd === password.value)
    {window.location.href = 'home.html'}
    else{
        alert('invalid username and password')
    }

        }
    }

