<script>
import axios from 'axios'
import Card from "../components/Card.vue"
import NavBar from "../components/NavBar.vue"
import CornerStyle from "../components/CornerStyle.vue"
import Header from "../components/Header.vue";
import AddRoomButton from "../components/AddRoomButton.vue"
import RoomCard from '../components/RoomCard.vue';
import NavBtn from "../components/NavBtn.vue";
export default {
    components: {
        Card, NavBar, Header, CornerStyle, AddRoomButton, RoomCard, NavBtn
    },
    data: () => ({
        rooms: []
    }),
    mounted: async function() {
        let authToken = window.sessionStorage.getItem('auth');
        // constructing url that works with our api
        let baseUrl = window.location.href;
        let index = baseUrl.indexOf('/',10);
        baseUrl = baseUrl.slice(0,index);
        // get request to get our testing rooms data
        await axios.get(`${baseUrl}/api/testingRooms`,
        {headers: {'Authorization':`token ${authToken}`}})
        .then((res) => {
            let data = res.data;
            data.forEach(element => {
                this.rooms.push(element);
            });
        })
        // for bad api request
        .catch((err) => {
            console.log(err);
        });
    }
}

</script>



<template>
    <div class="admin-home">
        <Header title="Testing Page"/>
        <NavBtn/>

        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements="[
        { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/admin' },
        { title: 'Rooms', img: 'roomNav-icon.svg', route: 'admin/rooms' },
        { title: 'Inbox', img: 'mailNav-icon.svg', route: 'admin/inbox' },
        { title: 'Settings', img: 'settings-icon.svg', route: 'admin/settings' },
        { title: 'My Account', img: 'profile-icon.svg', route: 'admin/account' }]" />
        <!-- <add-room-button:> -->
        <!-- <div class="card-container">
            <Card img-name="room-icon.svg" button-header="View Rooms" route="admin/rooms" />
            <Card img-name="email-icon.svg" button-header="View Inbox" route="admin/inbox" />
        </div> -->
        <div class="room-page-contents">
            <AddRoomButton buttonName="Add New Room"/>
            <div class = "room-cards">
                <RoomCard cardColor='18ACFF' roomNum='120' bldg='Winston Chung Hall' seatNum='45' />
                <RoomCard cardColor='18ACFF' roomNum='220' bldg='Winston Chung Hall' seatNum='45' />
            </div>
        </div>
        <CornerStyle />
    </div>
</template>