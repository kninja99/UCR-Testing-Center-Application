<template>
    <div class ="action-buttons">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <button v-on:click="mailbutton" class="pmail-button">
            <span class="mail-icon"><i class="fa fa-envelope"></i></span>
        </button>            
        <button v-on:click="flagbutton" class="pflag-button">
            <span class="mail-icon"><i class="fa fa-flag"></i></span>
        </button>
    </div>
</template>
<script>
export default {
    methods: {
        mailbutton() {
            alert("Sending Email")
        },
        flagbutton() {
            alert("Student Flagged")
        },
    }
}   
</script>
