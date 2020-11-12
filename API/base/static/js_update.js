console.log("Welcome")

async function profile_data(url) {
    let authentication = localStorage.getItem('Authentication')
    let myToken = "Token" + " " + authentication
    const result = await fetch(url, {
        method: 'GET',
        headers: {
            'Authorization': myToken,
        }
    });
    console.log(result.status)
    if (result.status==404){
    window.location.href=('/form')

    }
    if (!result.ok) {
        return false;
    }
    const data = await result.json()
    console.log(data['name'])
    document.querySelector('.name').setAttribute('value',data['name'])
    document.querySelector('.age').setAttribute('value',data['age'])
    document.querySelector('.blood').setAttribute('value',data['blood_group'])
    document.querySelector('.address').setAttribute('value',data['address'])
    document.querySelector('.ph').setAttribute('value',data['phone'])
    document.querySelector('.sex').setAttribute('value',data['gender'])

    return true;
}
let pid = localStorage.getItem('UserId')
console.log(pid)
let pro= profile_data('http://127.0.0.1:8000/rest/blood/info/'+pid)
console.log(pro)


async function profile_update(url, name, age, sex, ph, address, blood_group, image) {
    let authentication = localStorage.getItem('Authentication')
    let uid = localStorage.getItem('UserId')
    console.log(uid)
    let myToken = "Token"+" "+authentication
    console.log(myToken)

    var formData = new FormData();
        formData.append('name', name);
        formData.append('age', parseInt(age));
        formData.append('address', address);
        formData.append('phone', parseInt(ph));
        formData.append('blood_group', blood_group);
        formData.append('gender', sex);
        formData.append('image', image);

   for (let key of formData.keys()){
       console.log(key,formData.get(key))
   }

    const result = fetch(url, {
        method: 'PATCH',
        headers: {
            'Authorization': myToken,
        },
        body: formData
    })

//    console.log(result.method)

    if (!result.ok) {
        console.log(result)
        console.log("Res")
        return false;
    }

    const data = await result.json()
    console.log(data)
    return true;
}


updateForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const form = e.target
            console.log(form['myimg'].files[0]);
            let pid = localStorage.getItem('UserId')
            console.log(pid)
            let pro= form['action']+pid
            console.log(pro)
            const isAuthorized = await profile_update(pro, form['name'].value, form['age'].value,form['sex'].value,form['ph'].value,form['address'].value,form['blood'].value,form['myimg'].files[0]);
            console.log(isAuthorized)
            if (isAuthorized) {
                window.location.href = '/profile';
                console.log("Signuped in")
            } else {
                form.reset();
                console.log("Not updated Something went wrong")
            }
        });

