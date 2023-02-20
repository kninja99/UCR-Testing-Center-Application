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
                type: TimeRanges,
                required: true
            },
            schedTimeTo: {
                type: TimeRanges,
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
    <!-- 
            schedDateFrom: {
                type:Date,
                required: true
            },
            schedDateTo: {
                type:Date,
                required: true
            },
            schedTimeRange: {
                type:TimeRanges,
                required: true
            }

        <a :href="route" class= nav-comp>
        <img :src="require(`../assets/imgs/${imgName}`)" :alt="imgName">
        <h3>{{navTitle}}</h3>
    </a> -->
    <div class="admin-notif-element">
        <div class="prof-column">
            <p>Prof: {{profName}} <br>{{className}}</p>
        </div>

        <div class="room-column">
            <p>Room: {{roomNum}}</p>
        </div>
        
        <div class="sched-column">
            <p>Schedule: {{schedDate}}<br>{{schedTimeFrom}} - {{schedTimeTo}}</p>
        </div>
        <div class="admin-notif-buttons">
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
            <button class="check-button"><i class="fa fa-check"></i></button>
            <button class="mail-button"><i class="fa fa-envelope"></i></button>
            <button class="reject-button"><i class="fa fa-close"></i></button>
        </div> 

    </div> 
</template>