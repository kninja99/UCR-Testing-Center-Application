<script>
import Card from "../components/Card.vue"
import NavBar from "../components/NavBar.vue"
import CornerStyle from "../components/CornerStyle.vue"
import Header from "../components/Header.vue";
import Calendar from '../components/Calendar.vue'
import NavBtn from "../components/NavBtn.vue";
// import AddRoomButton from '../components/AddRoomButton.vue';
export default {
    components: {
    Card,
    NavBar,
    Header,
    CornerStyle,
    Calendar,
    NavBtn
}
}
</script>



<template>
     <div class="admin-home">
        <Header title="Testing Page"/>

        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements="[
        { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/admin' },
        { title: 'Rooms', img: 'roomNav-icon.svg', route: 'admin/rooms' },
        { title: 'Inbox', img: 'mailNav-icon.svg', route: 'admin/inbox' },
        { title: 'Settings', img: 'settings-icon.svg', route: 'admin/settings' },
        { title: 'My Account', img: 'profile-icon.svg', route: 'admin/account' },
        { title: 'Logout', img: 'logout-icon.svg', route: '/login' }]" />

        <NavBtn />       

        <div class="dp-container">
        <Calendar />
        </div>

        <CornerStyle />
    </div> 
</template>