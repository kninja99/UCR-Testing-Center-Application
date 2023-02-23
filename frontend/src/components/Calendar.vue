<template>
  <div class="calendar-container">
    <div class="calendar-nav-btns">
      <button @click="previousWeek">Previous</button>
      <button @click="togglePopout">Add Availability</button>
      <button @click="advanceWeek">Next</button>
    </div>
    <DayPilotCalendar id="dp" :config="config" ref="calendar" />
    <!-- custome popout for avlability form -->
    <PopOut v-if="popOutToggle">
      <div class="popout-header">
        <p class="popout-name">Make Room Availability</p>
        <button @click="togglePopout" class="close-popout">X</button>
      </div>
      <form class="availability-form">
        <h2 class="form-header">Time Range</h2>
        <div class="availability-inputs">
          <span>
            <h3>Start Time</h3>
            <input v-model="startTime" type="time" name="start-time" id="start-time" step="3600000">
          </span>
          <span>
            <h3>End Time</h3>
            <input v-model="endTime" type="time" name="start-time" id="start-time" step="3600000">
          </span>
        </div>
        <h2 class="form-header">Date Range</h2>
        <div class="availability-inputs">
          <span>
            <h3>Start Date</h3>
            <input v-model="startDate" type="date" name="start-date" id="start-date">
          </span>
          <span>
            <h3>End Date</h3>
            <input v-model="endDate" type="date" name="end-date" id="end-date">
          </span>
        </div>
        <button @click="addAvailabilityEvent" class="form-btn">Submit Availability</button>
      </form>
    </PopOut>
  </div>
</template>

<script>
import { DayPilotCalendar } from '@daypilot/daypilot-lite-vue'
import axios from 'axios'
import PopOut from './PopOut.vue'
export default {
  name: 'Calendar',
  data: function () {
    return {
      config: {
        viewType: "Week",
        eventResizeHandling: "Disabled",
        eventMoveHandling: "Disabled",
        timeRangeSelectedHandling: "Disabled"
      },
      roomID: -1,
      popOutToggle: false,
      startTime: "",
      endTime: "",
      startDate: "",
      endDate: ""
    }
  },
  components: {
    DayPilotCalendar,
    PopOut
  },
  computed: {
    calendar() {
      return this.$refs.calendar.control;
    }
  },
  methods: {
    /**
     * loads avlability for the room, this is done by making a request
     * to the backend
     */
    async loadEvents() {
      await this.getRoomId();
      let events = []
      // getting variables needed for get request
      let authToken = window.sessionStorage.getItem('auth');
      let baseUrl = window.location.href;
      let index = baseUrl.indexOf('/', 10);
      baseUrl = baseUrl.slice(0, index);
      // get request for room avlability
      await axios.get(`${baseUrl}/api/testingRoomsAvailability/roomAvailability/`, {
        headers: { 'Authorization': `token ${authToken}` },
        params: {
          id: this.roomID,
        }
      })
        .then((res) => {
          let availability = res.data
          // populating events
          for (let i = 0; i < availability.length; i += 1) {
            let eventText;
            let eventBarColor;
            let startTime = `${availability[i].date}T${availability[i].start_time}`
            let endTime = `${availability[i].date}T${availability[i].end_time}`
            // determining the inner text and bar color
            if (availability[i].is_booked) {
              eventText = "Booked";
              eventBarColor = "red";
            }
            else {
              eventText = "Avalable";
              eventBarColor = "green";
            }
            // event to be added to events
            let event = {
              id: availability[i].id,
              start: startTime,
              end: endTime,
              text: eventText,
              barColor: eventBarColor
            }
            events.push(event);
          }
        })
        .catch((err) => {
          console.log(err);
        })

      this.calendar.update({ events });
    },
    /**
     * getting room id from backend
     */
    async getRoomId() {
      // getting variables needed for get request
      let authToken = window.sessionStorage.getItem('auth');
      let baseUrl = window.location.href;
      let index = baseUrl.indexOf('/', 10);
      baseUrl = baseUrl.slice(0, index);
      // request to get testing room data
      await axios.get(`${baseUrl}/api/testingRooms/getTestingRoom/`, {
        headers: { 'Authorization': `token ${authToken}` },
        params: {
          roomNum: this.$route.params.room,
          bldg: this.$route.params.bldg
        }
      })
        .then(res => {
          this.roomID = res.data[0].id;
        })
        .catch((err) => {
          console.log(err);
        })
    },
    /**
     * Advance the week in dayplot calendar
     */
    advanceWeek() {
      this.calendar.startDate = this.calendar.startDate.addDays(7);
      this.calendar.update();
    },
    /**
     * will go back to previous week in dayplot calendar
     */
    previousWeek() {
      this.calendar.startDate = this.calendar.startDate.addDays(-7);
      this.calendar.update();
    },
    /**
     * toggleing our add availability popout
     */
    togglePopout() {
      if (this.popOutToggle) {
        this.popOutToggle = false;
      }
      else {
        this.popOutToggle = true;
      }
    },
    addAvailabilityEvent(e) {
      console.log("add avlability");
      // how to get data bindings
      console.log(`startTime:${this.startTime}`);
      console.log(`endTime:${this.endTime}`);
      console.log(`startDate;${this.startDate}`);
      console.log(`endDate:${this.endDate}`);
      console.log(`room id: ${this.roomID}`);
      let roomAvlability = {
        start_time: this.startTime,
        end_time: this.endTime,
        date: this.startDate,
        is_booked: false,
        testing_room_id: this.roomID
      }
      // getting variables needed for get request
      let authToken = window.sessionStorage.getItem('auth');
      let baseUrl = window.location.href;
      let index = baseUrl.indexOf('/', 10);
      baseUrl = baseUrl.slice(0, index);
      // axios.post(`${baseUrl}/api/testingRoomsAvailability/`, roomAvlability)
      // .then(res => {
      //   console.log("should be in db");
      //   console.log(res);
      // })
      // .catch(err => {
      //   console.log("this is an error");
      //   console.log(err);
      // })
      e.preventDefault(e);
    }
  },
  mounted() {
    this.loadEvents();
  }
}
</script>
