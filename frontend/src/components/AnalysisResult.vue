<template>
  <div class="card">
    <h2 class="text-xl font-bold text-primary mb-4">Analysis Results</h2>
    <div v-if="results.length > 0" class="space-y-2">
      <div v-for="(result, index) in results" :key="index" class="border p-4 rounded bg-gray-200">
        <h3 class="font-semibold">{{ result.title }}</h3>
        <p class="text-sm text-gray-700">{{ result.details }}</p>
      </div>
    </div>
    <p v-else class="text-gray-500 italic">No results available.</p>
  </div>
</template>

<script setup>
const results = [
  { title: 'App A Analysis', details: 'No critical vulnerabilities.' },
  { title: 'App B Analysis', details: '1 high severity finding.' }
]
</script>
