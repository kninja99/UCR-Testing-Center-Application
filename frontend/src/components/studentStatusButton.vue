<script>
export default {
    data() {
        return {
            toggle: false,
        };
    },
    methods: {
        statusChange() {
            this.toggle = !this.toggle;
            console.log("CLICKED");
        },
    }
}   
</script>

<template>
    <button @click="statusChange()" 
        class="status-toggle"
        :style="{
        backgroundColor: toggle ? 'Green' : 'red'
      }">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <span class="check-icon"><i class="fa fa-check"></i></span>
        <!--<span class="x-icon"><i class="fa fa-close"></i></span>-->
    </button>
    
</template>