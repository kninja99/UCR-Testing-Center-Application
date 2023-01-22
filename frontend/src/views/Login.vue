<script>
import Header from "../components/Header.vue"
import LoginBox from "../components/LoginBox.vue";
export default {
    components: {
        Header, LoginBox
    }
}
</script>

<template>
    <div class="login">
        <Header title="Welcome to the UCR Testing Center"/>
        <LoginBox/>
        <footer class="login-trouble">Trouble Connecting?<br>Contact us at: sendhelp@ucr.edu</footer>
    </div>
</template>







