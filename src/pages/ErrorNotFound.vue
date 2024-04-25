<template>
  <div
    class="flex items-center justify-center min-h-screen bg-cover bg-center bg-no-repeat"
    style="background-image: url('https://picsum.photos/id/11/2500/1667')"
  >
    <div
      class="max-w-md mx-auto text-center bg-white bg-opacity-90 p-8 rounded-lg shadow-lg"
    >
      <div class="text-9xl font-bold text-primary-600 mb-4">404</div>
      <h1 class="text-4xl font-bold text-gray-800 mb-6">Page Not Found</h1>
      <p class="text-lg text-gray-600 mb-8">
        Diese Seite existiert leider nicht.
      </p>

      <q-btn
        class="q-mt-xl text-4xl"
        color="white"
        text-color="primary"
        to="/"
        label="Zurück zur Startseite"
        no-caps
        size="xl"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
defineOptions({
  name: 'ErrorNotFound',
});
</script>
