<script>
export default {
    props: {
        className: String,
        profName: String
    }
}   
</script>

<template>
    <div class="student-room-card-element">
        <div class="student-room-card-element-color">
        </div>

        <div class="room-card-element-text">
            {{className}}<br>Prof {{profName}}
        </div>
    </div>
</template>