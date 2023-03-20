<script>
    export default {
        props: {
            senderName: {
                type:String,
                required: true
            },
            subject: {
                type:String,
                required: true
            },
            message: {
                type:String,
                required: true
            },
            receivedDate: {
                type: String,
                required: true
            },
            receivedTime: {
                type: String,
                required: true
            },
            readStatus: {
                type: String,
                required: true
            }
        }
    }   
</script>

<template>
    <div class="proctor-inbox-element">
        <div class="sender-name">
            <p>{{senderName}}</p>
        </div>

        <div class="subject">
            <p>SUBJECT: {{subject}}</p>
        </div>
        
        <div class="message">
            <p>{{message}} </p>
        </div>

        <div class="received-date">
            <p>{{receivedDate}}<br>{{receivedTime}}</p>
        </div>

        <div class="read-status">
            <p>{{readStatus}}</p>
        </div>
    </div> 
</template>