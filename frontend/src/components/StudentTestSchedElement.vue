<script>
import StudentTestViewVue from '../views/StudentTestView.vue';
    export default {
        data(){
            return {
                show: false,
                book: "Book",
            };
        },
        methods: {
            studentBookClick() {
                if(this.show) {
                    this.show = false;
                    this.book = "Book";
                    alert("Test Unbooked");
                }
                else {
                    this.show = true;
                    this.book = "Unbook";
                    alert("Test Booked");
                }
            },
        },
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
        <div class="student-test-sched-text">
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
        </div>
        <div class="student-book-button-container"> 
            <p v-if="!this.show"><button v-on:click="studentBookClick"
            class="student-book-button">{{book}}</button></p>
            <p v-else><button v-on:click="studentBookClick"
            class="student-book-button">{{book}}</button></p>
        </div>
        
    </div> 
</template>