<script>
import StudentStatusButton from "../components/studentStatusButton.vue"
import studentStatusActions from "./studentStatusActions.vue";
export default {
    components: {
    StudentStatusButton,
    studentStatusActions,
},
    props: {
        studentName: String,
        className: String,
        instructorName: String
    }
}   
</script>


<template>
    <div class="status-element">
        <h1 class="status-text"><StudentStatusButton/>  </h1>
        <h2 class="status-text">{{ studentName }}</h2>
        <h3 class="status-text">{{ className }}</h3>
        <h4 class="status-text">{{ instructorName }}</h4>
        <h5 class="status-text"><studentStatusActions/></h5>
    </div>
</template>
