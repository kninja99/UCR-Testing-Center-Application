<script>
import TestCard from "../components/TestCard.vue"
import NavBar from "../components/NavBar.vue"
import CornerStyle from "../components/CornerStyle.vue"
import Header from "../components/Header.vue";
import NavBtn from "../components/NavBtn.vue";
export default {
    components: {
        TestCard, NavBar, Header, CornerStyle, NavBtn
    }
}
</script>



<template>
    <div class="admin-home">
        <Header title="Testing Rooms"/>
        <NavBtn/>

        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements="[
        { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/proctor' },
        { title: 'Rooms', img: 'roomNav-icon.svg', route: 'proctor/rooms' },
        { title: 'Inbox', img: 'mailNav-icon.svg', route: 'proctor/inbox' },
        { title: 'Settings', img: 'settings-icon.svg', route: 'proctor/settings' },
        { title: 'My Account', img: 'profile-icon.svg', route: 'proctor/account' },
        { title: 'Logout', img: 'logout-icon.svg', route: '/login' }]" />
        <div class="card-container">
            <TestCard img-name="room-icon.svg" button-header="View Rooms" route="proctor/rooms" />
            <TestCard img-name="email-icon.svg" button-header="View Inbox" route="proctor/inbox" />
        </div>
        <CornerStyle />
    </div>
</template>
