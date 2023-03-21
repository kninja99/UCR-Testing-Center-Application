<script>
export default {
   
    methods: {
            notifyStudent() {
                alert("Messaged Student")
            },
        },
    props: {
        studentName: String,
        className: String
    }
}   
</script>


<template>
    <div class="proctor-inbox-element">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <div class="sender-name">
            <span class="reject-button"><i class="fa fa-close"></i></span>
        </div>
        <div class="sender-name">{{ studentName }}</div>
        <div class="sender-name">{{ className }}</div>
        <div class="sender-name">
            <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"> -->
            <button v-on:click="notifyStudent" class="mail-button"><i class="fa fa-envelope"></i></button>
        </div>
    </div>
</template>
