<script>
    import Card from "../components/Card.vue"
    export default {
        components: {
         Card
        }
    }
</script>



<template>
    <div class="admin-home">
        <h1>Admin home page</h1>
        <Card img-name="room-icon.svg" button-header="View Rooms"/>
        <Card img-name="email-icon.svg" button-header="View Inbox"/>
    </div>
</template>