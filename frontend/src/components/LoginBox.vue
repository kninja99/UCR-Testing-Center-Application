<template>
    <div class="login-wrapper">
        <div class="login-box">
            <h2>Sign In</h2>
            <form @submit.prevent="loginEvent">
                <input id = "username" type="text" placeholder="Username">
                <input id = "password" type="password" placeholder="Password">
                <button class = "login-btn">Login</button>
            </form>
        </div>
    </div>
    
</template>

<script>
    import axios from 'axios'
    export default {
        methods: {
            loginEvent(e) {
                // collecting our user data
                let loginForm = document.querySelector(".login-box form");
                let userName = document.querySelector("#username").value;
                let pass = document.querySelector("#password").value;
                let loginData = {
                username: userName ,
                password: pass
                };
                //authentication
                axios.post('/api/login/', loginData)
                .then((res) => {
                    window.sessionStorage.setItem("auth",res.data.token);
                    window.sessionStorage.setItem("validUser",true);
                    // getting our user type, note we need to pass a header argument with
                    // out auth token
                    axios.get('/api/account/getUserType',
                    {headers: {'Authorization':`token ${window.sessionStorage.getItem('auth')}`}})
                    .then((res) => {
                        window.sessionStorage.setItem("userType",res.data[0].user_type);
                        // temp login logic, this is where routing will go
                        alert("Login in successful");
                        loginForm.reset();
                    })
                    .catch((err) => {
                        console.log(err);
                    })
                })
                .catch((err) => {
                    console.log(err.response.data);
                });
                e.preventDefault(e);
            }
        },
    }
</script>