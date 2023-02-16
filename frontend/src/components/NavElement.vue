<script>
export default {
    props: {
        navTitle: {
            type: String,
            required: true
        },
        imgName: {
            type: String,
            required: true
        },
        route: {
            type: String,
            required: true
        }
    }
}   
</script>

<template>
    <router-link :to="route" class="nav-comp">
        <img :src="require(`../assets/imgs/${imgName}`)" :alt="imgName">
        <h3>{{ navTitle }}</h3>
    </router-link>
</template>