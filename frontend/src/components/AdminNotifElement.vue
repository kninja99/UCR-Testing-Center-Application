<script>
import AdminNotifButtons from './AdminNotifButtons.vue';
    export default {
        components: {
            AdminNotifButtons
        },
        props: {
            profName: {
                type:String,
                required: true
            },
            className: {
                type:String,
                required: true
            },
            roomNum: {
                type:String,
                required: true
            },
            schedTimeFrom: {
                type: time,
                required: true
            },
            schedTimeTo: {
                type: time,
                required: true
            },
            schedDate: {
                type: Date,
                required: true
            }
        }
    }   

</script>



<template>
    <div class="admin-notif-container">
        <div class="prof-column">
            <p>Prof: {{profName}} <br>{{className}}</p>
        </div>
        <div class="room-column">
            <p>Room: {{roomNum}}</p>
        </div>
        <div class="sched-column">
            <p>Schedule: </p>
        </div>
    </div> 
</template>