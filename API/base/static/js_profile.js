console.log("Hello profile");

async function profile(url) {
    let authentication = localStorage.getItem('Authentication')
    let myToken = "Token"+" "+authentication
    const result = await fetch(url, {
        method: 'GET',
        headers: {
            'Authorization': myToken,
        }
    });
    console.log(result.status)
    if (result.status==404){
    window.location.href=('/create_form')

    }
    if (!result.ok) {
        return false;
    }
    const data = await result.json()
    console.log(data)
    const template = document.querySelector('#personal_card')
    const cont = document.querySelector('#personal');

    const temElement = template.content.cloneNode(true);
    temElement.querySelector('.personal-image').setAttribute('src',data['image'])
    temElement.querySelector('.personal-name').innerHTML="Name: "+data['name']
    temElement.querySelector('.personal-blood').innerHTML="Blood Group: "+data['blood_group']
    temElement.querySelector('.personal-age').innerHTML="Age: "+data['age']
    temElement.querySelector('.personal-sex').innerHTML="Gender: "+data['gender']
    temElement.querySelector('.personal-ph').innerHTML="Phone: "+data['phone']
    temElement.querySelector('.personal-address').innerHTML="Address: "+ data['address']
    console.log(temElement.querySelector('.doner-address'))
    cont.appendChild(temElement);

    return true;
}
let pid = localStorage.getItem('UserId')
console.log(pid)
let pro= profile('http://127.0.0.1:8000/rest/blood/info/'+pid)
console.log(pro)

final_logout()