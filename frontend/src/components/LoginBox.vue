<template>
    <div class="login-wrapper">
        <div class="login-box">
            <h2>Sign In</h2>
            <form @submit.prevent="loginEvent">
                <input id = "username" type="text" placeholder="Username" v-model="username">
                <input id = "password" type="password" placeholder="Password" v-model = "password">
                <p v-if="error.length" class="err-msg">{{ error }}</p>
                <button class = "login-btn">Login</button>
            </form>
        </div>
    </div>
    
</template>

<script>
    import axios from 'axios'
    export default {
        data: () => ({
            username: "",
            password: "",
            error:""
        }),
        methods: {
            loginEvent(e) {
                // collecting our user data
                let loginForm = document.querySelector(".login-box form");
                let userName = this.username;
                let pass = this.password;
                let loginData = {
                username: userName ,
                password: pass
                };
                //authentication
                axios.post('/api/login/', loginData)
                .then((res) => {
                    let auth = res.data.token
                    // getting our user type, note we need to pass a header argument with
                    // our auth token
                    axios.get('/api/account/getUserType',
                    {headers: {'Authorization':`token ${auth}`}})
                    .then((res) => {
                        let userType = res.data[0].user_type
                        // payLoad being passed to vuex store
                        let payLoad = {
                            authToken: auth,
                            userType: userType
                        }
                        this.$store.commit('login', payLoad);
                        alert("Login in successful");
                        this.$router.push(`/${userType}`);
                        loginForm.reset();
                    })
                    .catch((err) => {
                        console.log(err);
                        this.error = "Server Error, try again later or contact support"
                    })
                })
                .catch((err) => {
                    let errorMsg = err.response.data;
                    if(errorMsg.username || errorMsg.passowrd){
                        this.error = "Please input both username and password"
                    }
                    else if(errorMsg.non_field_errors){
                        this.error = "Can't log in with the provided credentials";
                    }
                    else {
                        this.error = "Server Error, try again later or contact support"
                    }
                    console.log(err.response.data);
                });
                e.preventDefault(e);
            }
        },
    }
</script>