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
        <!-- Temp header for styling reasons -->
        <header><h1>Admin Home Page</h1></header>
        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements = "[
            {title: 'Dashboard', img: 'dashBoard-icon.svg', route:'/admin'},
            {title: 'Rooms', img: 'roomNav-icon.svg', route:'admin/rooms'},
            {title: 'Inbox', img: 'mailNav-icon.svg', route:'admin/inbox'},
            {title: 'Settings', img: 'settings-icon.svg', route:'admin/settings'},
            {title: 'My Account', img: 'profile-icon.svg', route:'admin/account'},
            {title: 'Logout', img: 'logout-icon.svg', route:'/login'}]" />
        <div class="card-container">
            <Card img-name="room-icon.svg" button-header="View Rooms"/>
            <Card img-name="email-icon.svg" button-header="View Inbox"/>
        </div>
    </div>
</template>