<template>
  <DayPilotCalendar id="dp" :config="config"  ref="calendar"/>
</template>

<script>
import {DayPilotCalendar} from '@daypilot/daypilot-lite-vue'
import axios from 'axios'
export default {
  name: 'Calendar',
  props: {
    testingRoomId: Number
  },
  data: function() {
    return {
      config: {
        viewType: "Week",
        eventResizeHandling: "Disabled",
        eventMoveHandling: "Disabled",
        timeRangeSelectedHandling: "Disabled"
      }
    }
  },
  components: {
    DayPilotCalendar
  },
  computed: {
    calendar() {
      return this.$refs.calendar.control;
    }
  },
  methods: {
    async loadEvents() {
      let events = []
      // getting variables needed for get request
      let authToken = window.sessionStorage.getItem('auth');
      let baseUrl = window.location.href;
      let index = baseUrl.indexOf('/',10);
      baseUrl = baseUrl.slice(0,index);
      // get request for room avlability
      await axios.get(`${baseUrl}/api/testingRoomsAvailability/roomAvailability/`, {
        headers: {'Authorization':`token ${authToken}`},
        params: {
          id: this.$props.testingRoomId,
        }
      })
      .then((res) => {
        let avlability = res.data
        // populating events
        for(let i = 0; i < avlability.length ; i+=1 ) {
          let eventText;
          let eventBarColor;
          let startTime = `${avlability[i].date}T${avlability[i].start_time}`
          let endTime = `${avlability[i].date}T${avlability[i].end_time}`
          // determining the inner text and bar color
          if(avlability[i].is_booked){
            eventText = "Booked";
            eventBarColor = "red";
          }
          else {
            eventText = "Avalable";
            eventBarColor = "green";
          }
          // event to be added to events
          let event = {
            id: avlability[i].id,
            start: startTime,
            end: endTime,
            text: eventText,
            barColor: eventBarColor
          }
          events.push(event);
        }
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      })

      this.calendar.update({events});
    }
  },
  mounted() {
    this.loadEvents();
  }
}
</script>
