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
    <a class="room-card">

        <div class="room-card-color">
            Float
        </div>

        <div class="room-card-text">
            Room: {{roomNum}}<br>{{bldg}}
        </div>
    </a>
</template>