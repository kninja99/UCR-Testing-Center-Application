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
    <div class="test-card">
        <a :href="route">
            <button class="test-card-btn">{{ buttonHeader }}</button>
        </a>
    </div>
</template>