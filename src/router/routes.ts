import { RouteRecordRaw } from 'vue-router';
import VueSimpleCalendar from 'src/pages/VueSimpleCalendar.vue';
import ComparisonPage from 'src/pages/ComparisonPage.vue';
import OnboardingPage0 from 'src/pages/OnboardingPage0.vue';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {
        path: 'index',
        component: () => import('pages/IndexPage.vue'),
      },
      {
        path: 'schedulex',
        component: () => import('pages/ScheduleXCalendar.vue'),
      },
      {
        path: 'simplecalendar',
        component: VueSimpleCalendar,
      },
      {
        path: 'comparison',
        component: ComparisonPage,
      },
      {
        path: 'onboarding0',
        component: OnboardingPage0,
      },
    ],
  },
  // {
  //   path: '/schedulex',
  //   component: () => import('layouts/MainLayout.vue'),
  //   children: [
  //     {
  //       path: '',
  //       component: () => import('pages/ScheduleXCalendar.vue'),
  //     },
  //   ],
  // },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
