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
      console.log(this.$props.testingRoomId);
      // placeholder for an AJAX call
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
