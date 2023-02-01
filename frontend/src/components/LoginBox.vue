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
                let userName = document.querySelector("#username").value;
                let pass = document.querySelector("#password").value;
                let loginData = {
                username: userName ,
                password: pass
                };
                //authentication
                axios.post('/api/login/', loginData)
                .then((res) => {
                    console.log(res);
                })
                .catch((err) => {
                    console.log(err.response.data);
                });
                e.preventDefault(e);
            }
        },
    }
</script>