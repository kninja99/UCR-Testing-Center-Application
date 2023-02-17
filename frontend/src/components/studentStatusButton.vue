<script>
export default {
    props: {
        buttonName: String
    }
}   
</script>

<template>
    <div href="#" class="student-status-button">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <span class="check-icon"><i class="fa fa-check"></i></span>
        <span class="add-text">{{buttonName}}</span>
    </div>
</template>