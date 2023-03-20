<script>
    import AdminNotifButtons from './AdminNotifButtons.vue';
    export default {
        components: {
            AdminNotifButtons
        },
        methods: {
            checkbutton() {
                alert("Reservation Accepted")
            },
            mailbutton() {
                alert("Mailing")
            },
            rejectbutton() {
                alert("Reservation Declined")
            }
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
    <div class="admin-notif-element">
        <div class="profColumn">
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
            <button class = "checkbutton" v-on:click="checkbutton"><i class="fa fa-check"></i></button>
            <button class="mail-button" v-on:click="mailbutton"><i class="fa fa-envelope"></i></button>
            <button class="reject-button" v-on:click="rejectbutton"><i class="fa fa-close"></i></button>
        </div> 

    </div> 
</template>