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
        console.log(res);
      })
      .catch((err) => {
        console.log(err);
      })
      const events = [
        {
          id: 1,
          start: "2023-02-17T10:00:00",
          end: "2023-02-17T11:00:00",
          text: "Avlable",
          barColor: "green"
        },
        {
          id: 2,
          start: "2023-02-17T13:00:00",
          end: "2023-02-17T16:00:00",
          text: "Booked",
          barColor: "red"
        },
      ];
      this.calendar.update({events});
    }
  },
  mounted() {
    this.loadEvents();
  }
}
</script>
