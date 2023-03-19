<script>
    // import AdminNotifButtons from './AdminNotifButtons.vue';
    export default {
        // components: {
        //     AdminNotifButtons
        // },
        props: {
            studentName: {
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
                type: String,
                required: true
            },
            schedTimeTo: {
                type: String,
                required: true
            },
            schedDate: {
                type: String,
                required: true
            }
        }
    }   
</script>

<template>
    <div class="status-element">
        <div class="profColumn">
            <p>{{studentName}}<br>{{className}}</p>
        </div>

        <div class="room-column">
            <p>Room: {{roomNum}}</p>
        </div>
        
        <div class="sched-column">
            <p>{{schedDate}}<br>{{schedTimeFrom}} - {{schedTimeTo}}</p>
        </div>
        <!-- <div class="admin-notif-buttons"> same styling -->
        <div class="prof-notif-icon">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <span class="flag-button"><i class="fa fa-flag"></i></span>
            <span>Student-Flagged</span>
        </div> 

    </div> 
</template>