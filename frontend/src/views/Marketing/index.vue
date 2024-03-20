<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">营销活动</h1>
    <el-table :data="campaigns" stripe>
      <el-table-column prop="name" label="活动名称" />
      <el-table-column prop="status" label="状态" />
      <el-table-column prop="budget" label="预算(元)" />
      <el-table-column prop="spent" label="已花费(元)" />
      <el-table-column prop="leads_generated" label="获取线索" />
      <el-table-column prop="roi" label="ROI" />
    </el-table>
  </div>
</template>
<script setup lang="ts">
import { ref,onMounted } from "vue"
import api from "../../api/index"
const campaigns = ref([])
onMounted(async()=>{const res=await api.get("/marketing/campaigns");campaigns.value=res.data})
</script>
