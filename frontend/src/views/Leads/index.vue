<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">销售线索管理</h1>
    <el-table :data="leads" stripe>
      <el-table-column prop="name" label="姓名" />
      <el-table-column prop="company" label="公司" />
      <el-table-column prop="score" label="AI评分" />
      <el-table-column prop="score_label" label="意向等级" />
      <el-table-column prop="status" label="状态" />
    </el-table>
  </div>
</template>
<script setup lang="ts">
import { ref,onMounted } from "vue"
import { getLeads } from "../../api/leads"
const leads = ref([])
onMounted(async()=>{const res=await getLeads();leads.value=res.data})
</script>
