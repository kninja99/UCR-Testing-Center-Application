<script>
import Card from "../components/Card.vue"
import NavBar from "../components/NavBar.vue"
import CornerStyle from "../components/CornerStyle.vue";
export default {
    components: {
        Card, NavBar, CornerStyle,
import Header from "../components/Header.vue"
export default {
    components: {
        Card, NavBar, Header
    }
}
}
}
</script>



<template>
    <div class="admin-home">
        <Header title="Admin Home Page"/>

        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements="[
        { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/admin' },
        { title: 'Rooms', img: 'roomNav-icon.svg', route: 'admin/rooms' },
        { title: 'Inbox', img: 'mailNav-icon.svg', route: 'admin/inbox' },
        { title: 'Settings', img: 'settings-icon.svg', route: 'admin/settings' },
        { title: 'My Account', img: 'profile-icon.svg', route: 'admin/account' },
        { title: 'Logout', img: 'logout-icon.svg', route: '/login' }]" />
        <div class="card-container">
            <Card img-name="room-icon.svg" button-header="View Rooms" route="admin/rooms" />
            <Card img-name="email-icon.svg" button-header="View Inbox" route="admin/inbox" />
        </div>
        <CornerStyle />
    </div>
</template>