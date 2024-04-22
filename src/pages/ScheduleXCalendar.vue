<template>
  ScheduleX 1.32
  <div>
    <a href="https://schedule-x.dev/docs">Documentation</a>
  </div>
  <q-page class="row items-center justify-evenly">
    <div>
      <ScheduleXCalendar :calendar-app="calendarApp" />
      <!-- <q-calendar
		  ref="calendar"
		  v-model="selectedDate"
		  view="month"
		  locale="en-us"
		  animated
		  no-active-date
		  transition-prev="slide-right"
		  transition-next="slide-left"
		  :selected-dates="selectedDates"
		/> -->
    </div>
  </q-page>
</template>

<script setup lang="ts">
//import { ref } from 'vue';
//import QPdfViewer from '@quasar/quasar-app-extension-qpdfviewer';
//import { QCalendar } from '@quasar/quasar-ui-qcalendar';
//import pdfjsLib from 'app/public/pdfjs/web/viewer';
import { ScheduleXCalendar } from '@schedule-x/vue';
import {
  createCalendar,
  viewDay,
  viewWeek,
  viewMonthGrid,
  viewMonthAgenda,
} from '@schedule-x/calendar';
import '@schedule-x/theme-default/dist/index.css';
import { createDragAndDropPlugin } from '@schedule-x/drag-and-drop';
import { createEventModalPlugin } from '@schedule-x/event-modal';

const calendarApp = createCalendar({
  locale: 'de-AT',
  views: [viewMonthGrid, viewMonthAgenda, viewWeek, viewDay],
  datePicker: {
    selectedDate: '2023-12-01',
  },
  defaultView: viewWeek.name,
  events: [
    {
      id: 1,
      title: 'Coffee with John',
      start: '2023-12-01',
      end: '2023-12-01',
    },
    {
      id: 2,
      title: 'Breakfast with Sam',
      description: 'Discuss the new project',
      location: 'Starbucks',
      start: '2023-11-29 05:00',
      end: '2023-11-29 06:00',
    },
    {
      id: 3,
      title: 'Gym',
      start: '2023-11-27 06:00',
      end: '2023-11-27 07:00',
      calendarId: 'leisure',
    },
    {
      id: 4,
      title: 'Media fasting',
      start: '2023-12-01',
      end: '2023-12-03',
      calendarId: 'leisure',
    },
    {
      id: 5,
      title: 'Some appointment',
      people: ['John'],
      start: '2023-12-03 03:00',
      end: '2023-12-03 04:30',
    },
    {
      id: 6,
      title: 'Other appointment',
      people: ['Susan', 'Mike'],
      start: '2023-12-03 03:00',
      end: '2023-12-03 04:00',
      calendarId: 'leisure',
    },
  ],
  calendars: {
    leisure: {
      colorName: 'leisure',
      lightColors: {
        main: '#1c7df9',
        container: '#d2e7ff',
        onContainer: '#002859',
      },
      darkColors: {
        main: '#c0dfff',
        onContainer: '#dee6ff',
        container: '#426aa2',
      },
    },
  },
  plugins: [createDragAndDropPlugin(), createEventModalPlugin()],
});

defineOptions({
  name: 'IndexPage',
});

// const selectedDate = ref<string>(new Date().toISOString());
// const selectedDates = ref<string[]>([]);

// function onToggleDate({ scope: any }) {
//   if (scope !== undefined) toggleDate(scope);
// }

// function toggleDate(scope) {
//   const date = scope.timestamp.date;
//   if (selectedDates.value.includes(date)) {
//     // remove the date
//     for (let i = 0; i < selectedDates.value.length; ++i) {
//       if (date === selectedDates.value[i]) {
//         selectedDates.value.splice(i, 1);
//         break;
//       }
//     }
//   } else {
//     // add the date if not outside
//     if (scope.outside !== true) {
//       selectedDates.value.push(date);
//     }
//   }
// }
</script>
