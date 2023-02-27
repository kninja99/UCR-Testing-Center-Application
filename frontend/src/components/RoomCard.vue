<script>
import Header from './Header.vue'
import axios from 'axios'
export default {
  components: { Header },
    props: {
        cardColor : String,
        roomNum : Number,
        bldg : String,
        seatNum : Number
    },
    data: () => ({
        roomActions: false
    }),
    methods: {
        roomClickEvent(e) {
            // checking to make sure we aren't click on our action areas
            if(e.target.className != "room-actions-btn" 
            && e.target.className != "admin-room-actions" 
            && e.target.className != "remove-room-btn"){
                try {
                    this.$router.push({ path: `rooms/${this.$props.bldg}/${this.$props.roomNum}`});
                }
                catch {
                    alert("room is not reachable");
                }
            }
        }, 
        /**
         * checks to see if a user is admin, if so it will render admin actions
         */
        isAdmin() {
            if(window.sessionStorage.getItem("userType") === 'admin') {
                return true;
            }
            else {
                return false;
            }
        },
        toggleRoomActions() {
            if(this.roomActions) {
                this.roomActions = false;
            }
            else {
                this.roomActions = true;
            }
        },
        async removeRoomEvent() {
            let roomId = -1
            let authToken = window.sessionStorage.getItem('auth');
            let baseUrl = window.location.href;
            let index = baseUrl.indexOf('/', 10);
            baseUrl = baseUrl.slice(0, index);
            await axios.get(`${baseUrl}/api/testingRooms/getTestingRoom/`, {
                headers: { 'Authorization': `token ${authToken}` },
                params: {
                    roomNum: this.$props.roomNum,
                    bldg: this.$props.bldg
                }
            })
            .then(res => {
                roomId = res.data[0].id;
            })
            .catch((err) => {
                console.log(err);
            })
            console.log(roomId);
            // removing element from dom
            this.$destroy();
            this.$el.parentNode.removeChild(this.$el);
        }
    }
}   
</script>

<template>
    <div @click="roomClickEvent" class="room-card-element">
        <div class="room-card-element-color">
            <button @click="toggleRoomActions" v-if="this.isAdmin()" class = "room-actions-btn">&#8942;</button>
            <div v-if="this.roomActions" class="admin-room-actions">
                <button @click="removeRoomEvent" class="remove-room-btn">Remove</button>
            </div>
        </div>

        <div class="room-card-element-text">
            <div class="room-card-element-location">
                Room: {{roomNum}}<br>{{bldg}}
            </div>
            <div class="room-card-element-seats">
                Seats: {{seatNum}}
            </div>
        </div>
    </div>
</template>