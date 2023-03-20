<script>
    export default {
        data(){
            return {
                active: false,
            };
        },
        methods: {
            procInboxClick() {
                this.active = true;
            },
        },
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
    <button @click="procInboxClick" 
        class="proctor-inbox-element" 
        :style="{
            font: active? 'unset' : 'bold',
            readStatus: active? 'Read' : 'Unread'
            }">
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
    </button> 
</template>