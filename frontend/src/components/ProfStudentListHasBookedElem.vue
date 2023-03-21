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
        <h1 class="sender-name">
            <span class="reject-button"><i class="fa fa-close"></i></span>
        </h1>
        <h2 class="sender-name">{{ studentName }}</h2>
        <h3 class="sender-name">{{ className }}</h3>
        <h4 class="sender-name">
            <!-- <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"> -->
            <button v-on:click="notifyStudent" class="mail-button"><i class="fa fa-envelope"></i></button>
        </h4>
    </div>
</template>
