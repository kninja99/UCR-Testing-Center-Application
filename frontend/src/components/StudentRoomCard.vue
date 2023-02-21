<script>
export default {
    props: {
        // buttonHeader: String,
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
            <div class="room-card-element-class">
                Course: {{className}}
            </div>
            <div class="room-card-element-seats">
                Prof: {{profName}}
            </div>
        </div>
    </div>
</template>