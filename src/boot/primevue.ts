import { boot } from 'quasar/wrappers';
import PrimeVue from 'primevue/config';
//import 'primevue/resources/themes/aura-light-green/theme.css';
//import '/src/css/themes/aura-light-green/theme.css';
import 'primeicons/primeicons.css';
import Wind from '../presets/wind';

//import { Button } from 'primevue/button';
import Button from 'primevue/button';

export default boot(({ app }) => {
  // Set i18n instance on app
  app.component('PrimeButton', Button);
  app.use(PrimeVue, {
    unstyled: true,
    pt: Wind,
  });
  //app.provide('Button', Button);
});
