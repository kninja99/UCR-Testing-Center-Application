<script>
    // import AdminNotifButtons from './AdminNotifButtons.vue';
    export default {
        // components: {
        //     AdminNotifButtons
        // },
        props: {
            adminName: {
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
            <p>{{adminName}}</p>
        </div>

        <div class="room-column">
            <p>Room: {{roomNum}}</p>
        </div>
        
        <div class="sched-column">
            <p>{{schedDate}}<br>{{schedTimeFrom}} - {{schedTimeTo}}</p>
        </div>
        <div class="prof-notif-icon"> <!-- same styling -->
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <span class="check-button"><i class="fa fa-check"></i></span>
            <span>Approved</span>
        </div> 

    </div> 
</template>