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
            <p>{{day}}</p>
        </div>
        <div class="student-date-column">
            <p>{{date}}</p>
        </div>
        <div class="student-bldg-column">
            <p>{{bldgName}}</p>
        </div>
        <div class="student-room-column">
            <p>Room: {{roomNum}}</p>
        </div> 
        <div class="student-time-block-column">
            <p>{{timeBlock}}</p>
        </div> 
        <div class="student-seat-left-column">
            <p>{{seatLeft}} Seats Left</p>
        </div> 
        <div> 
            <p><button class="student-book-button">Book</button></p>
        </div>
    </div> 
</template>