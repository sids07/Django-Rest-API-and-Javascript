console.log('Hello Signup')

async function create(url, username, email, password, confirm_password,age,sex,address,blood,phone,disease) {
    const result = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'username': username,
            'email': email,
            'password': password,
            'confirm_password':confirm_password,
            'age':age,
            'gender':sex,
            'address':address,
            'blood':blood,
            'phone':phone,
            'disease':disease
        })
    });

    if (!result.ok) {
        return false;
    }

    const data = await result.json()
    console.log(data)
    return true;
}

function getSelectedOptions(oList)
{
   var sdValues = [];
   for(var i = 0; i < oList.options.length; i++)
   {
      if(oList.options[i].selected == true)
      {
      sdValues.push(oList.options[i].value);
      }
   }
   return sdValues;
}
signUpForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const form = e.target
            console.log("check");
            console.log(form.elements["disease"])
            let a = getSelectedOptions(form.elements["disease"])
            console.log(a)
            const isAuthorized = await create(form['action'], form['sname'].value, form['semail'].value,form['spass'].value,form['scpass'].value,form['age'].value,form['sex'].value,form['address'].value,form['blood'].value,form['phone'].value,a);
            if (isAuthorized) {
                window.location.href = '/login';
                console.log("Signuped in")
            } else {
                form.reset();
                console.log("Something went wrong")
            }
        });
