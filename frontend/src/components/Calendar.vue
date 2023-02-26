<template>
  <div class="calendar-container">
    <div class="calendar-nav-btns">
      <button @click="previousWeek">Previous</button>
      <button @click="advanceWeek">Next</button>
    </div>
    <DayPilotCalendar id="dp" :config="config" ref="calendar"/>
    <p>* hint: you can use the calendar to make new availabilitys by clicking and dragging</p>
  </div>
</template>

<script>
import { DayPilot,DayPilotCalendar } from '@daypilot/daypilot-lite-vue'
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
        /**
         * Add a new avlability to a testing room bassed off a time
         * range selection done on the dayplot calendar
         * @param {*} args args that are supplied from time range select event in dayplot
         */
        onTimeRangeSelected: async (args) => {
          //getting variables needed for request (commented out so I can figure out mass booking)
          let authToken = window.sessionStorage.getItem('auth');
          let baseUrl = window.location.href;
          let index = baseUrl.indexOf('/', 10);
          baseUrl = baseUrl.slice(0, index);
          // start and end dates from time select
          let initStart = args.start;
          let initEnd = args.end;
          // while loop that will break our time selection up into
          // hour blocks
          while(initStart < initEnd) {
            let advancedHour = initStart.addHours(1);
            // roomAvailability structure for api call
            let roomAvailability = {
              start_time: `${initStart.getHours()}:${initStart.getMinutes()}`,
              end_time: `${advancedHour.getHours()}:${advancedHour.getMinutes()}`,
              date: `${initStart.getYear()}-${initStart.getMonth()+1}-${initStart.getDay()}`,
              is_booked: false,
              testing_room_id: this.roomID
            };
            // api call that will be used to send this room avalability to db
            await axios.post(`${baseUrl}/api/testingRoomsAvailability/`, roomAvailability, {headers: {'Authorization':`token ${authToken}`}})
            .then(res => {
              // updating our calendar event with new event if api call works
              this.calendar.events.add({
                start: initStart,
                end: initStart.addHours(1),
                id: res.data.id,
                text: "Available",
                barColor: "green"
              });
            })
            // error handling
            .catch(err => {
              // checks for unique feild error
              if(err.response.data.non_field_errors) {
                alert(`${roomAvailability.date} ${roomAvailability.start_time}-${roomAvailability.end_time} already has a availability assigned to it`)
              }
              else {
                console.log("API Error");
                console.log(err);
              }
            })
            // increment are start time for next event
            initStart = advancedHour;
          }
        },
        onBeforeEventRender: async (args) => {
          args.data.areas = [
          {
            cssClass: "scheduler_default_event_delete",
            action: "None",
            visibility: "Visible",
            onClick: args => {
              console.log("event deleteing");
              // have to make api call to delete, can use args.source.data.id
              // (which is our id that matches in db)
              console.log(args.source)
              // will remove event from calendar
              //this.calendar.events.remove(args.source);
            }
          }];
        }
      },
      roomID: -1
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
              eventText = "Available";
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
    }
  },
  mounted() {
    this.loadEvents();
  }
}
</script>
