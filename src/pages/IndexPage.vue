<template>
  <q-page class="row items-center justify-evenly">
    <example-component
      title="Example component"
      active
      :todos="todos"
      :meta="meta"
    ></example-component>
    <q-separator />
    <div></div>
  </q-page>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { Todo, Meta } from 'components/models';
import ExampleComponent from 'components/ExampleComponent.vue';
//import QPdfViewer from '@quasar/quasar-app-extension-qpdfviewer';
//import { QCalendar } from '@quasar/quasar-ui-qcalendar';
//import pdfjsLib from 'app/public/pdfjs/web/viewer';
import {
  createCalendar,
  viewDay,
  viewWeek,
  viewMonthGrid,
  viewMonthAgenda,
} from '@schedule-x/calendar';
import '@schedule-x/theme-default/dist/index.css';

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

const todos = ref<Todo[]>([
  {
    id: 1,
    content: 'ct1',
  },
  {
    id: 2,
    content: 'ct2',
  },
  {
    id: 3,
    content: 'ct3',
  },
  {
    id: 4,
    content: 'ct4',
  },
  {
    id: 5,
    content: 'ct5',
  },
]);

const meta = ref<Meta>({
  totalCount: 1200,
});
</script>
