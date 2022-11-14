<script>
    import Card from "../components/Card.vue"
    import NavBar from "../components/NavBar.vue"
    export default {
        components: {
         Card, NavBar
        }
    }
</script>



<template>
    <div class="admin-home">
        <header><h1>Admin Home Page</h1></header>
        <NavBar/>
        <div class="card-container">
            <Card img-name="room-icon.svg" button-header="View Rooms"/>
            <Card img-name="email-icon.svg" button-header="View Inbox"/>
        </div>
    </div>
</template>