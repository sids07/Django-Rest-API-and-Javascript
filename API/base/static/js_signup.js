console.log('Hello Signup')

async function create(url, username, email, password, confirm_password) {
    const result = await fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            'username': username,
            'email': email,
            'password': password,
            'confirm_password':confirm_password
        })
    });

    if (!result.ok) {
        return false;
    }

    const data = await result.json()
    console.log(data)
    return true;
}


signUpForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const form = e.target
            console.log("check");
            const isAuthorized = await create(form['action'], form['sname'].value, form['semail'].value,form['spass'].value,form['scpass'].value);

            if (isAuthorized) {
                window.location.href = '/login';
                console.log("Signuped in")
            } else {
                form.reset();
                console.log("Something went wrong")
            }
        });
