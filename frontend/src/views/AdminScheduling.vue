<script>
import Card from "../components/Card.vue"
import NavBar from "../components/NavBar.vue"
import CornerStyle from "../components/CornerStyle.vue"
import Header from "../components/Header.vue";
import Calendar from '../components/Calendar.vue'
import NavBtn from "../components/NavBtn.vue";
import axios from "axios";
export default {
    components: {
        Card,
        NavBar,
        Header,
        CornerStyle,
        Calendar,
        NavBtn
    },
    data: () => ({
        testingRoomId: 0
    }),
    created: async function() {
            // getting variables needed for get request
            let authToken = window.sessionStorage.getItem('auth');
            let baseUrl = window.location.href;
            let index = baseUrl.indexOf('/',10);
            baseUrl = baseUrl.slice(0,index);
            // request to get testing room data
            await axios.get(`${baseUrl}/api/testingRooms/getTestingRoom/`, {
                headers: {'Authorization':`token ${authToken}`},
                params: {
                roomNum: this.$route.params.room,
                bldg: this.$route.params.bldg
                }
            })
            .then(res => {
                if(res.data.length > 0) {
                    this.testingRoomId=res.data[0].id;
                }
            })
            .catch((err) => {
                console.log(err);
            })
        }
}

</script>



<template>
     <div class="admin-home">
        <Header :title="this.$route.params.bldg + ' ' +this.$route.params.room"/>

        <!-- nav-elements is an array of objects that map nav elements -->
        <!-- object {title:Sting , img:String , route:String} -->
        <NavBar :nav-elements="[
        { title: 'Dashboard', img: 'dashBoard-icon.svg', route: '/admin' },
        { title: 'Rooms', img: 'roomNav-icon.svg', route: '/admin/rooms' },
        { title: 'Inbox', img: 'mailNav-icon.svg', route: '/admin/inbox' },
        { title: 'Settings', img: 'settings-icon.svg', route: '/admin/settings' },
        { title: 'My Account', img: 'profile-icon.svg', route: '/admin/account' }]" />

        <NavBtn />       

        <div class="dp-container">
            <Calendar v-if = this.testingRoomId  :testingRoomId = this.testingRoomId />
        </div>

        <CornerStyle/>
    </div> 
</template>