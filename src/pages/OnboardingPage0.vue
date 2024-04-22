<template>
  <div class="grid grid-cols-12 mr-0 ml-0 mt-0 text-800">
    <div
      class="col-span-12 md:col-span-6 p-6 text-center md:text-left flex items-center"
    >
      <section>
        <span class="block text-6xl font-bold mb-1">Herzlich Willkommen</span>
        <div class="text-6xl text-primary-600 font-bold mb-8">im PAPO</div>
        <p class="mt-0 mb-8 text-700 line-height-3 text-xl">
          Mit dem neuen Patientenportal der Humanomed Gruppe haben Sie Zugriff
          zu den Dokumenten Ihrer Aufenthalte, sehen den Verlauf Ihrer
          Vitalwerte und können eigene Einträge erstellen oder Dokumente
          hochladen.
        </p>
        <div class="flex gap-x-4 justify-center mt-4">
          <Button
            label="Mehr erfahren"
            type="button"
            outlined
            size="large"
          ></Button>
          <Button
            label="Onboarding starten"
            type="button"
            class="mr-3 p-button-raised"
            size="large"
          ></Button>
        </div>
      </section>
    </div>
    <div class="col-span-12 md:col-span-6 overflow-hidden">
      <img
        src="https://picsum.photos/id/106/2592/1728"
        alt="Image"
        class="md:ml-auto block md:h-full"
        style="clip-path: polygon(8% 0, 100% 0%, 100% 100%, 0 100%)"
      />
    </div>
  </div>
</template>
<script setup lang="ts">
// color #16A34A
import Button from 'primevue/button';
</script>
