<template>
    <div class="calendar-container">
      <button @click="goBackEvent" class="go-back-btn">Go Back</button>
      <button @click="goToList" class="prof-student-list-btn">Student List</button>
      <div class="calendar-nav-btns">
        <button @click="previousWeek">Previous</button>
        <button @click="advanceWeek">Next</button>
      </div>
      <div v-if="!this.resView" class="calendar-book-btns">
        <button :value="0" @click="unbook" class = "unbook-btn">Unbook Sunday</button>
        <button :value="1" @click="unbook" class = "unbook-btn">Unbook Monday</button>
        <button :value="2" @click="unbook" class = "unbook-btn">Unbook Tuesday</button>
        <button :value="3" @click="unbook" class = "unbook-btn">Unbook Wednesday</button>
        <button :value="4" @click="unbook" class = "unbook-btn">Unbook Thursday</button>
        <button :value="5" @click="unbook" class = "unbook-btn">Unbook Friday</button>
        <button :value="6" @click="unbook" class = "unbook-btn">Unbook Saturday</button>
      </div>
      <div v-if="this.resView" class="calendar-book-btns">
        <button :value="0" @click="book">Book Sunday</button>
        <button :value="1" @click="book">Book Monday</button>
        <button :value="2" @click="book">Book Tuesday</button>
        <button :value="3" @click="book">Book Wednesday</button>
        <button :value="4" @click="book">Book Thursday</button>
        <button :value="5" @click="book">Book Friday</button>
        <button :value="6" @click="book">Book Saturday</button>
      </div>
      <DayPilotCalendar id="dp" :config="config" ref="calendar"/>
    </div>
  </template>
  
  <script>
  import { DayPilot,DayPilotCalendar } from '@daypilot/daypilot-lite-vue'
  import axios from 'axios'
  import PopOut from './PopOut.vue'
  export default {
    name: 'Calendar',
    props: {
      resView: Boolean
    },
    data: function () {
      return {
        config: {
          viewType: "Week",
          eventResizeHandling: "Disabled",
          eventMoveHandling: "Disabled",
          timeRangeSelectedHandling: "Disabled"
        },
        roomID: -1,
        dateDictionary: new Object()
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
              if(!this.resView && !availability[i].is_booked) {
                // ignoring avliable events if professor is viewing
                // their reservation
                continue;
              }
              // event to be added to events
              let event = {
                id: availability[i].id,
                start: startTime,
                end: endTime,
                text: eventText,
                barColor: eventBarColor
              }
              // building our key value for dateDictionary
              let tLocation = startTime.indexOf("T");
              let calendarDate = new DayPilot.Date(startTime.slice(0,tLocation));
              // adding event ids to our array associated with that date
              if(!this.dateDictionary[calendarDate.value]) {
                this.dateDictionary[calendarDate.value] = [event.id];
              }
              else {
                this.dateDictionary[calendarDate.value].push(event.id);
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
       * Booking event that is triggered when a user clicks a day that they want to book
       * @param  e event target 
       */
      async book(e) {
        let bookingErr = false;
        // gets target date index
        let dayOfWeek = Number(e.target.value);
        // gets correct date that we are selecting for booking
        let dateSelected = this.calendar.startDate.firstDayOfWeek("en-us").addDays(dayOfWeek);
        // getting all event IDs on target day
        let eventIdList = this.dateDictionary[dateSelected.value];
        console.log(eventIdList)
        // booking of each event
        let authToken = window.sessionStorage.getItem('auth');
        let baseUrl = window.location.href;
        let index = baseUrl.indexOf('/', 10);
        baseUrl = baseUrl.slice(0, index);
        for(let i = 0; i < eventIdList.length ; i++) {
          // getting calendar event
          let calendarEvent = this.calendar.events.find(eventIdList[i]);
          // now need to make booking in the backend
          let professorResData = {
            availability_id: eventIdList[i],
            approved: true
          }
          await axios.post(`${baseUrl}/api/professorReservation/`, professorResData, {headers: {'Authorization':`token ${authToken}`}})
          .then(res => {
            console.log(res);
            // updating calendar event on front end
            calendarEvent.data.barColor = "red";
            calendarEvent.data.text = "booked";
            this.calendar.update(calendarEvent);
          })
          .catch(err => {
            calendarEvent.data.barColor = "red";
            calendarEvent.data.text = "booked";
            this.calendar.update(calendarEvent);
            bookingErr = true;
          })
        }
        if(bookingErr) {
          alert('dates already booked');
        }
      },
      async unbook(e) {
        // gets target date index
        let dayOfWeek = Number(e.target.value);
        // gets correct date that we are selecting for booking
        let dateSelected = this.calendar.startDate.firstDayOfWeek("en-us").addDays(dayOfWeek);
        // getting all event IDs on target day
        let eventIdList = this.dateDictionary[dateSelected.value];
        // booking of each event
        let authToken = window.sessionStorage.getItem('auth');
        let baseUrl = window.location.href;
        let index = baseUrl.indexOf('/', 10);
        baseUrl = baseUrl.slice(0, index);
        try {
          for(let i = 0;i < eventIdList.length ; i++) {
          // getting calendar event
          let calendarEvent = this.calendar.events.find(eventIdList[i]);
          // now need to make booking in the backend
          let professorResData = {
            availability_id: eventIdList[i],
          }
          await axios.post(`${baseUrl}/api/professorReservation/delReservation/`, professorResData, {headers: {'Authorization':`token ${authToken}`}})
          .then(res => {
            console.log(res);
            this.calendar.events.remove(calendarEvent);
            delete this.dateDictionary[dateSelected.value];
          })
          .catch(err => {
            console.log(err);
          })
        }
        }
        catch {
          alert("Nothing to unbook");
        }
        
      },
      goBackEvent() {
        this.$router.go(-1);
      },
      goToList(){
        this.$router.push({ path: '/professor/rooms/prof-student-list'})
      }
    },
    mounted() {
      this.loadEvents();
    }
  }
  </script>
  