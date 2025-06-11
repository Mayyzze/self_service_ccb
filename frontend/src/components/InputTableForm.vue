<template>
  <div class="card">
    <form @submit.prevent="submit" class="space-y-4 text-center">
      <div class="w-full flex justify-start">
        <div class="flex items-center space-x-4">
          <input type="file" class="hidden" id="file-upload" @change="handleFileUpload" accept=".xlsx, .xls" />
          <label for="file-upload" class="px-5 py-2 bg-gray-200 text-gray-800 font-medium border border-gray-400 rounded cursor-pointer hover:bg-gray-300 transition">
          Upload Excel Input for Security Control Analysis
        </label>
        <span v-if="fileName" class="text-sm text-gray-600 italic">{{ fileName }}</span>
      </div>
      </div>

      <div v-if="rows.length" class="max-h-[calc(7*2.5rem)] overflow-y-auto border">
        <table v-if="rows.length" class="w-full border text-sm border-collapse">
          <thead class="bg-gray-200 text-center">
            <tr>
              <th v-for="(header, index) in headers" :key="index" class="px-2 py-1 border border-gray-300 text-gray-700">
                {{ header }}
              </th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(row, rowIndex) in rows" :key="rowIndex">
              <td v-for="(colIndex, i) in headers.length" :key="i" class="px-2 py-1 border border-gray-300">
                {{ row[i] ?? '' }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <div class="flex justify-center">
        <button type="submit" class="btn btn-primary">Launch Analysis</button>
      </div>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import * as XLSX from 'xlsx'

const headers = ref([])
const rows = ref([])
const fileName = ref('')

const handleFileUpload = (event) => {
  const file = event.target.files[0]
  if (!file) return
  event.target.value = '' // <-- force reset so same file triggers again
  fileName.value = file.name

  const reader = new FileReader()
  reader.onload = (e) => {
    const data = new Uint8Array(e.target.result)
    const workbook = XLSX.read(data, { type: 'array' })
    const sheetName = workbook.SheetNames[0]
    const worksheet = XLSX.utils.sheet_to_json(workbook.Sheets[sheetName], { header: 1 })
    console.log('Parsed worksheet:', worksheet)


    if (worksheet.length) {
      headers.value = worksheet[0]
      rows.value = worksheet.slice(1)
    }
  }
  reader.readAsArrayBuffer(file)
}

const submit = () => {
  console.log('Submitted rows:', rows.value)
}
</script>