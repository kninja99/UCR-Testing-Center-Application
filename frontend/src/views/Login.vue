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
        <footer class="login-trouble">
            <p>Trouble Connecting?</p>
            <p>Contact us at: <a href="mailto: sendhelp@ucr.edu">sendhelp@ucr.edu</a></p>
        </footer>
    </div>
</template>







