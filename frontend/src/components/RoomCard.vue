<script>
import Header from './Header.vue'
export default {
  components: { Header },
    props: {
        cardColor : String,
        roomNum : String,
        bldg : String,
        seatNum : String
    }
}   
</script>

<template>
    <div class="room-card">
        <div class="room-card-color">
        </div>
        <div class="room-card-text">
            <a>Room: {{roomNum}}<br>{{bldg}}
            </a>
        </div>
    </div>
</template>