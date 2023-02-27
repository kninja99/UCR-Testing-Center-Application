<script>
import Header from './Header.vue'
export default {
  components: { Header },
    props: {
        cardColor : String,
        roomNum : Number,
        bldg : String,
        seatNum : Number
    },
    methods: {
        roomClickEvent() {
            try {
                this.$router.push({ path: `rooms/${this.$props.bldg}/${this.$props.roomNum}`});
            }
            catch {
                alert("room is not reachable");
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
        }
    }
}   
</script>

<template>
    <div @click="roomClickEvent" class="room-card-element">
        <div class="room-card-element-color">
            <button v-if="this.isAdmin()" class = "room-actions">&#8942;</button>
            
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