<script>
export default {
    props: {
        buttonHeader: String,
        imgName: String,
        route: String
    }
}   
</script>

<template>
    <div class="card">
        <img class="card-logo" :src="require(`../assets/imgs/${imgName}`)" alt="logo">
        <a :href="route">
            <button class="card-btn">{{ buttonHeader }}</button>
        </a>
    </div>
</template>