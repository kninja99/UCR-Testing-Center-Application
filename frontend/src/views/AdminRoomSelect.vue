<script>
import Card from "../components/Card.vue"
import NavBar from "../components/NavBar.vue"
import CornerStyle from "../components/CornerStyle.vue"
import Header from "../components/Header.vue";
import AddRoomButton from "../components/AddRoomButton.vue"
import RoomCard from '../components/RoomCard.vue';
export default {
    components: {
        Card, NavBar, Header, CornerStyle, AddRoomButton, RoomCard
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
        <!-- <add-room-button:> -->
        <!-- <div class="card-container">
            <Card img-name="room-icon.svg" button-header="View Rooms" route="admin/rooms" />
            <Card img-name="email-icon.svg" button-header="View Inbox" route="admin/inbox" />
        </div> -->
        <AddRoomButton buttonName="Add New Room"/>
        <div class = "room-cards">
            <RoomCard cardColor='yellow' roomNum='120' bldg='Winston Chung Hall' />
        </div>
        <CornerStyle />
    </div>
</template>