
const loginForm = document.querySelector('#login-form');

console.log("A")
//fetchProtected().then((result) => {
//            console.log("ok")
//            console.log({ result });
//        });
console.log("b")
loginForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const form = e.target

            const isAuthorized = await auth(form['action'], form['uid'].value, form['passed'].value);

            if (isAuthorized) {
                window.location.href = '/';
                console.log("Logged in")
            } else {
                form.reset();
                console.log("credential not matched")
            }
        });
