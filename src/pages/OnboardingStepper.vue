<template>
  <div class="q-pa-md">
    <q-stepper v-model="step" ref="stepper" color="primary" animated>
      <q-step
        :name="1"
        title="Persönliche Daten"
        icon="fa-solid fa-1"
        :done="step > 1"
      >
        <div class="flex flex-col gap-10">
          <q-input
            v-model="patient.firstName"
            label="Vorname"
            class="md:max-w-64"
          />
          <q-input
            v-model="patient.lastName"
            label="Nachname"
            class="md:max-w-64"
          />
          <div>
            <q-btn-toggle
              v-model="patient.gender"
              toggle-color="primary"
              :options="[
                { label: 'Weiblich', value: 'female' },
                { label: 'Männlich', value: 'male' },
              ]"
            />
          </div>
          <div>
            <!-- <q-date v-model="patient.birthday" minimal /> -->
            <q-input
              filled
              v-model="patient.birthday"
              mask="date"
              :rules="['date']"
              label="Geburtsdatum"
              class="md:max-w-64"
            >
              <template v-slot:append>
                <q-icon name="event" class="cursor-pointer">
                  <q-popup-proxy
                    cover
                    transition-show="scale"
                    transition-hide="scale"
                  >
                    <q-date v-model="patient.birthday">
                      <div class="row items-center justify-end">
                        <q-btn
                          v-close-popup
                          label="OK"
                          color="primary"
                          flat
                          locale="de-AT"
                        />
                      </div>
                    </q-date>
                  </q-popup-proxy>
                </q-icon>
              </template>
            </q-input>
          </div>
          <div>
            <q-input
              v-model.number="patient.ssn"
              label="Sozialversicherungsnummer"
              type="number"
              class="md:max-w-64"
            />
          </div>
        </div>
      </q-step>

      <q-step
        :name="2"
        title="Allergien & Merkmale"
        icon="fa-solid fa-2"
        :done="step > 2"
      >
        <div padding class="max-w-120 max-w-4xl flex flex-col gap-8">
          <div class="grid grid-cols-2">
            <q-item class="md:max-w-80">
              <q-item-section>
                <q-item-label> Allergien </q-item-label>
                <q-input v-model="allergy" label="z.B. Pollen" />
              </q-item-section>
              <q-item-section side>
                <q-btn
                  icon="fa-solid fa-plus"
                  round
                  size="small"
                  @click="addAllergy"
                ></q-btn>
              </q-item-section>
            </q-item>

            <q-card class="w-full">
              <q-card-section>
                <div
                  v-if="patient.allergies.length == 0"
                  class="text-lg text-gray-600 text-center"
                >
                  Keine Allergien
                </div>
                <div v-else>
                  <div class="text-lg text-center">Allergien</div>
                  <ul>
                    <li v-for="allergy in patient.allergies" :key="allergy">
                      {{ allergy }}
                    </li>
                  </ul>
                </div>
              </q-card-section>
            </q-card>
          </div>
          <div class="grid grid-cols-2">
            <q-item class="md:max-w-80">
              <q-item-section>
                <q-item-label> Infektionen </q-item-label>
                <q-input v-model="infection" label="z.B. Hepatitis" />
              </q-item-section>
              <q-item-section side>
                <q-btn
                  icon="fa-solid fa-plus"
                  round
                  size="small"
                  @click="addInfection"
                ></q-btn>
              </q-item-section>
            </q-item>
            <q-card class="w-full">
              <q-card-section>
                <div
                  v-if="patient.infections.length == 0"
                  class="text-lg text-gray-600 text-center"
                >
                  Keine Infektionen
                </div>
                <div v-else>
                  <div class="text-lg text-center">Infektionen</div>
                  <ul>
                    <li
                      v-for="infection in patient.infections"
                      :key="infection"
                    >
                      {{ infection }}
                    </li>
                  </ul>
                </div>
              </q-card-section>
            </q-card>
          </div>
          <div class="grid grid-cols-2">
            <q-item class="md:max-w-80">
              <q-item-section>
                <q-item-label> Unverträglichkeiten </q-item-label>
                <q-input v-model="sensitivity" label="z.B. Lactose" />
              </q-item-section>
              <q-item-section side>
                <q-btn
                  icon="fa-solid fa-plus"
                  round
                  size="small"
                  @click="addSensitivity"
                ></q-btn>
              </q-item-section>
            </q-item>
            <q-card class="w-full">
              <q-card-section>
                <div
                  v-if="patient.sensitivities.length == 0"
                  class="text-lg text-gray-600 text-center"
                >
                  Keine Unverträglichkeiten
                </div>
                <div v-else>
                  <div class="text-lg text-center">Unverträglichkeiten</div>
                  <ul>
                    <li
                      v-for="sensitivity in patient.sensitivities"
                      :key="sensitivity"
                    >
                      {{ sensitivity }}
                    </li>
                  </ul>
                </div>
              </q-card-section>
            </q-card>
          </div>
        </div>
      </q-step>

      <q-step
        :name="3"
        title="Medizinische Geschichte"
        icon="fa-solid fa-3"
        :done="step > 3"
      >
        <div class="text-lg text-center">
          Gab es bei Ihnen oder Ihren Eltern wichtige medizinische Ereignisse?
        </div>
        <div class="grid grid-cols-12">
          <div class="col-span-6 grid grid-cols-12 gap-y-8 gap-x-2 mt-8">
            <div class="col-span-12 md:col-span-2 xl:col-span-1 text-lg">
              Wer?
            </div>
            <div class="col-span-12 md:col-span-10 xl:col-span-11">
              <q-btn-toggle
                v-model="medicalEvent.who"
                toggle-color="primary"
                :options="[
                  { label: 'Ich', value: 'ich' },
                  { label: 'Mutter', value: 'mutter' },
                  { label: 'Vater', value: 'vater' },
                ]"
              />
            </div>

            <div class="col-span-12 md:col-span-2 xl:col-span-1 text-lg">
              Was?
            </div>
            <div class="col-span-12 md:col-span-10 xl:col-span-11">
              <q-input v-model="medicalEvent.what" class="md:max-w-80" />
            </div>

            <div class="col-span-12 md:col-span-2 xl:col-span-1 text-lg">
              Wann?
            </div>
            <div class="col-span-12 md:col-span-10 xl:col-span-11">
              <q-input v-model="medicalEvent.when" class="md:max-w-80" />
            </div>
            <div class="col-span-12">
              <q-btn round icon="fa-solid fa-plus" @click="addMedicalEvent" />
            </div>
          </div>
          <div id="showMedicalEvents" class="col-span-6 mt-8">
            <q-card class="w-full">
              <q-card-section>
                <div
                  v-if="patient.medicalEvents.length == 0"
                  class="text-lg text-gray-600 text-center"
                >
                  Keine medizinischen Ereignisse
                </div>
                <div v-else>
                  <div class="text-lg text-center mb-4">
                    Medizinische Ereignisse
                  </div>
                  <div v-for="event in patient.medicalEvents" :key="event.id">
                    <q-chip removable class="p-6">
                      {{ event.who.toUpperCase() }}: {{ event.what }} ({{
                        event.when
                      }})
                    </q-chip>
                  </div>
                </div>
              </q-card-section>
            </q-card>
          </div>
        </div>
      </q-step>

      <q-step :name="4" title="Impfpass" icon="fa-solid fa-4">
        Lorem ipsum.
      </q-step>

      <template v-slot:navigation>
        <q-stepper-navigation class="mt-12">
          <q-btn
            @click="stepper.next()"
            color="primary"
            :label="step === 4 ? 'Fertig' : 'Weiter'"
          />
          <q-btn
            v-if="step > 1"
            flat
            color="primary"
            @click="stepper.previous()"
            label="Zurück"
            class="q-ml-sm"
          />
        </q-stepper-navigation>
      </template>
    </q-stepper>
  </div>
</template>
<script setup lang="ts">
import { QStepper } from 'quasar';
import { ref, reactive } from 'vue';

const stepper = ref();

const patient: Patient = reactive({
  firstName: '',
  lastName: '',
  gender: 'female',
  birthday: '',
  ssn: '',
  allergies: [],
  infections: [],
  sensitivities: [],
  medicalEvents: [],
});

const allergy = ref<string>();
const infection = ref();
const sensitivity = ref();

const step = ref(1);

function addAllergy() {
  if (!allergy.value) return;

  patient.allergies.push(allergy.value);
  allergy.value = '';
}

function addInfection() {
  if (!infection.value) return;

  patient.infections.push(infection.value);
  infection.value = '';
}

function addSensitivity() {
  if (!sensitivity.value) return;

  patient.sensitivities.push(sensitivity.value);
  sensitivity.value = '';
}

const medicalEvent = ref<MedicalEvent>({
  who: 'ich',
  what: '',
  when: '',
  id: 0,
});

function addMedicalEvent() {
  let oldId = medicalEvent.value.id;
  patient.medicalEvents.push(medicalEvent.value);
  medicalEvent.value = {
    who: 'ich',
    what: '',
    when: '',
    id: oldId + 1,
  };
}

interface Patient {
  firstName: string;
  lastName: string;
  gender: string;
  birthday: any;
  ssn: number | string;
  allergies: string[];
  infections: string[];
  sensitivities: string[];
  medicalEvents: MedicalEvent[];
}

interface MedicalEvent {
  who: 'ich' | 'mutter' | 'vater';
  what: string;
  when: string;
  id: number;
}
</script>
