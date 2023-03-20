<script>
import ProfRoomCard from "../components/ProfessorRoomCard.vue"
import NavBar from "../components/NavBar.vue"
import CornerStyle from "../components/CornerStyle.vue"
import AddRoomButton from "../components/AddRoomButton.vue"
import Header from "../components/Header.vue";
import NavBtn from "../components/NavBtn.vue";
import axios from "axios"
export default {
    data: () => ({
        rooms: [],
    }),
    components: {
        ProfRoomCard, NavBar, Header, CornerStyle, NavBtn, AddRoomButton
    },
    methods: {
        routeToReservations() {
            this.$router.push(`reservation/select-room`);
        }
    },
    created: async function () {
        let authToken = window.sessionStorage.getItem('auth');
        // constructing url that works with our api
        let baseUrl = window.location.href;
        let index = baseUrl.indexOf('/', 10);
        baseUrl = baseUrl.slice(0, index);
        // get request to get our testing rooms data
        await axios.get(`${baseUrl}/api/professorReservation/myReservedRooms/`,
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
    }
}
</script>



<template>
    <div class="page-content">
        <Header title="Instructor Portal" />
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
            <AddRoomButton v-on:click.native="routeToReservations" buttonName="Make New Reservation" />
            <div class="room-cards">
                <ProfRoomCard v-for="(room) in this.rooms" cardColor='18ACFF' :roomNum="room.room_number" :bldg="room.bldg"
                    :seatNum="room.capacity" :approval="true"/>
            </div>
        </div>


        <CornerStyle />
    </div>
</template>