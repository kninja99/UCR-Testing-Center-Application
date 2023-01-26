<script>
export default {
    props: {
        buttonName: String
    }
}   
</script>

<template>
    <a href="#" class="edit-room-availability-button">
        <span class="edit-text">{{buttonName}}</span>
    </a>
</template>