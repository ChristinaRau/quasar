<template>
  <div id="app">
    Vue Simple Calendar 7.0.1
    <div>
      <a href="https://github.com/richardtallent/vue-simple-calendar"
        >Documentation</a
      >
    </div>
    <h4>My Calendar</h4>
    <CalendarView
      :show-date="showDate"
      :time-format-options="{ hour: 'numeric', minute: '2-digit' }"
      locale="de-AT"
      :items="calendarItems"
      display-week-numbers
      item-top="10 em"
      item-content-height="10 em"
      class="theme-default holiday-us-traditional holiday-us-official"
      :style="{ height: '70dvh' }"
      show-times
      enable-drag-drop
    >
      <template #header>
        <!-- <CalendarViewHeader @input="setShowDate" :headerProps /> -->
      </template>
    </CalendarView>
  </div>
</template>
<script setup lang="ts">
import { ref } from 'vue';
import { CalendarView, CalendarViewHeader } from 'vue-simple-calendar';
import { ICalendarItem } from 'vue-simple-calendar/dist/src/ICalendarItem';

import 'vue-simple-calendar/dist/style.css';
import 'vue-simple-calendar/dist/css/default.css';

const showDate = ref(new Date());
const headerProps = ref();

function setShowDate(date: Date) {
  showDate.value = date;
}

const calendarItems = ref<ICalendarItem[]>([
  {
    id: '1',
    title: 'Coffee with John',
    startDate: new Date('2024-04-10 14:15'),
    endDate: new Date('2024-04-10 14:45'),
    tooltip: 'My tooltip 1',
    style: 'border: 1px solid black; background-color: lightblue',
  },
  {
    id: '2',
    title: 'Coffee with Lisa',
    startDate: new Date('2024-04-11 16:00'),
    endDate: new Date('2024-04-11 17:00'),
    tooltip: 'My tooltip 1',
    style: 'border: 1px solid deeppink; background-color: pink',
  },
  {
    id: '3',
    title: 'Zahnarzt',
    startDate: new Date('2024-04-15 14:00'),
    endDate: new Date('2024-04-15 15:30'),
    tooltip: 'My tooltip 1',
    style: 'border: 3px dotted limegreen; background-color: lightgreen',
  },
]);
</script>
<style scoped>
.calendar-controls {
  margin-right: 1rem;
  min-width: 14rem;
  max-width: 14rem;
}

.calendar-parent {
  display: flex;
  flex-direction: column;
  flex-grow: 1;
  overflow-x: hidden;
  overflow-y: hidden;
  max-height: 80vh;
  background-color: white;
}

/* For long calendars, ensure each week gets sufficient height. The body of the calendar will scroll if needed */
.cv-wrapper.period-month.periodCount-2 .cv-week,
.cv-wrapper.period-month.periodCount-3 .cv-week,
.cv-wrapper.period-year .cv-week {
  min-height: 6rem;
}

/* These styles are optional, to illustrate the flexbility of styling the calendar purely with CSS. */

/* Add some styling for items tagged with the "birthday" class */
.theme-default .cv-item.birthday {
  background-color: #e0f0e0;
  border-color: #d7e7d7;
}

.theme-default .cv-item.birthday::before {
  content: '\1F382'; /* Birthday cake */
  margin-right: 0.5em;
}

/* The following classes style the classes computed in myDateClasses and passed to the component's dateClasses prop. */
.theme-default .cv-day.ides {
  background-color: #ffe0e0;
}

.ides .cv-day-number::before {
  content: '\271D';
}

.cv-day.do-you-remember.the-21st .cv-day-number::after {
  content: '\1F30D\1F32C\1F525';
}
</style>
