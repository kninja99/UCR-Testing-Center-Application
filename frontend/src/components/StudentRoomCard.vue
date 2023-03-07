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
        <div class="student-room-card-element-color">
        </div>

        <div class="room-card-element-text">
            {{className}}<br>Prof {{profName}}
        </div>
    </router-link>
</template>