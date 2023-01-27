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
    <div class="room-card-element">

        <div class="room-card-element-color">
            Float
        </div>

        <div class="room-card-element-text">
            Room: {{roomNum}}<br>{{bldg}}
        </div>
    </div>
</template>