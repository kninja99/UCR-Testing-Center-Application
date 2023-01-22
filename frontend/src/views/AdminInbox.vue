<script>
import Card from "../components/Card.vue"
import NavBar from "../components/NavBar.vue"
import Header from "../components/Header.vue"
import CornerStyle from "../components/CornerStyle.vue"
import AdminNotif from "../components/AdminNotifText.vue"
import AdminNotifButtons from "../components/AdminNotifButtons.vue"

export default {
    components: {
        Card, NavBar, Header, CornerStyle, AdminNotif, AdminNotifButtons
    }
}
</script>

<template>
    <div class="admin-inbox">
        <Header title="Admin Inbox"/>
        <NavBar :nav-elements="[
            { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/admin' },
            { title: 'Rooms', img: 'roomNav-icon.svg', route: 'admin/rooms' },
            { title: 'Inbox', img: 'mailNav-icon.svg', route: 'admin/inbox' },
            { title: 'Settings', img: 'settings-icon.svg', route: 'admin/settings' },
            { title: 'My Account', img: 'profile-icon.svg', route: 'admin/account' },
            { title: 'Logout', img: 'logout-icon.svg', route: '/login' }]" />
        <!-- <AdminNotif [{profName="Prof Allan Knight"}, {className="CS 061"}, {roomNum="234"}]" /> -->
        <AdminNotif profName='Allan Knight' className='CS061' roomNum='234' />
        <CornerStyle />
    </div>
</template>