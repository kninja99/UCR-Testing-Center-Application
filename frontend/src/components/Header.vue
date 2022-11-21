<script>
    export default {
        props: {
            title: String
        }
    }
</script>



<template>
    <header class="header">
        <div class="UCR-logo">
            <img src="../assets/imgs/UCRiverside-icon.svg">
        </div>
        <h1 class = theHeader>{{title}}</h1>
    </header>
</template>