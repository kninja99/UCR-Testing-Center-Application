<script>
import Header from './Header.vue'
export default {
  componenets: { Header },
    props: {
        cardColor : String,
        room: Number,
        approval: Boolean,
        seats: Number,
        building: String
    }
}   
</script>

<template>
    <div class="professor-room-card-element">
        <div class="professor-room-card-element-color">
        </div>

        <div class="room-card-element-text">
            <div class="room-card-element-location">
                Room: {{roomNum}}<br>Bldg:{{bldg}}
            </div>
            <div class="room-card-element-seats">
                Seats: {{seatNum}}<br>Approval:{{approval}}
            </div>
        </div>
    </div>
</template>