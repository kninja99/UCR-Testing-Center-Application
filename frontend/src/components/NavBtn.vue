<template>
    <div v-on:click="navBarEvent()" class="nav-btn">
        <div class="nav-icon"></div>
        <div class="nav-icon"></div>
        <div class="nav-icon"></div>
    </div>
</template>

<script>
    export default {
        methods: {
            navBarEvent() {
                let navBar = document.querySelector(".nav-bar");
                navBar.classList.toggle("nav-active")
            }
        },
    }
</script>