<script>
    export default {
        props: {
            navTitle: String,
            imgName: String,
            route: String
        }
    }   
</script>

<template>
    <a :href="route" class= nav-comp>
        <img :src="require(`../assets/imgs/${imgName}`)" :alt="imgName">
        <h3>{{navTitle}}</h3>
    </a>
</template>