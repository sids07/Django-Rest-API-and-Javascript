console.log("Wow");

let url = 'http://127.0.0.1:8000/rest/blood/info/'

async function donate(url) {
    let authentication = localStorage.getItem('Authentication')
    let myToken = "Token"+" "+authentication
    const result = await fetch(url, {
        method: 'GET',
        headers: {
            'Authorization': myToken,
        }
    });

    if (!result.ok) {
        return false;
    }

    const data = await result.json()
    console.log(data)
    const template = document.querySelector('#doner_card')
    const cont = document.querySelector('#myContainer');

    for (let don of data){
    const temElement = template.content.cloneNode(true);
    temElement.querySelector('.doner-image').setAttribute('src',don['image'])
    temElement.querySelector('.doner-name').innerHTML="Name: "+don['name']
    temElement.querySelector('.doner-blood').innerHTML="Blood Group: "+don['blood_group']
    temElement.querySelector('.doner-age').innerHTML="Age: "+don['age']
    temElement.querySelector('.doner-sex').innerHTML="Gender: "+don['gender']
    temElement.querySelector('.doner-ph').innerHTML="Phone: "+don['phone']
    temElement.querySelector('.doner-address').innerHTML="Address: "+ don['address']
        let dis=''
        don['disease'].forEach(function (element){
            dis = dis + element['dis_name']+ ','+' '
        })
        temElement.querySelector('.doner-disease').innerHTML="Disease: "+ dis

    cont.appendChild(temElement);
    }
    return data;
}

if (isAuthenticated()){
    let val = donate(url)
    }
if (!isAuthenticated()){
    window.location.href = '/login';
}

console.log(document.querySelector('#search').innerHTML)
final_logout();