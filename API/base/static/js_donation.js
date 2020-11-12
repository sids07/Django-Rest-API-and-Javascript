console.log("Fill the form");


async function create_donation(url, name, age, sex, ph, address, blood_group, image) {
    let authentication = localStorage.getItem('Authentication')
    let uid = localStorage.getItem('UserId')
    console.log(uid)
    let myToken = "Token"+" "+authentication
    console.log(myToken)
    console.log(parseInt(age),image)

    var formData = new FormData();
    formData.append('name',name);
    formData.append('age',parseInt(age));
    formData.append('address',address);
    formData.append('phone',parseInt(ph));
    formData.append('blood_group',blood_group);
    formData.append('gender',sex);
    formData.append('image',image);
    formData.append('user_id',uid);

   for (let key of formData.keys()){
       console.log(key,formData.get(key))
   }

    const result = fetch(url, {
        method: 'POST',
        headers: {
            'Authorization': myToken,
        },
        body: formData
    }).then(response =>
    console.log(response)
    ).catch(error=>
    console.log(error)
    )

//    console.log(result.method)

    if (!result.ok) {
        return false;
    }

    const data = await result.json()
    console.log(data)
    return true;
}


donationForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const form = e.target
            console.log("check");
            const isAuthorized = await create_donation(form['action'], form['inputName4'].value, form['inputAge4'].value,form['inputSex'].value,form['inputNumber'].value,form['inputAddress'].value,form['inputBlood'].value,form['myimg'].files[0]);

            if (isAuthorized) {
                window.location.href = '/doner';
                console.log("Signuped in")
            } else {
                form.reset();
                console.log("credential not matched")
            }
        });
