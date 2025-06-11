<template>
  <div class="card">
    <h2 class="text-xl font-bold text-primary mb-4">Task Status</h2>
    <ul class="divide-y divide-gray-200">
      <li v-for="(status, index) in statuses" :key="index" class="py-2 flex justify-between">
        <span>{{ status.task }}</span>
        <span :class="status.state === 'completed' ? 'text-green-600' : 'text-yellow-600'">
          {{ status.state }}
        </span>
      </li>
    </ul>
  </div>
</template>

<script setup>
const statuses = [
  { task: 'Scan app A', state: 'completed' },
  { task: 'Scan app B', state: 'pending' }
]
</script>