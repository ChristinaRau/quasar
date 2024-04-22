<template>
  Vergleich der UI Komponenten

  <table>
    <tr>
      <th></th>
      <th>Ionic</th>
      <th>Quasar</th>
      <th>PrimeVue</th>
    </tr>
    <tr>
      <th>Button</th>
      <td>
        <i class="pi pi-check"></i>
        <div>ion-button</div>
      </td>
      <td><q-btn>Button</q-btn></td>
      <td><Button>Button</Button></td>
    </tr>
    <tr>
      <th>Date picker</th>

      <td>
        <i class="pi pi-check"></i>
        <div>ion-input type="date"</div>
      </td>
      <td>
        <q-input filled v-model="date" mask="date" :rules="['date']">
          <template v-slot:append>
            <q-icon name="event" class="cursor-pointer">
              <q-popup-proxy
                cover
                transition-show="scale"
                transition-hide="scale"
              >
                <q-date v-model="date">
                  <div class="row items-center justify-end">
                    <q-btn v-close-popup label="Close" color="primary" flat />
                  </div>
                </q-date>
              </q-popup-proxy>
            </q-icon>
          </template>
        </q-input>
      </td>
      <td><Calendar v-model="date" /></td>
    </tr>

    <tr>
      <th>Time picker</th>
      <td>
        <i class="pi pi-check"></i>
        <div>ion-input type="time"</div>
      </td>
      <td>
        <h6>Inline:</h6>
        <q-time v-model="time" format24h now-btn />
        <h6>Not inline:</h6>
        <q-input filled v-model="time" mask="time" :rules="['time']">
          <template v-slot:append>
            <q-icon name="access_time" class="cursor-pointer">
              <q-popup-proxy
                cover
                transition-show="scale"
                transition-hide="scale"
              >
                <q-time v-model="time" format24h now-btn>
                  <div class="row items-center justify-end">
                    <q-btn v-close-popup label="Close" color="primary" flat />
                  </div>
                </q-time>
              </q-popup-proxy>
            </q-icon>
          </template>
        </q-input>
      </td>
      <td>
        <h6>Inline:</h6>
        <Calendar id="calendar-timeonly" v-model="time" timeOnly inline />

        <h6>Not inline:</h6>
        <Calendar id="calendar-timeonly" v-model="time" timeOnly />
      </td>
    </tr>

    <tr>
      <th>Slider</th>
      <td>
        <i class="pi pi-check"></i>
        <div>ion-range</div>
      </td>
      <td><q-slider v-model="sliderValue" /></td>
      <td><Slider v-model="sliderValue" /></td>
    </tr>

    <tr>
      <th>Dropdown</th>
      <td>
        <i class="pi pi-check"></i>
        <div>ion-select</div>
      </td>
      <td>
        <q-select
          outlined
          v-model="selectedCity"
          :options="cities"
          label="Select a City"
        />
      </td>
      <td>
        <Dropdown
          v-model="selectedCity"
          :options="cities"
          placeholder="Select a City"
        />
      </td>
    </tr>

    <tr>
      <th>File picker</th>
      <td>
        <i class="pi pi-times"></i>
      </td>
      <td>
        <q-file
          outlined
          v-model="file"
          label="Choose file"
          bottom-slots
          clearable
          counter
        >
          <template v-slot:prepend>
            <q-icon name="attachment" />
          </template>
        </q-file>
      </td>
      <td>
        <FileUpload
          show-cancel-button
          v-model="file"
          mode="basic"
          name="demo[]"
          url="/api/upload"
          :maxFileSize="1000000"
        />
      </td>
    </tr>

    <tr>
      <th>File picker drag and drop</th>
      <td>
        <i class="pi pi-times"></i>
      </td>
      <td>
        <i class="pi pi-times"></i>
      </td>

      <td>
        <FileUpload
          name="demo[]"
          url="/api/upload"
          :multiple="true"
          :maxFileSize="1000000"
        >
          <template #empty>
            <p>Drag and drop files to here to upload.</p>
          </template>
        </FileUpload>
      </td>
    </tr>
    <tr>
      <th>Toggle</th>
      <td>
        <i class="pi pi-check"></i>
        <div>ion-toggle</div>
      </td>
      <td>
        <div class="q-pa-md q-gutter-sm">
          <div>
            <q-toggle v-model="toggle" icon="alarm" />
            <q-toggle
              v-model="toggle"
              color="pink"
              icon="mail"
              label="Same Icon for each state"
            />
          </div>

          <div>
            <q-toggle
              v-model="toggle"
              checked-icon="check"
              color="green"
              unchecked-icon="clear"
            />
            <q-toggle
              v-model="toggle"
              checked-icon="check"
              color="red"
              label="Different icon for each state"
              unchecked-icon="clear"
            />
          </div>
        </div>
      </td>
      <td>
        <h6>InputSwitch:</h6>
        <InputSwitch v-model="toggle" />
        <h6>ToggleButton:</h6>
        <ToggleButton v-model="toggle" onLabel="On" offLabel="Off" />
      </td>
    </tr>
    <tr>
      <th>List</th>
      <td>
        <i class="pi pi-check"></i>
        <div>ion-list</div>
      </td>
      <td>
        <div class="q-pa-md" style="max-width: 350px">
          <q-list>
            <q-item>
              <q-item-section>
                <q-item-label>Single line item</q-item-label>
                <q-item-label caption lines="2"
                  >Secondary line text. Lorem ipsum dolor sit amet, consectetur
                  adipiscit elit.</q-item-label
                >
              </q-item-section>

              <q-item-section side top>
                <q-item-label caption>5 min ago</q-item-label>
                <q-icon name="star" color="yellow" />
              </q-item-section>
            </q-item>

            <q-separator spaced inset />

            <q-item>
              <q-item-section>
                <q-item-label>Single line item</q-item-label>
                <q-item-label caption
                  >Secondary line text. Lorem ipsum dolor sit amet, consectetur
                  adipiscit elit.</q-item-label
                >
              </q-item-section>

              <q-item-section side top>
                <q-item-label caption>Voted!</q-item-label>
              </q-item-section>
            </q-item>

            <q-separator spaced inset />

            <q-item>
              <q-item-section>
                <q-item-label>Single line item</q-item-label>
                <q-item-label caption
                  >Secondary line text. Lorem ipsum dolor sit amet, consectetur
                  adipiscit elit.</q-item-label
                >
              </q-item-section>

              <q-item-section side top>
                <q-badge color="teal" label="10k" />
              </q-item-section>
            </q-item>

            <q-separator spaced inset />

            <q-item>
              <q-item-section>
                <q-item-label>Single line item</q-item-label>
                <q-item-label caption
                  >Secondary line text. Lorem ipsum dolor sit amet, consectetur
                  adipiscit elit.</q-item-label
                >
              </q-item-section>

              <q-item-section side top>
                <q-item-label caption>2 min ago</q-item-label>
                <div class="text-orange">
                  <q-icon name="star" />
                  <q-icon name="star" />
                  <q-icon name="star" />
                </div>
              </q-item-section>
            </q-item>

            <q-separator spaced inset />

            <q-item>
              <q-item-section>
                <q-item-label>Single line item</q-item-label>
                <q-item-label caption
                  >Secondary line text. Lorem ipsum dolor sit amet, consectetur
                  adipiscit elit.</q-item-label
                >
              </q-item-section>

              <q-item-section side top>
                <q-item-label caption>meta</q-item-label>
              </q-item-section>
            </q-item>
          </q-list>
        </div>
      </td>
      <td>
        <i class="pi pi-question" style="font-size: 1.5rem"></i>
      </td>
    </tr>
    <tr>
      <th>Spinner</th>
      <td>
        <i class="pi pi-check"></i>
        <div>
          ion-spinner
          <a href="https://ionicframework.com/docs/api/spinner"
            ><i class="pi pi-external-link"></i
          ></a>
        </div>
      </td>
      <td>
        <div class="q-pa-md q-gutter-xs">
          <div class="q-gutter-md row justify-center" style="font-size: 2em">
            <q-spinner-ball color="red" />
            <q-spinner-clock color="brown" />
            <q-spinner-comment color="deep-purple" />
            <q-spinner-dots color="blue" />
            <q-spinner-gears color="cyan" />
            <q-spinner-grid color="teal" />
            <q-spinner-hearts color="green" />
            <q-spinner-hourglass color="light-green" />
            <q-spinner-ios color="pink" />
            <q-spinner-orbit color="blue" />
            <q-spinner-oval color="amber" />
            <q-spinner-pie color="orange" />
            <q-spinner-puff color="deep-orange" />
            <q-spinner-radio color="brown" />
            <q-spinner-rings color="grey" />
            <q-spinner-tail color="blue-grey" />
          </div>
        </div>
      </td>
      <td>
        <ProgressSpinner />
        <ProgressSpinner
          style="width: 50px; height: 50px"
          strokeWidth="8"
          fill="var(--surface-ground)"
          animationDuration=".5s"
          aria-label="Custom ProgressSpinner"
        />
      </td>
    </tr>
  </table>
</template>
<script setup lang="ts">
import { ref } from 'vue';
import Button from 'primevue/button';
import Calendar from 'primevue/calendar';
import Slider from 'primevue/slider';
import Dropdown from 'primevue/dropdown';
import FileUpload from 'primevue/fileupload';
import InputSwitch from 'primevue/inputswitch';
import ToggleButton from 'primevue/togglebutton';
import ProgressSpinner from 'primevue/progressspinner';

import { IonButton } from '@ionic/vue';

const date = ref();
const sliderValue = ref();
const selectedCity = ref();
const cities = ref([
  'Klagenfurt',
  'Wien',
  'Graz',
  'Linz',
  'Salzburg',
  'Innsbruck',
]);
const file = ref();
const time = ref();
const toggle = ref(false);
</script>
<style scoped>
td {
  border-left: 2px dotted lightgrey;
  padding: 15px;
  margin: auto;
  text-align: center;
}
td,
th {
  border-top: 2px dotted lightgrey;
}
th {
  padding: 5px;
}

tr:first-child th:not(:first-child) {
  border-left: 2px dotted lightgrey;
}
</style>
