<script>
    export default {
        props: {
            day: {
                type:String,
                required: true
            },
            date: {
                type:String,
                required: true
            },
            bldgName: {
                type:String,
                required: true
            },
            roomNum: {
                type: String,
                required: true
            },
            timeBlock: {
                type: String,
                required: true
            },
            seatLeft: {
                type: String,
                required: true
            }
        }
    }   
</script>

<template>
    <div class="student-test-sched-element">
        <div class="student-day-column">
            {{day}}
        </div>
        <div class="student-date-column">
            {{date}}
        </div>
        <div class="student-bldg-column">
            {{bldgName}}
        </div>
        <div class="student-room-column">
            Room: {{roomNum}}
        </div> 
        <div class="student-time-block-column">
            {{timeBlock}}
        </div> 
        <div class="student-seat-left-column">
            {{seatLeft}} Seats Left
        </div> 
        <div> 
            <button class="student-book-button">Book</button>
        </div>
    </div> 
</template>