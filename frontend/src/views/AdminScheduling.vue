<script>
import Card from "../components/Card.vue"
import NavBar from "../components/NavBar.vue"
import CornerStyle from "../components/CornerStyle.vue"
import Header from "../components/Header.vue";
import EditRoomAvailabilityButton from "../components/EditRoomAvailabilityButton.vue"
import EditRoomAvailabilityButton from "../components/EditRoomAvailabilityButton.vue";
export default {    
    components: {
    Card,
    NavBar,
    Header,
    CornerStyle,
    EditRoomAvailabilityButton
}
}
</script>



<template>
    <div class="admin-scheduling-home">
        <Header title="Admin Scheduling"/>

        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements="[
        { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/admin' },
        { title: 'Rooms', img: 'roomNav-icon.svg', route: 'admin/rooms' },
        { title: 'Inbox', img: 'mailNav-icon.svg', route: 'admin/inbox' },
        { title: 'Settings', img: 'settings-icon.svg', route: 'admin/settings' },
        { title: 'My Account', img: 'profile-icon.svg', route: 'admin/account' },
        { title: 'Logout', img: 'logout-icon.svg', route: '/login' }]" />
        
        <EditRoomAvailabilityButton buttonName="Edit Room Availability"/>
        <CornerStyle />

    </div>
</template>