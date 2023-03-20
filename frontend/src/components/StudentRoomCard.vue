<script>
export default {
    props: {
        className: String,
        profName: String,
        route: String
    }
}   
</script>

<template>
    <router-link :to="route" class="student-room-card-element">
        <div class="student-room-card-element-color"></div>

        <div class="student-room-card-element-text">
            <div class="room-card-student">{{className}} <br> Prof {{profName}} </div>
        </div>
    </router-link>
</template>