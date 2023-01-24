<script>
export default {
    props: {
        buttonName: String
    }
}   
</script>

<template>
    <a href="#" class="add-room-button">
        <span class="add-icon">+</span>
        <span class="add-text">{{buttonName}}</span>
    </a>
</template>