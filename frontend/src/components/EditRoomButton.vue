<script>
export default {
    props: {
        buttonName: String
    }
}   
</script>

<template>
    <a href="#" class="edit-room-button">
        <span class="edit-icon">~</span>
        <span class="edit-text">{{buttonName}}</span>
    </a>
</template>