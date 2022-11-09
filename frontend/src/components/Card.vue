<script>
    export default {
        props: {
            buttonHeader: String,
            imgName: String
        }
    }   
</script>

<template>
    <div class="card">
        <img class="card-logo" :src="require(`../assets/imgs/${imgName}`)" alt="logo">
        <button class="card-btn">{{buttonHeader}}</button>
    </div>
</template>