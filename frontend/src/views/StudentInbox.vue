<script>
import Card from "../components/Card.vue"
import NavBar from "../components/NavBar.vue"
import NavBtn from "../components/NavBtn.vue";
import Header from "../components/Header.vue"
import CornerStyle from "../components/CornerStyle.vue"
import AdminNotif from "../components/AdminNotifText.vue"
import AdminNotifButtons from "../components/AdminNotifButtons.vue"

export default {
    components: {
        Card, NavBar, NavBtn, Header, CornerStyle, AdminNotif, AdminNotifButtons
    }
}
</script>

<template>
    <div class="page-content">
        <Header title="Student Inbox"/>
        <NavBtn/>
        <NavBar :nav-elements="[
            { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/student' },
            { title: 'Rooms', img: 'roomNav-icon.svg', route: '/student/rooms' },
            { title: 'Inbox', img: 'mailNav-icon.svg', route: '/student/inbox' },
            { title: 'Settings', img: 'settings-icon.svg', route: '/student/settings' },
            { title: 'My Account', img: 'profile-icon.svg', route: '/student/account' }]" />
        <div class="admin-notif-container">
            
        </div>
        <CornerStyle />
    </div>
</template>