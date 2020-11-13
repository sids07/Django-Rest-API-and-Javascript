console.log("Wow search");
let url_back = window.location.href.split("/").pop().split("?").pop();

console.log(url_back);
let url = 'http://127.0.0.1:8000/rest/blood/info/blood/list?'

async function search(url) {
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
    console.log(don['image'])
    const temElement = template.content.cloneNode(true);
    temElement.querySelector('.doner-image').setAttribute('src',don['image'])
    temElement.querySelector('.doner-name').innerHTML="Name: "+don['name']
    temElement.querySelector('.doner-blood').innerHTML="Blood Group: "+don['blood_group']
    temElement.querySelector('.doner-age').innerHTML="Age: "+don['age']
    temElement.querySelector('.doner-sex').innerHTML="Gender: "+don['gender']
    temElement.querySelector('.doner-ph').innerHTML="Phone: "+don['phone']
    temElement.querySelector('.doner-address').innerHTML="Address: "+ don['address']
    console.log(temElement.querySelector('.doner-address'))
    cont.appendChild(temElement);
    }
    return data;
}

console.log(url+url_back)
const searched = search(url+url_back)

final_logout();