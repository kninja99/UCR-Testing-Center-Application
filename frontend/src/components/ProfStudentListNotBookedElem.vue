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
        <div class="sender-name"> <!-- same styling -->
            <span class="check-button"><i class="fa fa-check"></i></span>
        </div>
        <div class="sender-name"><!-- same styling -->{{ studentName }}</div>
        <div class="sender-name"><!-- same styling -->{{ className }}</div>
        <div class="sender-name"><!-- same styling -->
            <button v-on:click="notifyStudent" class="mail-button"><i class="fa fa-envelope"></i></button>
        </div>
    </div>
</template>