<script>
import axios from 'axios'
import Card from "../components/Card.vue"
import NavBar from "../components/NavBar.vue"
import CornerStyle from "../components/CornerStyle.vue"
import Header from "../components/Header.vue";
import AddRoomButton from "../components/AddRoomButton.vue"
import RoomCard from '../components/RoomCard.vue';
import NavBtn from "../components/NavBtn.vue";
import PopOut from '../components/PopOut.vue';
export default {
    components: {
        Card, NavBar, Header, CornerStyle, AddRoomButton, RoomCard, NavBtn, PopOut
    },
    data: () => ({
        rooms: [],
        popOutToggle: false,
        newRoomNumber: null,
        newRoomBldg: null,
        newRoomCap: null,
        error: false
    }),
    methods: {
        testToggle() {
            if (this.popOutToggle) {
                this.popOutToggle = false;
            }
            else {
                this.popOutToggle = true;
            }
        },
        closePopout(e) {
            if (e.target.className === "popout-close") {
                this.popOutToggle = false;
                this.newRoomNumber = this.newRoomBldg = this.newRoomCap = null;
            }
        },
        createNewRoomEvent(e) {

            let validRoom = this.newRoomFormCheck();
            if (validRoom) {
                //getting variables needed for request
                let authToken = window.sessionStorage.getItem('auth');
                let baseUrl = window.location.href;
                let index = baseUrl.indexOf('/', 10);
                baseUrl = baseUrl.slice(0, index);
                // getting form data
                let newRoom = {
                    room_number: this.newRoomNumber,
                    bldg: this.newRoomBldg,
                    capacity: this.newRoomCap
                }
                // api call to add room to database
                axios.post(`${baseUrl}/api/testingRooms/`, newRoom,
                    { headers: { 'Authorization': `token ${authToken}` } })
                    .then(res => {
                        console.log("new room created");
                    })
                    .catch(err => {
                        console.log(err);
                    });
                // also add new room to frontend
                // clear previous inputs and closes popout
                this.popOutToggle = false;
                this.newRoomNumber = this.newRoomBldg = this.newRoomCap = null;
                this.error = false;
                e.preventDefault(e);
            }
            else {
                // generate an error msg
                this.error = true;
                console.log("error");
                e.preventDefault(e);
            }
        },
        newRoomFormCheck() {
            if (!this.newRoomNumber || !this.newRoomBldg || !this.newRoomCap) {
                return false
            }
            else {
                return true
            }
        }
    },
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
    }
}

</script>



<template>
    <div class="page-content">
        <Header title="Testing Page" />
        <NavBtn />

        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements="[
            { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/admin' },
            { title: 'Rooms', img: 'roomNav-icon.svg', route: `/admin/rooms` },
            { title: 'Inbox', img: 'mailNav-icon.svg', route: '/admin/inbox' },
            { title: 'Settings', img: 'settings-icon.svg', route: '/admin/settings' },
            { title: 'My Account', img: 'profile-icon.svg', route: '/admin/account' }]" />
        <div class="room-page-contents">
            <AddRoomButton buttonName="Add New Room" v-on:click.native="testToggle" />
            <!-- renders all testing rooms in db -->
            <div class="room-cards">
                <RoomCard v-for="(room) in this.rooms" cardColor='18ACFF' :roomNum="room.room_number" :bldg="room.bldg"
                    :seatNum="room.capacity" />
            </div>
        </div>
        <PopOut v-on:click.native="closePopout" v-if="popOutToggle" class="new-room-popup" title="New Room">
            <form action="#" class="new-room-form">
                <span>
                    <label class="new-room-label" for="room-number">Room Number</label>
                    <input v-model="newRoomNumber" type="number" name="room-number" id="room-number" placeholder="142"
                        min="1">
                </span>
                <span>
                    <label class="new-room-label" for="room-bldg">Building</label>
                    <input v-model="newRoomBldg" type="Text" name="room-bldg" id="room-bldg"
                        placeholder="Winston Chung Hall">
                </span>
                <span>
                    <label class="new-room-label" for="room-capacity">Capacity</label>
                    <input v-model="newRoomCap" type="number" name="room-capacity" id="room-capacity" placeholder="50"
                        min="1">
                </span>
                <p v-if="this.error" class="err-msg">Make Sure you fill in all inputs</p>
                <button @click="createNewRoomEvent" id="create-room-btn">Create</button>
            </form>
        </PopOut>
        <CornerStyle />
    </div>
</template>
