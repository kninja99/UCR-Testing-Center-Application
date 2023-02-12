<script>
import Header from './Header.vue'
export default {
  components: { Header },
    props: {
        cardColor : String,
        roomNum : String,
        bldg : String,
        seatNum : String
    },
    methods: {
        roomClickEvent() {
            this.$router.push('/proctor/rooms/testTimes');
        }
    }
}   
</script>

<template>
    <div @click="roomClickEvent" class="room-card-element">
        <div class="room-card-element-color">
            
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