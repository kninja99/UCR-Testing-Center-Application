<script>
import RoomCard from '../components/RoomCard.vue';
import NavBar from "../components/NavBar.vue";
import CornerStyle from "../components/CornerStyle.vue";
import AddRoomButton from "../components/AddRoomButton.vue";
import Header from "../components/Header.vue";
import NavBtn from "../components/NavBtn.vue";
import axios from "axios";
export default {
    components: {
        RoomCard, NavBar, Header, CornerStyle, NavBtn, AddRoomButton
    },
    data: () => ({
        rooms: [],
    }),
    created: async function () {
        let authToken = window.sessionStorage.getItem('auth');
        // constructing url that works with our api
        let baseUrl = window.location.href;
        let index = baseUrl.indexOf('/', 10);
        baseUrl = baseUrl.slice(0, index);
        // get request to get our testing rooms data
        await axios.get(`${baseUrl}/api/testingRooms`,
            { headers: { 'Authorization': `token ${authToken}` } })
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
    },
    methods: {
        goBackEvent() {
            this.$router.go(-1);
        }
    },
}
</script>



<template>
    <div class="page-content">
        <Header title="Select Room For New Reservation" />
        <NavBtn />

        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements="[
            { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/professor' },
            { title: 'Rooms', img: 'roomNav-icon.svg', route: '/professor/rooms' },
            { title: 'Inbox', img: 'mailNav-icon.svg', route: '/professor/inbox' },
            { title: 'Settings', img: 'settings-icon.svg', route: '/professor/settings' },
            { title: 'My Account', img: 'profile-icon.svg', route: '/professor/account' }]" />
        <div class="room-page-contents">
            <button @click="goBackEvent" class="go-back-btn">Go Back</button>
            <!-- need to add rooms that have avlavility -->
            <div class="room-cards">
                <RoomCard v-for="(room) in this.rooms" cardColor='18ACFF' :roomNum="room.room_number" :bldg="room.bldg"
                    :seatNum="room.capacity" />
            </div>
        </div>


        <CornerStyle />
    </div>
</template>