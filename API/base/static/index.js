console.log("This is JS");

async function auth(url, username, password) {
    const result = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'username': username,
            'password': password
        })
    });

    if (!result.ok) {
        return false;
    }

    const data = await result.json()

    localStorage.setItem('Authentication', data['token']);

    localStorage.setItem('UserId', data['user_id']);

    return true;
}

function isAuthenticated() {
    return !!localStorage.getItem('Authentication');
}

function logout() {
    localStorage.removeItem('Authentication')
    localStorage.removeItem('UserId')
}

function fetchProtected() {
    const headers = {};
    console.log("AAAA")
    if (isAuthenticated()) {
        const token = localStorage.getItem('Authentication');
        headers['Authorization'] = `Token ${token}`
        console.log(headers['Authorization'])
    }

    const result = fetch('http://localhost:5000/rest/blood/info/', {
        headers: headers,
    });

    return result.then((res) => {
        if (res.ok) {
            return res.json();
            console.log(res)
        }


        if (res.status === 401) {
            logout();
        }

        return res.text();
    });


}function navChange(){
 if (isAuthenticated()){
       let element = document.createElement('a');
       let text = document.createTextNode('Profile');

       let my = document.getElementsByClassName('nav-link')[2];
       element.appendChild(text)
       element.className='nav-link';
       element.setAttribute('href','/profile');
       element.innerText='Profile'
       my.replaceWith(element)

       let element_1 = document.createElement('button');
       let text_1 = document.createTextNode('Logout');

       let my_1 = document.getElementsByClassName('nav-link')[3];
       element_1.appendChild(text_1)
       element_1.id='but'
       element_1.className='nav-link';
//       element_1.setAttribute('type','button');
       element_1.innerText='Logout'
       my_1.replaceWith(element_1)
//       window.location.href='/';
 }
 }
 navChange();

function final_logout(){
let btn = document.querySelector('#but')
console.log(btn)
btn.addEventListener('click',_logout);
}
 function _logout(e) {
            console.log("Hel")
            logout()
            window.location.href = '/login';
            alert('loggedout');
        }


final_logout()

