<template>
  <div class="min-h-screen bg-white flex flex-col items-center px-4 pt-4 pb-5">
    <h1 class="text-3xl font-bold text-primary mb-10 text-center">SAST/SCA Security Gate</h1>
    <div class="w-full max-w-6xl space-y-8">
      <!-- Insert your components here -->
      <InputTableForm />
      <StatusDisplay />
      <AnalysisResult />
    </div>
  </div>
</template>

<script setup>
import InputTableForm from './components/InputTableForm.vue'
import StatusDisplay from './components/StatusDisplay.vue'
import AnalysisResult from './components/AnalysisResult.vue'
</script>