<script>
import Header from './Header.vue'
export default {
  componenets: { Header },
    props: {
        cardColor : String,
        roomNum: Number,
        approval: Boolean,
        seatNum: Number,
        bldg: String
    },
    methods: {
        roomClickEvent() {
            this.$router.push({ path: `rooms/${this.$props.bldg}/${this.$props.roomNum}`});
        }
    },
}   
</script>

<template>
    <div @click="roomClickEvent" class="professor-room-card-element">
        <div class="professor-room-card-element-color">
        </div>

        <div class="room-card-element-text">
            <div class="room-card-element-location">
                Room: {{roomNum}}<br>{{bldg}}
            </div>
            <div class="room-card-element-seats">
                Seats: {{seatNum}}<br>Approval:{{approval}}
            </div>
        </div>
    </div>
</template>